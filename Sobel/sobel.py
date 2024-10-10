import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
imagem = cv2.imread('./Sobel/placa.png')
imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

# Filtro de realce de bordas (Sobel)
sobel_x = cv2.Sobel(imagem_rgb, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(imagem_rgb, cv2.CV_64F, 0, 1, ksize=3)
filtro_sobel = cv2.magnitude(sobel_x, sobel_y)

cv2.imshow("Imagem Original",imagem)
cv2.imshow("Imagem Filtro Sobel", filtro_sobel)

cv2.waitKey(0)
cv2.destroyAllWindows()