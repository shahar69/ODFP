import os
import cv2
import imutils
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/detect_objects')
def detect_objects():
    try:
        # Initialize the camera
        camera = cv2.VideoCapture(0)

        # Create the captures folder if it doesn't exist
        if not os.path.exists('captures'):
            os.makedirs('captures')

        # Generate a unique filename for the captured image
        capture_filename = f'captures/{str(uuid.uuid4())}.jpg'

        # Capture the image
        ret, frame = camera.read()
        if ret:
            # Save the captured image
            cv2.imwrite(capture_filename, frame)

        # Release the camera
        camera.release()

        return jsonify({'message': 'Object detection completed successfully.', 'capture': capture_filename})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
