from flask import Flask, render_template, Response, request
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed', methods=['GET'])
def video_feed():
    username = request.args.get('username')
    password = request.args.get('password')
    ip_address = request.args.get('ip_address')

    if username is None or password is None or ip_address is None:
        return "Error: Por favor, proporciona el nombre de usuario, la contraseña y la dirección IP."

    url_rtsp = f'rtsp://{username}:{password}@{ip_address}/stream1'
    
    cap = cv2.VideoCapture(url_rtsp)

    if not cap.isOpened():
        return "Error: No se pudo abrir el flujo de video"

    def generate_frames():
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            else:
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        cap.release()  # Liberar recursos al finalizar

    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)



