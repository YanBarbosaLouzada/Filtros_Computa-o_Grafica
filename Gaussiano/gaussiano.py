import cv2
import matplotlib.pyplot as plt
import numpy as np


# Carregar a imagem
imagem = cv2.imread('./Trabalho_2/Gaussiano/placa.png')


# Filtro de suavização (Gaussiano)
filtro_gaussiano = cv2.GaussianBlur(imagem, (7, 7), 0)


# Mostrar o resultado
cv2.imshow("Imagem Original",imagem)
cv2.imshow("Imagem Filtro Gaussiano", filtro_gaussiano)

cv2.waitKey(0)
cv2.destroyAllWindows()
