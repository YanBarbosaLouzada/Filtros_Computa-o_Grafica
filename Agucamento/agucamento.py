import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
imagem = cv2.imread('./Agucamento/placa.png')
imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

# Filtro de aguçamento (Kernel)
kernel = np.array([[0, -1, 0], 
                   [-1, 5, -1], 
                   [0, -1, 0]])

filtro_agucamento = cv2.filter2D(imagem_rgb, -1, kernel)

# Mostrar o resultado
cv2.imshow("Imagem Original",imagem)
cv2.imshow("Imagem Filtro Aguçamento", filtro_agucamento)

cv2.waitKey(0)
cv2.destroyAllWindows()