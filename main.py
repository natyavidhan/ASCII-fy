from PIL import Image, ImageDraw, ImageFont
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font
from tkinter import filedialog


class App:
    def __init__(self, root):
        root.title("ASCII-fy")
        width = 500
        height = 300
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        self.font = Font(family="Consolas", size=10)
        applabel = tk.Label(root, text="ASCII-fy Image",
                            font=("Consolas", 30), fg="black")
        applabel.place(x=90, y=26)
        self.imagepath = tk.StringVar()
        imagepathinput = ttk.Entry(
            root, textvariable=self.imagepath, font=self.font)
        imagepathinput.place(x=30, y=90, width=312, height=20)
        imagepathchooser = ttk.Button(
            root, text="Choose Image", command=self.chooseImage)
        imagepathchooser.place(x=350, y=90, width=120, height=20)

        self.outputfolder = tk.StringVar()
        outputfolderinput = ttk.Entry(
            root, textvariable=self.outputfolder, font=self.font)
        outputfolderinput.place(x=30, y=130, width=312, height=20)
        outputfolderchooser = ttk.Button(
            root, text="Choose Output Folder", command=self.chooseOutputFolder)
        outputfolderchooser.place(x=350, y=130, width=120, height=20)

        self.imageReduce = tk.IntVar()
        self.imageReduce.set(1)
        imageReduceInput = ttk.Entry(
            root, textvariable=self.imageReduce, font=self.font)
        imageReduceInput.place(x=200, y=200, width=30, height=20)
        imageReducelable = tk.Label(
            root, text="Image Reduction", font=self.font)
        imageReducelable.place(x=30, y=200)

        startButton = ttk.Button(root, text="Start", command=self.start)
        startButton.place(x=200, y=250, width=100, height=30)

    def convert(self, imagePath, reduce):
        shades = " .:-=+*#%@"
        img = Image.open(imagePath)
        img = img.convert("L")
        asciiImage = ""
        img = img.resize((img.size[0]//reduce, img.size[1]//reduce))
        img_width, img_height = img.size
        for y in range(img_height):
            for x in range(img_width):
                pix = img.getpixel((x, y))
                asciiImage += shades[int((pix/255)*(len(shades)-1))] + " "
            asciiImage += "\n"
        return asciiImage

    def toImage(self, asciiImage, folderPath):
        img = Image.new("RGB", (len(asciiImage.split(
            "\n")[0]*6), len(asciiImage.split("\n"))*12), "black")
        d1 = ImageDraw.Draw(img)
        font = ImageFont.truetype("Consolas.ttf", 10)
        d1.text((0, 0), asciiImage, font=font, fill=(255, 255, 255))
        img.save(folderPath + "/ascii.png")
        open(folderPath + "/ascii.txt", "w").write(asciiImage)

    def chooseImage(self):
        path = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("png files", "*.png"), ("jpeg files", "*.jpg"), ("all files", "*.*")))
        if path:
            self.imagepath.set(path)

    def chooseOutputFolder(self):
        path = filedialog.askdirectory(initialdir="/", title="Select folder")
        if path:
            self.outputfolder.set(path)

    def start(self):
        try:
            asciiImage = self.convert(
                self.imagepath.get(), self.imageReduce.get())
            self.toImage(asciiImage, self.outputfolder.get())
        except Exception as e:
            messagebox.showerror("Error", e)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
