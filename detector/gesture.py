import pyautogui #biblioteca para automação de tarefas, utilizada para simular ações do teclado e mouse, permitindo que o programa controle o computador com base nos gestos reconhecidos pela função gestos.
import time

from controller import all_fingers, index_middle, index_middle_ring, onlyindex #Importa as funções onlyindex, indeMiidder, indexMiderRingfinger e allFinger do módulo controller, para simular ações do teclado com base nos gestos reconhecidos pela função gestos.

def gestos(lm, String): #Função para verificar se apenas o dedo indicador está levantado, utilizando as coordenadas dos pontos de referência da mão detectada. Por que usar lm? Porque é a variável que armazena as coordenadas dos pontos de referência da mão detectada, e é necessário para verificar a posição dos dedos e não depende de bibliotecas externas, tornando a função mais modular e reutilizável nem do main.py, permitindo que seja facilmente integrada em diferentes contextos ou projetos. ele é uma lista que armezaa numeros.

    indicadory = [lm[8].y, lm[7].y, lm[6].y, lm[5].y] 
    medioy = [lm[12].y, lm[11].y, lm[10].y, lm[9].y] 
    anelary = [lm[16].y, lm[15].y, lm[14].y, lm[13].y] 
    mindinhoy = [lm[20].y, lm[19].y, lm[18].y, lm[17].y] 
    dedaoy = [lm[4].y, lm[3].y, lm[2].y, lm[1].y] 
    dedaox = [lm[4].x, lm[3].x, lm[2].x, lm[1].x]         
        
        
    if (
        indicadory[0] < indicadory[2]) and (medioy[0] > medioy[2]) and (anelary[0] > anelary[2]) and (mindinhoy[0] > mindinhoy[2] and dedaox[0] < dedaox[1]):
        onlyindex()
    elif (
        indicadory[0] < indicadory[2]) and (medioy[0] < medioy[2]) and (anelary[0] > anelary[2]) and (mindinhoy[0] > mindinhoy[2] and dedaox[0] < dedaox[1]):
        index_middle()
    elif (
        indicadory[0] < indicadory[2]) and (medioy[0] < medioy[2]) and (anelary[0] < anelary[2]) and (mindinhoy[0] > mindinhoy[2] and dedaox[0] < dedaox[1]):
        index_middle_ring()
    elif (
        indicadory[0] < indicadory[2]) and (medioy[0] < medioy[2]) and (anelary[0] < anelary[2]) and (mindinhoy[0] < mindinhoy[2] and dedaox[0] > dedaox[1]):
        all_fingers()
    else:
        return "Nenhum gesto reconhecido"
