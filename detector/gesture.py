

def only_index(lm): #Função para verificar se apenas o dedo indicador está levantado, utilizando as coordenadas dos pontos de referência da mão detectada. Por que usar lm? Porque é a variável que armazena as coordenadas dos pontos de referência da mão detectada, e é necessário para verificar a posição dos dedos e não depende de bibliotecas externas, tornando a função mais modular e reutilizável nem do main.py, permitindo que seja facilmente integrada em diferentes contextos ou projetos. ele é uma lista que armezaa numeros.
    
    indicador = lm[8].y < lm[6].y
    medio = lm[12].y > lm[10].y
    anelar = lm[16].y > lm[14].y
    mindinho = lm[20].y > lm[18].y

    if indicador and medio and anelar and mindinho:
        return print("Apenas o dedo indicador está levantado")
    else:
        return print("Outro gesto detectado")