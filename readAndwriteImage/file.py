
from PIL import Image, ImageDraw, ImageFont

# Pil :PIL is the Python Imaging Library which provides the python interpreter with image editing capabilities

im = Image.open('sample.jpg') # Open Image
width, height =im.size

draw = ImageDraw.Draw(im)
text = input("Enter Your Name ")    #user Input

if len(text) > 40:                  #Overflow Text Elipise
   str1=text[:40]+"..."
   text=str1 
else:
    text 


color = (0,0,0) #font color

font = ImageFont.truetype('arial.ttf', 30)  # Font Family and font Size
textwidth, textheight = draw.textsize(text, font)  

draw.text((455, 253), text,fill=color, align='left',font=font ) # calculate the Width,Height  
im.show() 
im.save('sample3.jpg') #Save image