from matplotlib import image as img
import PIL
import scipy._lib

image = img.imread("flower.jpg")
image.shape()

r = []
g = []
b = []

for line in image:
    for pixel in line:
        temp_r, temp_g, temp_b = pixel

        r.append(temp_r)
        g.append(temp_g)
        b.append(temp_b)



