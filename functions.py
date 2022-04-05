from PIL import Image, ImageDraw, ImageFont
from datetime import datetime


def convert(imagePath: str, reduce: float) -> str:
    """
    Convert an image to ASCII art

    :param imagePath: The path to the image you want to convert
    :type imagePath: str
    :param reduce: The amount by which the image is reduced
    :type reduce: float
    :return: A string of characters representing the image.
    """
    shades = " .:-=+*#%@"
    img = Image.open(imagePath)
    img = img.convert("L")
    asciiImage = []
    img = img.resize((img.size[0] // reduce, img.size[1] // reduce))
    img_width, img_height = img.size
    for y in range(img_height):
        for x in range(img_width):
            pix = img.getpixel((x, y))
            asciiImage.append(shades[round((pix / 255) * (len(shades) - 1))] + " ")
        asciiImage.append("\n")
    return "".join(asciiImage)


def toImage(asciiImage: str, folderPath: str) -> None:
    """
    Converts an ASCII art image to a PNG image

    :param asciiImage: The ascii image to be converted to an image
    :type asciiImage: str
    :param folderPath: The path to the folder where the image will be saved
    :type folderPath: str
    """
    img = Image.new(
        "RGB",
        (len(asciiImage.split("\n")[0] * 6), len(asciiImage.split("\n")) * 12),
        "black",
    )
    d1 = ImageDraw.Draw(img)
    font = ImageFont.truetype("Consolas.ttf", 10)
    d1.text((0, 0), asciiImage, font=font, fill=(255, 255, 255))
    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    img.save(f"{folderPath}/ascii ({date}).png")
    open(f"{folderPath}/ascii ({date}).txt", "w").write(asciiImage)
