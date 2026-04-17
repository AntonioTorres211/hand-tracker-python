# Hand Tracking com MediaPipe 

import cv2 #biblioteca para captura de vídeo e manipulação de imagens
import mediapipe as mp
from controller import all_fingers, aumentar_volume, diminuir_volume, index_middle, index_middle_ring, onlyindex
from detector.gesture import gestos#Importa a função only_index do módulo geture localizado na pasta detector, para verificar se apenas o dedo indicador está levantado.

# Inicialização
validacao = "" 
mp_hands = mp.solutions.hands

hands = mp_hands.Hands( #Configurações para detecção de mãos, biblioteca MediaPipe
    max_num_hands=1,
    min_detection_confidence=0.7, 
    min_tracking_confidence=0.7 
)

mp_draw = mp.solutions.drawing_utils 

# Webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) 
gestos_anterior = None
while True:
    success, img = cap.read()

    if not success:
        print("Erro ao acessar câmera") 
        break

    # Converter para RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #MediaPipe trabalha com imagens no formato RGB, enquanto o OpenCV captura em BGR. Portanto, é necessário converter a imagem para o formato RGB antes de processá-la com o MediaPipe.

    # Processar imagem
    results = hands.process(img_rgb)

    # Se detectar mão
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                img,
                handLms,
                mp_hands.HAND_CONNECTIONS    
                               
            )
        hand = results.multi_hand_landmarks[0]
        lm = hand.landmark
        gesto_atual = gestos(lm)
        
        if gesto_atual != gestos_anterior:
            if gesto_atual == "onlyindex":
                onlyindex()
            elif gesto_atual == "index_middle":
                index_middle()
            elif gesto_atual == "index_middle_ring":
                index_middle_ring()
            elif gesto_atual == "all_fingers":
                all_fingers()
            elif gesto_atual == "diminuir_volume":
               diminuir_volume()
            #    wait_time = 0.3
            elif gesto_atual == "aumentar_volume":
                aumentar_volume()
            #    wait_time = 0.3
            gestos_anterior = gesto_atual

    cv2.imshow("Hand Tracker", img)

    if cv2.waitKey(1) & 0xFF == 27: #27 é o código ASCII para a tecla "Esc".
        break

cap.release()
cv2.destroyAllWindows()