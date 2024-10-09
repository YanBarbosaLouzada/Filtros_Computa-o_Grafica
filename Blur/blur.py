import cv2
import matplotlib.pyplot as plt

# Carregar a imagem
imagem = cv2.imread('./Trabalho_2/Blur/placa.png')
imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

# Filtro de Média (Blur)
filtro_media = cv2.blur(imagem_rgb, (7, 7))

# Mostrar o resultado
cv2.imshow('Filtro de Média', filtro_media)
cv2.imshow("Imagem Original",imagem)


cv2.waitKey(0)
cv2.destroyAllWindows()