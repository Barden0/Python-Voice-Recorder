import tkinter as tk
import sounddevice as sd
import numpy as np
from threading import Thread
from pydub import AudioSegment

# Initialize recording variables
recording_data = []
recording_stream = None

# Function to start recording
def start_recording():
    global recording_data, recording_stream
    recording_data = []
    recording_stream = sd.InputStream(samplerate=44100, channels=2, callback=record_callback)
    recording_stream.start()

# Callback function for audio recording
def record_callback(indata, frames, time, status):
    global recording_data
    recording_data.append(indata.copy())

# Function to stop recording and save to MP3
def stop_recording():
    global recording_data, recording_stream
    if recording_stream:
        recording_stream.stop()
        recording_stream.close()
        audio_data = np.concatenate(recording_data, axis=0)
        audio_segment = AudioSegment(
            audio_data.tobytes(),
            frame_rate=44100,
            sample_width=audio_data.dtype.itemsize,
            channels=2
        )
        audio_segment.export("recording.mp3", format="mp3")
        print("Recording saved as recording.mp3")

# GUI setup
root = tk.Tk()
root.title("Audio Recorder")

start_button = tk.Button(root, text="Start Recording", command=start_recording)
start_button.pack(pady=20)

stop_button = tk.Button(root, text="Stop Recording", command=stop_recording)
stop_button.pack(pady=20)

root.mainloop()

