from PIL import Image, ImageDraw, ImageFont
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font
from tkinter import filedialog

def convert(imagePath, reduce):
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

def toImage(asciiImage):
    img = Image.new("RGB", (len(asciiImage.split("\n")[0]*6), len(asciiImage.split("\n"))*12), "black")
    d1 = ImageDraw.Draw(img)
    font = ImageFont.truetype("Consolas.ttf", 10)
    d1.text((0, 0), asciiImage, font=font, fill=(255, 255, 255))
    try:
        img.save("output/ascii.png")
    except:
        os.mkdir("output")
        img.save("output/ascii.png")


class App:
    def __init__(self, root):
        root.title("ASCII-fy")
        width=500
        height=475
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        self.font = Font(family="Consolas", size=10)
        applabel = tk.Label(root, text="ASCII-fy Image", font=("Consolas", 30), fg="black")
        applabel.place(x=90, y=26)
        self.imagepath = tk.StringVar()
        self.imagepathinput = ttk.Entry(root, textvariable=self.imagepath, font=self.font)
        self.imagepathinput.place(x=30, y=90, width=312, height=20)
        self.imagepathchooser = ttk.Button(root, text="Choose Image", command=self.chooseImage)
        self.imagepathchooser.place(x=350, y=90, width=120, height=20)
        
        self.outputfolder = tk.StringVar()
        self.outputfolderinput = ttk.Entry(root, textvariable=self.outputfolder, font=self.font)
        self.outputfolderinput.place(x=30, y=130, width=312, height=20)
        self.outputfolderchooser = ttk.Button(root, text="Choose Output Folder", command=self.chooseOutputFolder)
        self.outputfolderchooser.place(x=350, y=130, width=120, height=20)
        
    
    def chooseImage(self):
        path = filedialog.askopenfilename(initialdir = "/",title = "Select file",
                                          filetypes = (("png files","*.png"), ("jpeg files","*.jpg"),("all files","*.*")))
        if path:
            self.imagepath.set(path)
    
    def chooseOutputFolder(self):
        path = filedialog.askdirectory(initialdir = "/",title = "Select folder")
        if path:
            self.outputfolder.set(path)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()