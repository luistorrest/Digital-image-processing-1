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

# Cargar la imagen
a = cv2.imread('carro (1).jpg')

# Mostrar la imagen original
cv2.imshow('Imagen original', a)
cv2.waitKey(0)

# Convertir la imagen a espacio de color HSV
b = cv2.cvtColor(a, cv2.COLOR_BGR2HSV)

# Mostrar la imagen en espacio de color HSV
cv2.imshow('Imagen en espacio de color HSV', b)
cv2.waitKey(0)

# Normalizar la imagen en espacio de color HSV
c = normalize(b)

# Mostrar la imagen normalizada
cv2.imshow('Imagen normalizada en espacio de color HSV', c)
cv2.waitKey(0)

# Convertir la imagen a espacio de color LAB
d = cv2.cvtColor(a, cv2.COLOR_BGR2LAB)

# Mostrar la imagen en espacio de color LAB
cv2.imshow('Imagen en espacio de color LAB', d)
cv2.waitKey(0)

# Normalizar la imagen en espacio de color LAB
e = normalize(d)

# Mostrar la imagen normalizada
cv2.imshow('Imagen normalizada en espacio de color LAB', e)
cv2.waitKey(0)

# Extraer componentes RGB
c1, c2, c3 = componentes(a)

# Mostrar las componentes RGB
cv2.imshow('Componentes RGB', np.hstack([c1, c2, c3]))
cv2.waitKey(0)

# Extraer componentes de la imagen en espacio de color HSV
c1, c2, c3 = componentes(b)
cs = c2

# Mostrar las componentes en espacio de color HSV
cv2.imshow('Componentes HSV', np.hstack([c1, c2, c3]))
cv2.waitKey(0)

# Extraer componentes de la imagen normalizada en espacio de color LAB
c1, c2, c3 = componentes(e)
cb = c3

# Ajustar el contraste de la componente cb
cb = cv2.equalizeHist(cb)

# Mostrar las componentes en espacio de color LAB
cv2.imshow('Componentes LAB', np.hstack([c1, c2, c3]))
cv2.waitKey(0)

# Mostrar las componentes cs y cb
cv2.imshow('Componente cs', cs)
cv2.waitKey(0)
cv2.imshow('Componente cb', cb)
cv2.waitKey(0)

# Guardar las componentes cb y cs como imágenes
cv2.imwrite('cb.jpg', cb)
cv2.imwrite('cs.jpg', cs)

# Limpiar pantalla
cv2.destroyAllWindows()

