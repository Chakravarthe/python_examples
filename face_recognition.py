#import libraries
import cv2
import face_recognition

#get a reference to webcam
video_capture = cv2.VideoCapture("/dev/video1")
#initialize variables
face_locations = []
while true:
    #grab a single frame of video
    ret,frame = video_capture.read()

    #convert the image from BGR color (which openCV use) RGB color (which face_recognition uses)
    rgb_frame = frame[:,:,::-1]

    #find all the faces in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)

    #Display results
    for top,right,bottom,left in face_locations:
        #Draw a box around the face
        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)
        #Draw the resulting image
        cv2.imshow('video',frame)

        #Hit 'q' on the keyboard to quit!
        if cv2.waitkey(1) & 0*FF == ord('q'):
            break
        #Release handle to the webcam
        video_capture.release()
        cv2.destroyAllWindows()
