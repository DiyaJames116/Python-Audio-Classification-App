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
import tensorflow as tf
import numpy as np
import io
import csv
import pandas as pd
from scipy.io import wavfile
```

For Android (Java):
```java
import android.os.Bundle;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import java.io.BufferedReader;
import java.io.InputStreamReader;
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
   git clone https://github.com/yourusername/your-repo.git
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


## License

This Python Audio Classification App is licensed under the [MIT License](LICENSE).

---

Feel free to include images of the app's output in the 'images' directory and reference them in the readme where relevant, like the "Sample Output" image shown above.
