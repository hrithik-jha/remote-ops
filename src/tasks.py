import threading
import components.face_detection_eye_blink_sensor_final as task1
from multiprocessing import Process

def schedule(id):
    # Task 1
    # Task 2
    thread = Process(target=task1.detect, args=(id,))
    print("Starting thread")
    thread.start()
    
