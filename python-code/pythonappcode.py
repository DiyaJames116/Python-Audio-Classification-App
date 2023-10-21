import tensorflow as tf
import numpy as np
import io
import csv
import pandas as pd
from scipy.io import wavfile

# Download the model to yamnet.tflite
interpreter = tf.lite.Interpreter('/Users/diyajames/Desktop/audio-main/yamnet_tflite_model.tflite')

def ensure_sample_rate(original_sample_rate, waveform,
                       desired_sample_rate=16000):
  # Resample waveform if required
  if original_sample_rate != desired_sample_rate:
    desired_length = int(round(float(len(waveform)) /
                               original_sample_rate * desired_sample_rate))
    waveform = scipy.signal.resample(waveform, desired_length)
  return desired_sample_rate, waveform

input_details = interpreter.get_input_details()
waveform_input_index = input_details[0]['index']
output_details = interpreter.get_output_details()
scores_output_index = output_details[0]['index']
embeddings_output_index = output_details[1]['index']
spectrogram_output_index = output_details[2]['index']

wav_file_name = 'Speaker_0000_00083.wav'
sample_rate, wav_data = wavfile.read(wav_file_name)
sample_rate, wav_data = ensure_sample_rate(sample_rate, wav_data)

# Calculate duration
duration = len(wav_data) / sample_rate
print(f'Total duration: {duration:.2f}s')

# Normalize the waveform
waveform = wav_data.astype(np.float32) / np.float32(np.iinfo(np.int16).max)

interpreter.resize_tensor_input(waveform_input_index, [len(waveform)], strict=True)
interpreter.allocate_tensors()
interpreter.set_tensor(waveform_input_index, waveform)
interpreter.invoke()
scores, embeddings, spectrogram = (
    interpreter.get_tensor(scores_output_index),
    interpreter.get_tensor(embeddings_output_index),
    interpreter.get_tensor(spectrogram_output_index))
# print(scores.shape, embeddings shape, spectrogram.shape)  # (N, 521) (N, 1024) (M, 64)

# Download the YAMNet class map (see main YAMNet model docs) to yamnet_class_map.csv
# See YAMNet TF2 usage sample for class_names_from_csv() definition.
class_map_path = '/Users/diyajames/Desktop/audio-main/yamnet_class_map.csv'
class_names = list(pd.read_csv(class_map_path)['display_name'])
prediction = np.mean(scores, axis=0)
top5_i = np.argsort(prediction)[::-1][:5]
result = []
result.append(f'Total duration: {duration:.2f}s')
result.append(class_names[scores.mean(axis=0).argmax()])
result.append(f'{wav_file_name} :\n' + '\n'.join(f'  {class_names[i]:12s}: {prediction[i]:.3f}' for i in top5_i))

# Confidence threshold
conf_threshold = 0.8
count = 0
for i in top5_i:
    if class_names[i] == 'Silence':
        if prediction[i] >= conf_threshold:
            count += 1
    else:
        continue
result.append(f'Silence count: {count}')

# Write the result to a .txt file
with open('output.txt', 'w') as output_file:
    output_file.write('\n'.join(result))

print("Results have been written to output.txt.")

