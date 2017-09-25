from PIL import Image
import numpy as np

img = Image.open("1_1.tif")
(imageWidth, imageHeight)=img.size
print(imageWidth, imageHeight)

n = 16

k = imageWidth/n
l = imageHeight/n

k = int(k)
l = int(l)



for i in range(0, l-1):
	for j in range(0, k-1):
		print(i," ",j," ",k," ",l," ",n)
		img2 = img.crop((i*n, j*n, n*i+n, n*j+n))
		img2.save("row-"+str(i+1)+"-col-"+str(j+1)+".png")

