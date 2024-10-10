import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
imagem = cv2.imread('./Laplaciano/placa.png')
imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

# Filtro Laplaciano
filtro_laplaciano = cv2.Laplacian(imagem_rgb, cv2.CV_64F)

# Mostrar o resultado
cv2.imshow("Imagem Original",imagem)
cv2.imshow("Imagem Filtro Laplacian", filtro_laplaciano)

cv2.waitKey(0)
cv2.destroyAllWindows()