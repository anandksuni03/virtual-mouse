import cv2
import mediapipe as mp
import pyautogui
cap = cv2.VideoCapture(0) #to take video from first source
hand_detector = mp.solutions.hands.Hands()  #to detect the hands
drawing_utils = mp.solutions.drawing_utils # to draw the points
screen_width, screen_height = pyautogui.size()
index_y = 0 # to declare outside the loop so we can access that anywhere in the code
middle_y = 0


while True: #for runing in a endless loop

    _,  frame = cap.read()  #to read what in cap variable
    def jls_extract_def():
        # to mirror the camera on y axis 1=yaxis and 0=xaxis
        return 


    frame = cv2.flip(frame, 1)# to mirror the camera on y axis 1=yaxis and 0=xaxis = jls_extract_def()
    frame_height, frame_width, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    output = hand_detector.process(rgb_frame)

    hands = output.multi_hand_landmarks



# Example usage (replace with your event trigger):


    if hands:

        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)  #for marking the land marks
            landmarks = hand.landmark

            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width) #tomark the x axis
                y = int(landmark.y*frame_height)#to mark y axis
              
                if id == 8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color =(0, 255,255)) #to mark a circle on the tip of index finger
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                    pyautogui.moveTo(index_x, index_y)
                if id == 12:
                    cv2.circle(img=frame, center=(x,y), radius=10, color =(0, 255,255)) #to mark a circle on the tip of index finger
                    middle_x = screen_width/frame_width*x
                    middle_y = screen_height/frame_height*y
                    # pyautogui.moveTo(middle_x, middle_y)
                
                if id == 4:
                    cv2.circle(img=frame, center=(x,y), radius=10, color =(0, 255,255)) #to mark a circle on the tip of index finger
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y #to adjust the frame to full size
                    
                    if abs(index_y - thumb_y) < 80:
                        pyautogui.click()
                        pyautogui.sleep(1)
                    if abs(middle_y - thumb_y) < 45:
                        pyautogui.click(button='right')
                        pyautogui.sleep(1)
                        
                  


    cv2.imshow('virtual Mouse', frame)   

    if cv2.waitKey(10) == ord("q"): # when a is pressed the camera wiull turn off

        break
      
