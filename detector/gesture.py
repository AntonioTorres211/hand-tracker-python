import pyautogui #biblioteca para automação de tarefas, utilizada para simular ações do teclado e mouse, permitindo que o programa controle o computador com base nos gestos reconhecidos pela função gestos.
import time #biblioteca para manipulação de tempo, utilizada para adicionar atrasos entre as ações simuladas pelo pyautogui, garantindo que as ações sejam executadas de forma mais natural e evitando sobrecarga do sistema.

def gestos(lm, String): #Função para verificar se apenas o dedo indicador está levantado, utilizando as coordenadas dos pontos de referência da mão detectada. Por que usar lm? Porque é a variável que armazena as coordenadas dos pontos de referência da mão detectada, e é necessário para verificar a posição dos dedos e não depende de bibliotecas externas, tornando a função mais modular e reutilizável nem do main.py, permitindo que seja facilmente integrada em diferentes contextos ou projetos. ele é uma lista que armezaa numeros.

    indicadory = [lm[8].y, lm[7].y, lm[6].y, lm[5].y] 
    medioy = [lm[12].y, lm[11].y, lm[10].y, lm[9].y] 
    anelary = [lm[16].y, lm[15].y, lm[14].y, lm[13].y] 
    mindinhoy = [lm[20].y, lm[19].y, lm[18].y, lm[17].y] 
    dedaoy = [lm[4].y, lm[3].y, lm[2].y, lm[1].y] 
    dedaox = [lm[4].x, lm[3].x, lm[2].x, lm[1].x] 
    
    
    if String == "Apenas o dedo indicador está levantado":
        if (
        indicadory[0] < indicadory[2]) and (medioy[0] > medioy[2]) and (anelary[0] > anelary[2]) and (mindinhoy[0] > mindinhoy[2]) and dedaox[0] < dedaox[1]:
            return "Apenas o dedo indicador está levantado"
    elif String == "O dedo indicador e o dedo médio estão levantados":
        if (
        indicadory[0] < indicadory[2]) and (medioy[0] < medioy[2]) and (anelary[0] > anelary[2]) and (mindinhoy[0] > mindinhoy[2] and dedaox[0] < dedaox[1]):
            return "O dedo indicador e o dedo médio estão levantados"
    elif String == "O dedo indicador, o dedo médio e o dedo anelar estão levantados":
        if (
        indicadory[0] < indicadory[2]) and (medioy[0] < medioy[2]) and (anelary[0] < anelary[2]) and (mindinhoy[0] > mindinhoy[2] and dedaox[0] < dedaox[1]):
            return "O dedo indicador, o dedo médio e o dedo anelar estão levantados"
    elif String == "Todos os dedos estão levantados":
        if (
        indicadory[0] < indicadory[2]) and (medioy[0] < medioy[2]) and (anelary[0] < anelary[2]) and (mindinhoy[0] < mindinhoy[2] and dedaox[0] > dedaox[1]):
            return "Todos os dedos estão levantados"

        
        
        
        
    if (
        indicadory[0] < indicadory[2]) and (medioy[0] > medioy[2]) and (anelary[0] > anelary[2]) and (mindinhoy[0] > mindinhoy[2] and dedaox[0] < dedaox[1]):
        pyautogui.press("k")
        return "Apenas o dedo indicador está levantado"

    elif (
        indicadory[0] < indicadory[2]) and (medioy[0] < medioy[2]) and (anelary[0] > anelary[2]) and (mindinhoy[0] > mindinhoy[2] and dedaox[0] < dedaox[1]):
        pyautogui.hotkey('shift', '.')
        return "O dedo indicador e o dedo médio estão levantados"
    elif (
        indicadory[0] < indicadory[2]) and (medioy[0] < medioy[2]) and (anelary[0] < anelary[2]) and (mindinhoy[0] > mindinhoy[2] and dedaox[0] < dedaox[1]):
        pyautogui.hotkey('shift', ',')
        return "O dedo indicador, o dedo médio e o dedo anelar estão levantados"    
    elif (
        indicadory[0] < indicadory[2]) and (medioy[0] < medioy[2]) and (anelary[0] < anelary[2]) and (mindinhoy[0] < mindinhoy[2] and dedaox[0] > dedaox[1]):
        pyautogui.press('F')
        return "Todos os dedos estão levantados"

    else:
        return "Nenhum gesto reconhecido"
