import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Cargar la imagen
a = np.array(Image.open('texto.png'))

# Convertir a escala de grises
b = np.array(Image.fromarray(a).convert('L'))

# Mostrar imagen b
plt.figure()
plt.imshow(b, cmap='gray')
plt.gca().set_title('Imagen en escala de grises')
plt.colorbar()
plt.show()

# Transponer la imagen c
c = b.T

# Mostrar imagen c
plt.figure()
plt.imshow(c, cmap='gray')
plt.gca().set_title('Imagen transpuesta')
plt.colorbar()
plt.show()

# Calcular la suma de cada columna en c
d = np.sum(c, axis=0)

# Mostrar gráfico de la suma
plt.figure()
plt.plot(d)
plt.title('Suma de columnas')
plt.xlabel('Columna')
plt.ylabel('Suma')
plt.show()

# Seleccionar una región de interés en b
e = b[10:41, :]

# Mostrar imagen e
plt.figure()
plt.imshow(e, cmap='gray')
plt.gca().set_title('Región de interés 1')
plt.colorbar()
plt.show()

# Seleccionar otra región de interés en b
f = b[70:91, :]

# Mostrar imagen f
plt.figure()
plt.imshow(f, cmap='gray')
plt.gca().set_title('Región de interés 2')
plt.colorbar()
plt.show()

# Calcular la suma de cada columna en f
g = np.sum(f, axis=0)

# Mostrar gráfico de la suma de columnas en f
plt.figure()
plt.plot(g)
plt.title('Suma de columnas en ROI 2')
plt.xlabel('Columna')
plt.ylabel('Suma')
plt.show()

# Seleccionar una región de interés en f
h = f[:, 290:361]

# Mostrar imagen h
plt.figure()
plt.imshow(h, cmap='gray')
plt.gca().set_title('Región de interés 3')
plt.colorbar()
plt.show()
