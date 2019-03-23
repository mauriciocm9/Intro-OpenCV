import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny(image):
    """
    Primero tomamos la imagen y la convertimos a escalas de grises
    Usamos GaussianBlur para eliminar el ruido con un kernel de 5x5
    Por ultimo usamos Canny para obtener los bordes
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 103)
    return canny

if __name__ == '__main__':
    img = cv2.imread('imagen.png')
    edges = canny(img)
    # plt.imshow(edges)
    # plt.show()
    cv2.imshow('Bordes', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
