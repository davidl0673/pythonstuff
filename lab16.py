from PIL import Image
img = Image.open("image.png") #Same directory as this script
width, height = img.size
pixels = img.load()

for x in range(width):
  for y in range (height):
    r, g, b = pixels[x, y]
    #Alter RGB Values
    brightness = int(0.299*r + 0.587*g + 0.114*b)
    pixels[x, y] = (brightness, brightness, brightness)
img.show()