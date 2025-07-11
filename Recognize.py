"""
In this code you use YOLO and OPENCV 
for 
"""
import cv2
from ultralytics import YOLO


model_path = "yolov8n.pt"
cap = cv2.VideoCapture(0) #select index 0 of camera

#ALERTS
Posicion_Persona = [] #feature for manage the person position


if not cap.isOpened():
    print("the video wasn't found")
    exit()


model = YOLO(model_path)

#extracting the person class of model features
person_class_id = None
for class_id, class_name in model.names.items():
    if class_name.lower() == "person":
        person_class_id = class_id
        break

threshold = 0.6

while True:
    ret, frame = cap.read()
     #Get the dimensions from frame for define limits
    height, width, _ = frame.shape

    left_boundary = width * 0.3
    right_boundary = width * 0.7

    if not ret:
        print("something has failed in the frame couting")
        break

    results = model(frame)[0]

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        color = (class_id*10, class_id*100, class_id*10)

        if int(class_id) == person_class_id: #filter for person
            if score > threshold:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 4)
                cv2.putText(frame, model.names[int(class_id)].upper(), (int(x1), int(y1) - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.3, color, 3, cv2.LINE_AA)
                
                #Calculate the point of central of bounding box(box rouding the person)
                center_x = int((x1 + x2) / 2)
                center_y = int((y1 + y2) / 2)

                #drawn the center point
                cv2.circle(frame, (center_x, center_y), 5, (58, 58, 240), -1) # Círculo central

                first_center_x = center_x #save the first person

            if first_center_x is not None:
                if first_center_x < left_boundary:
                    print("Person in left")
                    cv2.putText(frame, "LEFT", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    Posicion_Persona = 'persona in left'
                    
                elif first_center_x > right_boundary:
                    print("Person in right")
                    cv2.putText(frame, "RIGHT", (width - 200, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    Posicion_Persona = 'person in right'

                else:
                    cv2.putText(frame, "CENTER", (width // 2 - 50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    Posicion_Persona = 'person in center'

    cv2.imshow("frame", frame) 

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()