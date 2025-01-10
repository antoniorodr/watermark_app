from tkinter import Tk, Button, filedialog, Label
from tkinter.messagebox import showinfo
from PIL import Image
import os

def gui():
    window = Tk()
    window.title("Watermarking APP")
    window.config(padx = 100, pady = 50, bg = "#9bdeac")
    window.eval('tk::PlaceWindow . center')

    button = Button(text = "Upload", font = ("Courier", 20, "bold"), command = upload_file)
    button.grid(column = 0, row = 4)

    text = Label(text = "Choose your file", font = ("Courier", 20, "bold"), fg = "#9bdeac", bg = "#f7f5dd")
    text.grid(column = 0, row = 6)

    window.mainloop()

def upload_file():
    file = filedialog.askopenfilename(title="Select a File", filetypes=[("PNG files", "*.png"), ("JPG files", "*.jpg")])
    return add_watermark(file)

def add_watermark(file):
    image = Image.open(file)
    watermark = Image.open("watermark/default.png")
    position = (10, 10)
    image.paste(watermark, position, watermark)
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    output_path = os.path.join(downloads_path, "output_image.png")
    image.save(output_path)
    image.close()
    watermark.close()
    showinfo("Done!", "Watermark added. Please check your Downloads folder.")


if __name__ == "__main__":
    gui()