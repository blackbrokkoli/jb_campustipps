from PIL import Image, ImageDraw, ImageColor, ImageFilter, ImageFont
import random

# import background
l1 = Image.open("s2.jpg")

# scale to ideal Instagram size
scale = 1080 / l1.width
l1 = l1.resize((int(l1.width*scale), int(l1.height*scale)))
if l1.height < 1080:
    scale = 1080 / l1.height
    l1 = l1.resize((int(l1.width*scale), int(l1.height*scale)))

# crop to Instagram size
c1 = 0 + (l1.width - 1080) / 2
c2 = 0 + (l1.height - 1080) / 2
c3 = c1 + 1080
c4 = c2 + 1080

# crop, make greyscale
l1 = l1.crop((c1,c2,c3,c4)).convert('LA').convert('RGBA')
# blur background
l1 = l1.filter(ImageFilter.GaussianBlur(radius=3))

# Paste counter template on top

l2 = Image.open("bg_0002.png")
l1.paste(l2, (0,0), l2)

# Add rectangles

z1 = random.randint(-20,20)/10
z2 = random.randint(-20,20)/10

r1 = Image.new('RGBA', ((1200, 200)), (0, 170, 255)).rotate(z1, expand=True)
r2 = Image.new('RGBA', ((1200, 200)), (0, 170, 255)).rotate(z2, expand=True)


l1.paste(r1, (-50, 350), r1)
l1.paste(r2, (-50, 685), r2)
l1.save("post.png")
