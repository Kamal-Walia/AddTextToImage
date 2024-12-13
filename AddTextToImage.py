# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
 
# Open an Image
img = Image.open('test.png')
 
# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)
 
# Add Text to an image
font = ImageFont.truetype("fonts/Roboto-Regular.ttf", 60)
# Name
I1.text((350, 1000), "Kamal Walia", font=font, fill=(0, 0, 0))
font = ImageFont.truetype("fonts/Roboto-Regular.ttf", 50)
# CVV
I1.text((1600, 540), "1001", font=font, fill=(0, 0, 0)) 
# Member Since
I1.text((1270, 890), "22", font=font, fill=(0, 0, 0)) 
# Display edited image
img.show()
 
# Save the edited image
img.save("test_updated.png")