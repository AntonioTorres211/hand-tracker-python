# Hand Tracking com MediaPipe 

import cv2 #biblioteca para captura de vídeo e manipulação de imagens
import mediapipe as mp #biblioteca para detecção e rastreamento de mãos

# Inicialização
mp_hands = mp.solutions.hands

hands = mp_hands.Hands( #Configurações para detecção de mãos, biblioteca MediaPipe
    max_num_hands=2,
    min_detection_confidence=0.7, 
    min_tracking_confidence=0.7 
)

mp_draw = mp.solutions.drawing_utils 

# Webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) 

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

    cv2.imshow("Hand Tracker", img)

    if cv2.waitKey(1) & 0xFF == 27: #27 é o código ASCII para a tecla "Esc".
        break

cap.release()
cv2.destroyAllWindows()