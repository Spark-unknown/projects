import tkinter as tk
from threading import Thread
import cv2
import numpy as np
import pyautogui
import pyaudio
import wave

class ScreenRecorder:
    def __init__(self, root):
        self.root = root
        self.root.title("Screen Recorder")
        self.root.geometry("300x100")

        self.recording = False
        self.video_writer = None
        self.audio_writer = None

        self.start_button = tk.Button(self.root, text="Start Recording", command=self.start_recording)
        self.start_button.pack()

        self.stop_button = tk.Button(self.root, text="Stop Recording", command=self.stop_recording)
        self.stop_button.pack()

    def start_recording(self):
        self.recording = True
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.screen_recording_thread = Thread(target=self.record_screen)
        self.screen_recording_thread.start()
        self.audio_recording_thread = Thread(target=self.record_audio)
        self.audio_recording_thread.start()

    def stop_recording(self):
        self.recording = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")

    def record_screen(self):
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.video_writer = cv2.VideoWriter('screen_recording.avi', fourcc, 12.0, (pyautogui.size()[0], pyautogui.size()[1]))
        while self.recording:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.video_writer.write(frame)
        self.video_writer.release()

    def record_audio(self):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        RECORD_SECONDS = 1000000
        WAVE_OUTPUT_FILENAME = "audio_recording.wav"

        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        frames = []

        while self.recording:
            data = stream.read(CHUNK)
            frames.append(data)

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

root = tk.Tk()
app = ScreenRecorder(root)
root.mainloop()