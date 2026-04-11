import pyautogui #biblioteca para automação de tarefas, utilizada para simular ações do teclado e mouse, permitindo que o programa controle o computador com base nos gestos reconhecidos pela função gestos.
import time #biblioteca para manipulação de tempo, utilizada para adicionar atrasos entre as ações simuladas pelo pyautogui, garantindo que as ações sejam executadas de forma mais natural e evitando sobrecarga do sistema.


def onlyindex():
    pyautogui.press("k")

def index_middle():
    pyautogui.hotkey('shift', '.')

def index_middle_ring():
    pyautogui.hotkey('shift', ',')

def all_fingers():
    pyautogui.press('f')

    