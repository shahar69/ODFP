function detectObjects() {
    fetch('/detect_objects')
        .then(response => response.json())
        .then(data => {
            console.log(data.message);
            const objectStatus = document.getElementById('objectStatus');
            objectStatus.innerText = data.message;

            if (data.capture) {
                const capturedImage = document.getElementById('capturedImage');
                capturedImage.src = data.capture;
                capturedImage.style.display = 'block';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            const objectStatus = document.getElementById('objectStatus');
            objectStatus.innerText = 'Error occurred during object detection.';
        });
}
