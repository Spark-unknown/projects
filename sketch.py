import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def load_image():
    # Load the image
    img_path = filedialog.askopenfilename()
    img = cv2.imread(img_path)

    # Check if image is loaded correctly
    if img is None:
        messagebox.showerror("Error", "Unable to load image.")
    else:
        # Convert image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply threshold
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

        # Display the thresholded image
        thresh_img = Image.fromarray(thresh)
        thresh_img = ImageTk.PhotoImage(thresh_img)
        image_label.config(image=thresh_img)
        image_label.image = thresh_img

def save_image():
    # Save the image
    img_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", ".png"), ("SVG", ".svg")])
    if img_path:
        # Get the image from the label
        img = image_label.image
        img = ImageTk.getimage(img)
        if img_path.endswith(".svg"):
            img.save(img_path, format="SVG")
        else:
            img.save(img_path)

def copy_image():
    # Copy the image to clipboard
    root.clipboard_clear()
    root.clipboard_append(image_label.image)

root = tk.Tk()

# Create a frame for image
image_frame = tk.Frame(root)
image_frame.pack(side=tk.LEFT)

# Create a label to display the image
image_label = tk.Label(image_frame)
image_label.pack()

# Create a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(side=tk.RIGHT)

# Create buttons
load_button = tk.Button(button_frame, text="Load Image", command=load_image, font=("Arial", 16))
load_button.pack(pady=10)

save_button = tk.Button(button_frame, text="Save Image", command=save_image, font=("Arial", 16))
save_button.pack(pady=10)

copy_button = tk.Button(button_frame, text="Copy Image", command=copy_image, font=("Arial", 16))
copy_button.pack(pady=10)

root.mainloop()