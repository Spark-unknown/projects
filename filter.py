import cv2
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk

def load_image():
    # Load the image
    img_path = filedialog.askopenfilename()
    img = cv2.imread(img_path)

    # Check if image is loaded correctly
    if img is None:
        messagebox.showerror("Error", "Unable to load image.")
    else:
        # Convert image to selected color space
        color_space = color_space_var.get()
        if color_space == "Grayscale":
            converted_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            converted_img = cv2.cvtColor(converted_img, cv2.COLOR_GRAY2BGR)
        elif color_space == "HSV":
            converted_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        elif color_space == "LAB":
            converted_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        elif color_space == "RGB":
            converted_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        elif color_space == "YUV":
            converted_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
        elif color_space == "YCrCb":
            converted_img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

        # Resize image to half screen size
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        img_width = int(screen_width / 2)
        img_height = int(screen_height / 2)
        resized_img = cv2.resize(converted_img, (img_width, img_height))

        # Display the resized image
        global image_label_img
        image_label_img = ImageTk.PhotoImage(Image.fromarray(resized_img))
        image_label.config(image=image_label_img)

def save_image():
    # Save the image
    img_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", ".png"), ("SVG", ".svg")])
    if img_path:
        # Get the image from the label
        img = ImageTk.getimage(image_label_img)
        if img_path.endswith(".svg"):
            img.save(img_path, format="SVG")
        else:
            img.save(img_path)

def copy_image():
    # Copy the image to clipboard
    root.clipboard_clear()
    root.clipboard_append(image_label_img)

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

# Create a variable to store the selected color space
color_space_var = tk.StringVar()
color_space_var.set("Grayscale")

# Create a dropdown menu for color space selection
color_space_menu = ttk.OptionMenu(button_frame, color_space_var, "Grayscale", "HSV", "LAB", "RGB", "YUV", "YCrCb", command=load_image)
color_space_menu.pack(pady=10)

# Create buttons
load_button = tk.Button(button_frame, text="Load Image", command=load_image, font=("Arial", 16))
load_button.pack(pady=10)

save_button = tk.Button(button_frame, text="Save Image", command=save_image, font=("Arial", 16))
save_button.pack(pady=10)

copy_button = tk.Button(button_frame, text="Copy Image", command=copy_image, font=("Arial", 16))
copy_button.pack(pady=10)

root.mainloop()