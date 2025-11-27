import cv2

# Carrega o classificador Haar Cascade
cascade_path = "cascades/haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

# Abre a webcam (0 = webcam padrão)
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Erro: não foi possível acessar a câmera!")
    exit()

print("Pressione 'q' para sair.")

while True:
    ret, frame = camera.read()
    if not ret:
        print("Erro ao capturar frame.")
        break

    # Converte para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta rostos
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,   # Parâmetro ajustável
        minNeighbors=5,    # Parâmetro ajustável
        minSize=(50, 50)   # Tamanho mínimo da detecção
    )

    # Desenha retângulos nos rostos
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Exibe o vídeo
    cv2.imshow("Detecção Facial - Pressione Q para sair", frame)

    # Tecla para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
