import cv2
import tkinter as tk
from PIL import Image, ImageTk
import os


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.cap = cv2.VideoCapture(0)
        self.image_count = 0
        self.create_widgets()
        self.update_frame()

    def create_widgets(self):
        self.image_label = tk.Label(self)
        self.image_label.pack()

        self.capture_button = tk.Button(self)
        self.capture_button["text"] = "Capture"
        self.capture_image_method = self.capture_image  # Define method before using
        self.capture_button["command"] = self.capture_image_method
        self.capture_button.pack(side="top")

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            cv2_im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2_im)
            imgtk = ImageTk.PhotoImage(image=img)
            self.image_label.config(image=imgtk)
            self.image_label.image = imgtk  # keep a reference
        self.after(10, self.update_frame)

    def capture_image(self):
        ret, frame = self.cap.read()
        if ret:
            self.image_count += 1
            folder_name = "captured_images"
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
            filename = f"{folder_name}/image_{self.image_count}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Image captured and saved as {filename}")


root = tk.Tk()
app = Application(master=root)
app.mainloop()