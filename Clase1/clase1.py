import cv2
import numpy as np

# Cargar la imagen
a = cv2.imread('imagen.jpg')

# Crear una copia de la imagen original
a1 = a.copy()

# Mostrar la imagen original
cv2.imshow('Imagen original', a)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Convertir la imagen a escala de grises
b = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)

# Mostrar la imagen en escala de grises
cv2.imshow('Imagen en escala de grises', b)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Mostrar el histograma de la imagen
hist = cv2.calcHist([b], [0], None, [256], [0, 256])
plt.plot(hist)
plt.xlabel('Valor de píxel')
plt.ylabel('Frecuencia')
plt.title('Histograma de la imagen en escala de grises')
plt.show()

# Crear una copia de la imagen en escala de grises
c = b.copy()

# Establecer píxeles por debajo de 100 y por encima de 150 a 0
c[c < 100] = 0
c[c > 150] = 0

# Mostrar la imagen con píxeles modificados
cv2.imshow('Imagen con píxeles modificados', c)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Establecer píxeles no nulos a 255
c[c > 0] = 255

# Mostrar la imagen con píxeles modificados
cv2.imshow('Imagen con píxeles modificados', c)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Crear una imagen en color con los píxeles modificados
e = cv2.merge([c, c, c])

# Aplicar la máscara a la imagen original
a[e == 0] = 0

# Mostrar la imagen resultante
cv2.imshow('Imagen con máscara aplicada', a)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Crear una copia de la imagen en escala de grises
f = b.copy()

# Establecer píxeles por debajo de 150 y por encima de 200 a 0
f[f < 150] = 0
f[f > 200] = 0

# Establecer píxeles no nulos a 255
f[f > 0] = 255

# Mostrar la imagen con píxeles modificados
cv2.imshow('Imagen con píxeles modificados', f)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Crear una imagen en color con los píxeles modificados
g = cv2.merge([f, f, f])

# Aplicar la máscara a la imagen original
a1[g == 0] = 0

# Mostrar la imagen resultante
cv2.imshow('Imagen con máscara aplicada', a1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Obtener dimensiones de la imagen original
fil, col, cap = a.shape
area_total = fil * col

# Crear una copia binarizada de la imagen
d = c.copy()
d[d > 0] = 1

# Calcular el área de píxeles no nulos
area_l = np.sum(d)

# Imprimir el área total y el área de píxeles no nulos
print("Área total:", area_total)
print("Área de píxeles no nulos:", area_l)

