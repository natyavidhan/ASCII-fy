from PIL import Image, ImageDraw, ImageFont


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
    img.save("ascii.png")

asciiImage = convert("input/christmas.png", 1)
toImage(asciiImage)
open("ascii.txt", "w").write(asciiImage)
