#### import modules ####
from PIL import Image, ImageDraw

#### load image objects ####
im1 = Image.open("white.bmp")
draw1 = ImageDraw.Draw(im1)

#### blank the image out ####
draw1.rectangle([(0,0),(im1.size[0], im1.size[1])], fill=255)

#### divide the image up ####
sectors = 51
imsize = im1.size

'''
#### draw points for squares ####
for i in [int(x*(imsize[0]/sectors)) for x in range(sectors)]:
    for j in [int(y*(imsize[1]/sectors)) for y in range(sectors)]:
        draw1.point((i,j), fill=1)

'''
#### 
for i in [int(x*(imsize[0]/sectors)) for x in range(sectors)]:
    for j in [int(y*(imsize[1]/sectors)) for y in range(sectors)]:
        draw1.point((i+int(imsize[0]/(2*sectors)),j+int(imsize[1]/(2*sectors))), fill=200)

#### draw boxes ####
for i in [int(x*(imsize[0]/sectors)) for x in range(0,sectors,2)]:
    for j in [int(y*(imsize[1]/sectors)) for y in range(0,sectors, 2)]:
        draw1.rectangle([(i,j),(i+int(imsize[0]/sectors),j+int(imsize[1]/sectors))], outline=1, fill=200)

#### draw dark boxes ####
for i in [int(x*(imsize[0]/sectors)) for x in range(int(int(imsize[0]/sectors)/2),sectors,2)]:
    for j in [int(y*(imsize[1]/sectors)) for y in range(int(int(imsize[0]/sectors)/2),sectors, 2)]:
        draw1.rectangle([(i,j),(i+int(imsize[0]/sectors),j+int(imsize[1]/sectors))], outline=1, fill=100)

'''
#### draw gridlines ####
for (i,j) in [(int(x*(imsize[0]/sectors)),int(x*(imsize[1]/sectors))) for x in range(sectors)]:
    draw1.line([(i,0), (i,imsize[1])], fill=1, width=1)
    draw1.line([(0,j), (imsize[0],j)], fill=1, width=1)
'''

#### draw the rectangle ####
#draw1.rectangle([(10,10), (200,200)], fill= 230, outline=1)

#### now show image and close ####
im1.show()
'''
print(imsize)
print([int(x*(imsize[0]/sectors)) for x in range(sectors)])
print(int(imsize[0]/sectors))
print(int(imsize[0]/(2*sectors)))
'''
