# Python Voice Recorder

Python Voice Recorder is a simple Python application that enables you to record audio. It has a simple graphical user interface. It utilizes the `tkinter` library for creating the GUI, `sounddevice` for audio recording, and `pydub` for audio conversion to MP3 format.

## Features

- **Start Recording:** Click the "Start Recording" button to initiate the audio recording. The application will continue recording until you click the "Stop Recording" button.
- **Stop Recording:** Click the "Stop Recording" button to halt the audio recording. The recorded audio will be saved as "recording.mp3" in the application directory.

## Prerequisites

Ensure you have Python installed on your system. If not, you can download it from the [official Python website](https://www.python.org/downloads/).

Additionally, install the required Python packages using the following command:

```bash
pip install sounddevice pydub
```

## How to Use

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/username/python-voice-recorder.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd python-voice-recorder
   ```

3. **Run the Application:**
   ```bash
   python gui.py
   ```

4. **Using the GUI:**
   - The GUI window will appear. Click the "Start Recording" button to commence recording audio.
   - To stop the recording, click the "Stop Recording" button. The recorded audio will be saved as "recording.mp3" in the application directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
