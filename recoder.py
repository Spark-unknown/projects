import pyaudio
import wave
import tkinter as tk
from threading import Thread

class VoiceRecorder:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Recorder")
        self.root.geometry("300x100")

        self.recording = False

        self.start_button = tk.Button(self.root, text="Start Recording", command=self.start_recording)
        self.start_button.pack()

        self.stop_button = tk.Button(self.root, text="Stop Recording", command=self.stop_recording)
        self.stop_button.pack()

        self.play_button = tk.Button(self.root, text="Play Recording", command=self.play_recording)
        self.play_button.pack()

    def start_recording(self):
        self.recording = True
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.play_button.config(state="disabled")
        self.recording_thread = Thread(target=self.record)
        self.recording_thread.start()

    def stop_recording(self):
        self.recording = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.play_button.config(state="normal")

    def record(self):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        RECORD_SECONDS = 5
        WAVE_OUTPUT_FILENAME = "output.wav"

        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
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

    def play_recording(self):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        WAVE_OUTPUT_FILENAME = "output.wav"

        p = pyaudio.PyAudio()
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'rb')

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=CHANNELS,
                        rate=RATE,
                        output=True)

        data = wf.readframes(CHUNK)

        while data:
            stream.write(data)
            data = wf.readframes(CHUNK)

        stream.stop_stream()
        stream.close()
        p.terminate()

root = tk.Tk()
app = VoiceRecorder(root)
root.mainloop()