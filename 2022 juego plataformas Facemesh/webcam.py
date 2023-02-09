from threading import Thread
import cv2
    
class Webcam:
    def __init__(self):
        self.stopped = False
        self.stream = None
        self.lastFrame = None

    def start(self):
        t = Thread(target=self.update, args=())
        t.daemon = True
        t.start()
        return self

    def update(self):
        if self.stream is None:
            self.stream = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        while True:
            if self.stopped:
                return
            (result, image) = self.stream.read()
            if not result:
                self.stop()
                return
            self.lastFrame = image
                
    def read(self):
        return self.lastFrame

    def stop(self):
        self.stopped = True

    def width(self):
        return self.stream.get(cv2.CAP_PROP_FRAME_WIDTH )

    def height(self):
        return self.stream.get(cv2.CAP_PROP_FRAME_HEIGHT )
    
    def ready(self):
        return self.lastFrame is not None