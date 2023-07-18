import numpy as np
import cv2
from mayavi import mlab

# Carregar a imagem em formato PNG
imagem_png = cv2.imread('Logo2.png')
# Converter a imagem para tons de cinza
imagem_cinza = cv2.cvtColor(imagem_png, cv2.COLOR_BGR2GRAY)
# Obter as dimensões da imagem
altura, largura = imagem_cinza.shape
# Criar um grid 2D para os pontos da imagem
x, y = np.meshgrid(np.arange(0, largura), np.arange(0, altura))
# Converter as coordenadas x, y e os valores dos pixels em arrays 1D
x = x.ravel()
y = y.ravel()
z = np.zeros_like(x)
intensidades = imagem_cinza.ravel()

# Exibir a imagem 3D usando a biblioteca Mayavi
mlab.figure(bgcolor=(1, 1, 1))
mlab.points3d(x, y, z, intensidades, mode='cube', scale_mode='none')
mlab.show()