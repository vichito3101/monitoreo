import cv2

# URL RTSP de la cámara Tapo
url_rtsp = 'rtsp://HarkAI:nomeacuerdo1956@192.168.18.145:554/stream1'

# Configurar el objeto VideoCapture con la URL RTSP
cap = cv2.VideoCapture(url_rtsp)

# Verificar si se pudo abrir el flujo de video
if not cap.isOpened():
    print("Error: No se pudo abrir el flujo de video")
    exit()

# Leer y mostrar el video frame por frame
while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: No se pudo recibir un frame del flujo de video")
        break

    # Redimensionar el frame para que se ajuste a la ventana de visualización
    resized_frame = cv2.resize(frame, (800, 600))  # Cambia el tamaño según sea necesario

    # Mostrar el frame
    cv2.imshow('Cámara Tapo', resized_frame)

    # Salir del bucle si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar el objeto VideoCapture y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()

