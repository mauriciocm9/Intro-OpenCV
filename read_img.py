import cv2
import numpy as np


'''
imread toma 2 parametros
direccion de la imagen
flag indicando como leer la imagen:
  1 = color (por defecto)
  0 = escala de grises
'''
img = cv2.imread('imagen.png', 1)
cv2.imshow('Titulo', img)
print(type(img), img.shape)

p = cv2.waitKey(5000)
print(p)

'''
Tambien podemos mostrar imagenes
con matplotlib:
  plt.imshow(image)
  plt.show()
'''

img_gray = cv2.imread('imagen.png', 0)
cv2.imshow('Gray Scale', img_gray)
print(img_gray.shape)

# Esperamos cualquier tecla sea presionada
# y destruimos la ventana con el nombre asociado
cv2.waitKey(0)
cv2.destroyWindow('Gray Scale')

cv2.waitKey(0)
cv2.destroyAllWindows()



