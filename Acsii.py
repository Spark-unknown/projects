import tkinter as tk

def generate_ascii_art(image_path):
    from PIL import Image

    img = Image.open(image_path)
    img = img.resize((100, 50))
    img = img.convert('L')
    ascii_art = ''
    chars = '@%#*+=-:. '

    for y in range(img.height):
        for x in range(img.width):
            pixel = img.getpixel((x, y))
            ascii_art += chars[min(pixel // 25, len(chars) - 1)]
        ascii_art += '\n'

    return ascii_art

class ASCIIArtDisplay:
    def __init__(self, root):
        self.root = root
        self.root.title("ASCII Art Display")

        self.text_widget = tk.Text(root, font=("Courier", 10))
        self.text_widget.pack(fill="both", expand=True)

        self.display_button = tk.Button(root, text="Display ASCII Art", command=self.display_ascii_art)
        self.display_button.pack()

    def display_ascii_art(self):
        image_path = "ironman.png"
        ascii_art = generate_ascii_art(image_path)
        self.text_widget.delete(1.0, tk.END)
        self.text_widget.insert(tk.END, ascii_art)

if __name__ == "__main__":
    root = tk.Tk()
    root.attributes("-fullscreen", True)  # Set window to full screen
    app = ASCIIArtDisplay(root)
    root.mainloop()