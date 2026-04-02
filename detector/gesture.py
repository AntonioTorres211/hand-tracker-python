import pyautogui #biblioteca para automação de tarefas, utilizada para simular ações do teclado e mouse, permitindo que o programa controle o computador com base nos gestos reconhecidos pela função gestos.
import time #biblioteca para manipulação de tempo, utilizada para adicionar atrasos entre as ações simuladas pelo pyautogui, garantindo que as ações sejam executadas de forma mais natural e evitando sobrecarga do sistema.

def gestos(lm): #Função para verificar se apenas o dedo indicador está levantado, utilizando as coordenadas dos pontos de referência da mão detectada. Por que usar lm? Porque é a variável que armazena as coordenadas dos pontos de referência da mão detectada, e é necessário para verificar a posição dos dedos e não depende de bibliotecas externas, tornando a função mais modular e reutilizável nem do main.py, permitindo que seja facilmente integrada em diferentes contextos ou projetos. ele é uma lista que armezaa numeros.
        
    indicador = [lm[8].y, lm[7].y, lm[6].y, lm[5].y] 
    medio = [lm[12].y, lm[11].y, lm[10].y, lm[9].y] 
    anelar = [lm[16].y, lm[15].y, lm[14].y, lm[13].y] 
    mindinho = [lm[20].y, lm[19].y, lm[18].y, lm[17].y] 
    time.sleep(1)
    if (
        indicador[0] < indicador[2]) and (medio[0] > medio[2]) and (anelar[0] > anelar[2]) and (mindinho[0] > mindinho[2]):
        pyautogui.press("k")
        return print("Apenas o dedo indicador está levantado")

    elif (
        indicador[0] < indicador[2]) and (medio[0] < medio[2]) and (anelar[0] > anelar[2]) and (mindinho[0] > mindinho[2]):
        return print("O dedo indicador e o dedo médio estão levantados")
    else:
        return print("Nenhum gesto reconhecido")
