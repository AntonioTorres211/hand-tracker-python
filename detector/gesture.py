import pyautogui #biblioteca para automação de tarefas, utilizada para simular ações do teclado e mouse, permitindo que o programa controle o computador com base nos gestos reconhecidos pela função gestos.
import time

from controller import all_fingers, aumentar_volume, diminuir_volume, index_middle, index_middle_ring, onlyindex #Importa as funções onlyindex, indeMiidder, indexMiderRingfinger e allFinger do módulo controller, para simular ações do teclado com base nos gestos reconhecidos pela função gestos.

def gestos(lm): #Função para verificar se apenas o dedo indicador está levantado, utilizando as coordenadas dos pontos de referência da mão detectada. Por que usar lm? Porque é a variável que armazena as coordenadas dos pontos de referência da mão detectada, e é necessário para verificar a posição dos dedos e não depende de bibliotecas externas, tornando a função mais modular e reutilizável nem do main.py, permitindo que seja facilmente integrada em diferentes contextos ou projetos. ele é uma lista que armezaa numeros.

    indicadory = [lm[8].y, lm[7].y, lm[6].y, lm[5].y] 
    indicadorx = [lm[8].x, lm[7].x, lm[6].x, lm[5].x]
    medioy = [lm[12].y, lm[11].y, lm[10].y, lm[9].y] 
    mediox = [lm[12].x, lm[11].x, lm[10].x, lm[9].x] 
    anelary = [lm[16].y, lm[15].y, lm[14].y, lm[13].y] 
    mindinhoy = [lm[20].y, lm[19].y, lm[18].y, lm[17].y] 
    dedaoy = [lm[4].y, lm[3].y, lm[2].y, lm[1].y] 
    dedaox = [lm[4].x, lm[3].x, lm[2].x, lm[1].x]   
    distancia = (lm[8].x - lm[4].x) ** 2 + (lm[8].y - lm[4].y) ** 2
        
        
    if (
        indicadory[0] < indicadory[2]) and (medioy[0] > medioy[2]) and (anelary[0] > anelary[2]) and (mindinhoy[0] > mindinhoy[2] and dedaox[0] < dedaox[1]):
        return "onlyindex"
    elif (
        indicadory[0] < indicadory[2]) and (medioy[0] < medioy[2]) and (anelary[0] > anelary[2]) and (mindinhoy[0] > mindinhoy[2] and dedaox[0] < dedaox[1]):
        return "index_middle"
    elif (
        indicadory[0] < indicadory[2]) and (medioy[0] < medioy[2]) and (anelary[0] < anelary[2]) and (mindinhoy[0] > mindinhoy[2] and dedaox[0] < dedaox[1]):
        return "index_middle_ring"
    elif (
        indicadory[0] < indicadory[2]) and (medioy[0] < medioy[2]) and (anelary[0] < anelary[2]) and (mindinhoy[0] < mindinhoy[2] and dedaox[0] > dedaox[1]):
        return "all_fingers"
    elif (
        indicadory[0] < indicadory[2]) and (medioy[0] < medioy[2]) and (anelary[0] < anelary[2]) and (mindinhoy[0] < mindinhoy[2] and dedaox[0] > dedaox[1]):
        return "all_fingers"
    elif (
        indicadorx[0] > indicadorx[1] and indicadorx[1] > indicadorx[2] and indicadorx[2] > indicadorx[3]
        and dedaox[0] > dedaox[1] and dedaox[1] > dedaox[2] and dedaox[2] > dedaox[3]
        and mediox[0] > mediox[1] and mediox[1] > mediox[2] and mediox[2] > mediox[3]
        and anelary[0] > anelary[2]
        and mindinhoy[0] > mindinhoy[2]
        and distancia > 0.05
    ):
        return "diminuir_volume"    
    elif (
        indicadorx[0] > indicadorx[1] and indicadorx[1] > indicadorx[2] and indicadorx[2] > indicadorx[3]
        and dedaox[0] > dedaox[1] and dedaox[1] > dedaox[2] and dedaox[2] > dedaox[3]
        and medioy[0] > medioy[2]
        and anelary[0] > anelary[2]
        and mindinhoy[0] > mindinhoy[2]
        and distancia > 0.05
    ):
        return "aumentar_volume"

    else:
        return "Nenhum gesto reconhecido"
