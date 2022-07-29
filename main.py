#Object Tracker

import cv2

class ObjectTracker:
    def __init__(self, src=0):
        #Capture the video source
        self.video_handle = cv2.VideoCapture(src)
        #Test the open status
        if not self.video_handle.isOpened():
            raise Exception('Cant Access : '+ src )

        #A frame to initialize from the video source and process too
        self.frame = None

    def on_mouse_event(self, event, x, y, flag, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print('qqq ', x, y)
        elif event == cv2.EVENT_LBUTTONUP:
            print('www ', x, y)

    def play_and_track(self):
        #Create a named window
        cv2.namedWindow('Object Tracker')

        #Register with CV2 for a callback on mouse event
        cv2.setMouseCallback('Object Tracker', self.on_mouse_event )


        #know the FPS
        fps = self.video_handle.get(cv2.CAP_PROP_FPS)
        print(fps)
        #read the first frame
        flag, self.frame = self.video_handle.read() #(boolean, ndarray)
        while flag:
            #render
            cv2.imshow('Object Tracker', self.frame)


            #delay to match the FPS
            if cv2.waitKey(int(1000//fps)) == 27: #ASCII(ESC) == 27
                break

            #next frame
            flag, self.frame = self.video_handle.read()

        #Destroy the window
        cv2.destroyWindow('Object Tracker')

    #A special method of the class
    #It gets auto invoked (by the Garbage Collector) as life of the object ends (When reference count reduces to 0 or when application ends) .
    def __del__(self):
        if self.video_handle.isOpened():
            self.video_handle.release()

ot = ObjectTracker('E:/videos/bear.mp4')
ot.play_and_track()