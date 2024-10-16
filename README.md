# Análise de Filtros de Imagem

Este README documenta os resultados da aplicação de diferentes filtros de imagem, incluindo aguçamento, média, gaussiano, laplaciano e Sobel.

![image](https://github.com/user-attachments/assets/0a8de2aa-d77b-4201-a927-bb059c07673a)

## Filtros Aplicados

1. **Aguçamento**: Realça detalhes da imagem, acentuando bordas e áreas de transição.
2. **Filtro de Média**: Suaviza a imagem, reduzindo o ruído ao calcular a média dos pixels vizinhos.
3. **Filtro Gaussiano**: Suaviza a imagem de maneira eficiente, mantendo as bordas mais preservadas em comparação ao filtro de média.
4. **Filtro Laplaciano**: Realça bordas e contornos, destacando mudanças bruscas de intensidade.
5. **Filtro de Sobel**: Detecta bordas ao calcular gradientes de intensidade nas direções horizontal e vertical.

## Análise dos Resultados

### 1. Como a imagem original mudou após a aplicação de cada filtro?

![image](https://github.com/user-attachments/assets/7f7cf86b-bf37-4711-9354-fde299090ce3)

![image](https://github.com/user-attachments/assets/722f3af1-e635-4650-8c88-608b89345cd9)

![image](https://github.com/user-attachments/assets/f0d310bb-b5c3-4790-9f75-c444473683e6)

- **Aguçamento**: A imagem ficou mais nítida e os detalhes mais pronunciados, especialmente nas bordas e áreas de transição.
- **Filtro de Média**: A imagem ficou suavizada, com perda de detalhes, especialmente nas bordas.
- **Filtro Gaussiano**: A suavização foi mais uniforme e suave, preservando melhor as bordas enquanto reduzia o ruído.
- **Filtro Laplaciano**: As bordas ficaram destacadas, e a imagem realçou contornos com mais clareza.
- **Filtro Sobel**: As bordas se tornaram mais proeminentes, mostrando claramente gradientes de intensidade horizontal e vertical.

### 2. Qual filtro foi mais eficaz para suavizar a imagem?

- O **filtro Gaussiano** foi o mais eficaz na suavização da imagem, pois aplica uma suavização suave e mantém as bordas mais preservadas em comparação com o filtro de média.

### 3. E qual foi mais eficaz para destacar as bordas?

- O **filtro Sobel** foi o mais eficaz para destacar as bordas, com um excelente realce dos gradientes de intensidade em direções específicas (horizontal e vertical). O **Laplaciano** também destacou contornos, mas foi mais sensível ao ruído.

### 4. Quais situações podem exigir o uso de cada tipo de filtro em um projeto real?

- **Aguçamento**: Utilizado em projetos de realce de detalhes, como em edições de fotos ou aprimoramento de imagens médicas.
- **Filtro de Média**: Adequado para situações de redução de ruído em imagens simples, como no pré-processamento para segmentação.
- **Filtro Gaussiano**: Ideal para redução de ruído em aplicações de visão computacional, como reconhecimento de faces ou objetos.
- **Filtro Laplaciano**: Útil em detecção de bordas e contornos em imagens, principalmente para detecção de objetos ou análise de imagens médicas.
- **Filtro Sobel**: Comumente utilizado para detecção de bordas em visão computacional, como em robótica, análise de padrões e reconhecimento de objetos.

