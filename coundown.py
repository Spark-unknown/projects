import tkinter as tk
from threading import Thread
import time
import winsound
import tkinter.ttk as ttk

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer App")
        self.root.geometry("300x250")  # Set initial window size

        # Create tabs
        self.tabs = ttk.Notebook(root)
        self.stopwatch_tab = tk.Frame(self.tabs)
        self.countdown_tab = tk.Frame(self.tabs)
        self.converter_tab = tk.Frame(self.tabs)
        self.tabs.add(self.stopwatch_tab, text="Stopwatch")
        self.tabs.add(self.countdown_tab, text="Countdown")
        self.tabs.add(self.converter_tab, text="Converter")
        self.tabs.pack(fill="both", expand=True)  # Make tabs expand to fill window

        # Stopwatch tab
        self.stopwatch_label = tk.Label(self.stopwatch_tab, text="00:00:00", font=("Helvetica", 24))
        self.stopwatch_label.pack()
        self.stopwatch_button = tk.Button(self.stopwatch_tab, text="Start", command=self.start_stopwatch)
        self.stopwatch_button.pack()
        self.stopwatch_reset_button = tk.Button(self.stopwatch_tab, text="Reset", command=self.reset_stopwatch)
        self.stopwatch_reset_button.pack()

        # Countdown tab
        self.countdown_label = tk.Label(self.countdown_tab, text="00:00:00", font=("Helvetica", 24))
        self.countdown_label.pack()
        self.countdown_entry_label = tk.Label(self.countdown_tab, text="Enter seconds:")
        self.countdown_entry_label.pack()
        self.countdown_entry = tk.Entry(self.countdown_tab)
        self.countdown_entry.pack()
        self.countdown_button = tk.Button(self.countdown_tab, text="Start", command=self.start_countdown)
        self.countdown_button.pack()
        self.countdown_reset_button = tk.Button(self.countdown_tab, text="Reset", command=self.reset_countdown)
        self.countdown_reset_button.pack()

        # Converter tab
        self.converter_label = tk.Label(self.converter_tab, text="Second Converter", font=("Helvetica", 24))
        self.converter_label.pack()
        self.converter_hours_label = tk.Label(self.converter_tab, text="Hours:")
        self.converter_hours_label.pack()
        self.converter_hours_entry = tk.Entry(self.converter_tab)
        self.converter_hours_entry.pack()
        self.converter_minutes_label = tk.Label(self.converter_tab, text="Minutes:")
        self.converter_minutes_label.pack()
        self.converter_minutes_entry = tk.Entry(self.converter_tab)
        self.converter_minutes_entry.pack()
        self.converter_seconds_label = tk.Label(self.converter_tab, text="Seconds:")
        self.converter_seconds_label.pack()
        self.converter_seconds_entry = tk.Entry(self.converter_tab)
        self.converter_seconds_entry.pack()
        self.converter_button = tk.Button(self.converter_tab, text="Convert", command=self.convert_time)
        self.converter_button.pack()
        self.converter_result_label = tk.Label(self.converter_tab, text="Result:")
        self.converter_result_label.pack()
        self.converter_result_entry = tk.Entry(self.converter_tab)
        self.converter_result_entry.pack()

        self.running = False
        self.seconds = 0

    def start_stopwatch(self):
        if not self.running:
            self.running = True
            self.stopwatch_button.config(text="Stop")
            self.thread = Thread(target=self.increment_time)
            self.thread.start()
        else:
            self.running = False
            self.stopwatch_button.config(text="Start")

    def increment_time(self):
        while self.running:
            time.sleep(1)
            self.seconds += 1
            hours, remainder = divmod(self.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            self.stopwatch_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")

    def reset_stopwatch(self):
        self.running = False
        self.seconds = 0
        self.stopwatch_label.config(text="00:00:00")
        self.stopwatch_button.config(text="Start")

    def start_countdown(self):
        if not self.running:
            self.running = True
            self.countdown_button.config(text="Stop")
            self.seconds = int(self.countdown_entry.get())
            self.thread = Thread(target=self.decrement_time)
            self.thread.start()
        else:
            self.running = False
            self.countdown_button.config(text="Start")

    def reset_countdown(self):
        self.running = False
        self.seconds = 0
        self.countdown_label.config(text="00:00:00")
        self.countdown_button.config(text="Start")

        def decrement_time(self):
            while self.seconds > 0 and self.running:
                time.sleep(1)
                self.seconds -= 1
                hours, remainder = divmod(self.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.countdown_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
            if self.running:
                winsound.Beep(2500, 1000)
                self.countdown_label.config(text="Time's up!")
                self.running = False
                self.countdown_button.config(text="Start")

    def convert_time(self):
        hours = int(self.converter_hours_entry.get()) if self.converter_hours_entry.get() else 0
        minutes = int(self.converter_minutes_entry.get()) if self.converter_minutes_entry.get() else 0
        seconds = int(self.converter_seconds_entry.get()) if self.converter_seconds_entry.get() else 0
        total_seconds = hours * 3600 + minutes * 60 + seconds
        self.converter_result_entry.delete(0, tk.END)
        self.converter_result_entry.insert(0, str(total_seconds))

root = tk.Tk()
app = TimerApp(root)
root.mainloop()