# Python Audio Classification App

1. [Python Audio Classification App](#python-audio-classification-app)
   - [Introduction](#introduction)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
   - [Usage](#usage)
   - [Images](#images)
   - [License](#license)

## Introduction

This Python Audio Classification App is designed to identify and classify the type of noise present in an input .wav file. It leverages a tflite YAMNET model for audio classification and displays the detected sounds along with the probability of the audio class. The output is saved in a .txt file and presented by the app. Currently, the app exclusively displays the output of the Python model.

The application was initially developed to determine if an audio stream is silent. This functionality is achieved by dividing the audio into 2-second chunks and assessing whether the stream is entirely silent.


## Prerequisites

Before you can use the Python Audio Classification App, ensure you have the following libraries installed:

```python
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import csv
import matplotlib.pyplot as plt
from IPython.display import Audio
from scipy.io import wavfile
import io
import pandas as pd
```

For Android (Kotlin):
```kotlin
import android.os.Bundle;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import java.io.BufferedReader;
import java.io.InputStreamReader;
```

## Installation

To get started, follow these installation instructions:

1. Clone this repository to your local machine.
   ```
   gh repo clone DiyaJames116/Python-Audio-Classification-App
   ```

2. Install the required Python libraries if not already installed.
   ```bash
   pip install tensorflow tensorflow-hub numpy matplotlib scipy
   ```

3. Install the Android Studio or Android Studio (Kotlin) IDE on your development machine.

4. Open the Android project in Android Studio (located in the `android/` directory).

5. Build and run the Android app on your Android device or emulator.

## Usage

To use the Python Audio Classification App:

1. Launch the app on your Android device.

2. Choose an input .wav file that you want to classify.

3. The app will process the audio file and display the detected sounds and their corresponding probabilities.

## Images
 **Output of the python code that displays the class of the 2 seconds split audio.**
 ![Sample Output](./output/SC1.png)
 
 Note: This is the output of the last few seconds of the audio. The audio class with the highest score is displayed first
 
 ![Sample Output](./output/SC2.png)

**Output of the Android app**

![Sample Output](./output/c1.png)

The output of the pyhton program is written into the output.txt file
![Sample Output](./output/c2.png)

Success message that is shown when the output.txt file is updated with the result of the python code
![Sample Output](./output/c3.png)

The output shown on the emulator screen in Android Studio.

![Sample Output](./output/c4.png)

## License

This Python Audio Classification App is licensed under the [MIT License](LICENSE).

