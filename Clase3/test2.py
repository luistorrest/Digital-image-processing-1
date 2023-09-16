import cv2
import numpy as np

def componentes(a):
    c1, c2, c3 = cv2.split(a)
    return c1, c2, c3

def normalize(a):
    a = np.double(a)
    a = a / np.max(a)
    b = np.uint8(a * 255)
    return b

# Limpiar variables y pantalla
cv2.destroyAllWindows()

# Cargar las imágenes cb y cs
cb = cv2.imread('cb.jpg', cv2.IMREAD_GRAYSCALE)
cs = cv2.imread('cs.jpg', cv2.IMREAD_GRAYSCALE)

# Mostrar las imágenes cb y cs
cv2.imshow('Componente cb', cb)
cv2.imshow('Componente cs', cs)
cv2.waitKey(0)

# Cargar la imagen original
a = cv2.imread('carro (1).jpg')

# Convertir la componente cb a una imagen binaria
_, b = cv2.threshold(cb, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
b = normalize(b)

# Mostrar la imagen binaria
cv2.imshow('Imagen binaria', b)
cv2.waitKey(0)

# Crear una imagen en color con la componente binaria
c = cv2.merge([b, b, b])

# Aplicar la máscara a la imagen original
d = a.copy()
d[c == 0] = 0

# Mostrar la imagen original y la imagen con la máscara
cv2.imshow('Imagen original', a)
cv2.imshow('Imagen con máscara aplicada', d)
cv2.waitKey(0)

# Limpiar pantalla
cv2.destroyAllWindows()

