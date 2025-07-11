
<div align="center">
    <h1>YOLO_People_PositionRecognizing</h1>
</div>

<div align="center"> 
<p> Use YOLO and Opencv for recognize people position in the camera. 
</p>
</div>


![Python](https://img.shields.io/badge/Python-3.13.3-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![OpenCV](https://img.shields.io/badge/OpenCV-4.11.0.86-5C3EE8?style=for-the-badge&logo=opencv) ![Ultralytics](https://img.shields.io/badge/Ultralytics-8.3.152-FF6347?style=for-the-badge)


<h3> SETUP</h3>
Before to use the code be sure of download the libraries 
you won't need to wait too much and this will be the uniques 
settings, is simple the code.


<h3>Explanation</h3>
<p>The code just have one file, the Recognize.py file  the ultralytics library will download the model if he isn't found when you run the code when you don't worry about it.

The logic is simple, it's just create two borders at the left and right and apply an conditional when the people(person label of general YOLO model from ultralytics) is mayor of some of the boundary borders, he is in the right or left border. If he isn't none when he is center.


in the code first we extract the "person" label from Ultralytics YOLO general model:
```
#extracting the person class of model features
person_class_id = None
for class_id, class_name in model.names.items():
    if class_name.lower() == "person":
        person_class_id = class_id
        break `
```

In the center x and y we calculate the center point of predictions of models but just in case is a person(the label) we drawn a point where is the center point of prediction, this point is used like the object that touch the boundary lines(left and right) when is mayor, minor or is normal active the next conditionals.
> [!NOTE]
> you can close the opencv window press q key. you can change it in line 83 or waitkey function.
```
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
```


The rest of code is about opencv frame recording and the squarer of round the prediction of person.
