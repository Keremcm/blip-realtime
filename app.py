from flask import Flask, render_template, Response, jsonify
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import cv2
import threading

# Flask uygulaması
app = Flask(__name__)

# BLIP yükle
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

# Global değişkenler
current_caption = "Açıklama bekleniyor..."
processed_frame = None
camera = cv2.VideoCapture(0)

def generate_captions():
    """Webcam görüntüsünden açıklama üretir."""
    global current_caption, processed_frame
    while True:
        if processed_frame is not None:
            image = Image.fromarray(cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB))
            inputs = processor(image, return_tensors="pt")
            out = model.generate(
                **inputs,
                max_new_tokens=20,
                do_sample=True,
                top_p=0.9,
                temperature=0.8,
                num_return_sequences=1,
            )
            current_caption = processor.decode(out[0], skip_special_tokens=True)

def webcam_stream():
    """Webcam görüntüsünü sürekli yayınlar."""
    global processed_frame
    while True:
        ret, frame = camera.read()
        if not ret:
            break
        processed_frame = frame  # İşlenecek kareyi güncelle
        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/')
def index():
    """Ana sayfa."""
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """Webcam görüntüsünü yayınlar."""
    return Response(webcam_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_caption')
def get_caption():
    """Mevcut açıklamayı döndürür."""
    return jsonify({"caption": current_caption})

if __name__ == '__main__':
    # Kare işleme thread'ini başlat
    processing_thread = threading.Thread(target=generate_captions, daemon=True)
    processing_thread.start()
    app.run(debug=True)
