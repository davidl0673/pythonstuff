from PIL import Image , ImageDraw

img = Image.new('RGB', (500,500))

draw = ImageDraw.Draw(img)
draw.rectangle(((0, 0), (500, 500)), fill="white")



draw.line((250, 100, 250,300), fill ="black", width= 8)

draw.ellipse(( 200,200,350,350), fill="black")

img.show()                                                      #make a stick figureee or some shit 