from PIL import Image
import cv2
import matplotlib.pyplot as plt

imagen_1 = Image.open('images/imagen_1.jpg')
imagen_2 = Image.open('images/imagen_2.jpg')


# PRESENTAMOS LAS IMAGENES USANDO PLT.
plt.figure(figsize = (5,4))
plt.imshow(imagen_1)
plt.axis('off')

plt.figure(figsize = (10,6))
plt.imshow(imagen_2)
plt.axis('off')