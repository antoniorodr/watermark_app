from tkinter import Tk, Button, filedialog, Label
from PIL import Image

def gui():
    window = Tk()
    window.title("Watermarking APP")
    window.config(padx = 100, pady = 50, bg = "#9bdeac")

    button = Button(text = "Upload", font = ("Courier", 20, "bold"), command = upload_file)
    button.grid(column = 0, row = 4)

    text = Label(text = "Choose your file", font = ("Courier", 20, "bold"), fg = "#9bdeac", bg = "#f7f5dd")
    text.grid(column = 0, row = 6)

    window.mainloop()

def upload_file():
    file = filedialog.askopenfilename(title="Select a File", filetypes=[("PNG files", "*.png"), ("JPG files", "*.jpg")])
    return file


if __name__ == "__main__":
    gui()