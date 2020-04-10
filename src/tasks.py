import threading
import components.face_detection_eye_blink_sensor_final as task1
import subprocess

def schedule(id):
    # Task 1
    # Task 2
    thread = threading.Thread(target=task1.detect, args=(id,))

if __name__ == '__main__':
    p = subprocess.Popen([sys.executable, './main.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

