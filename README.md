
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
<p>The code just have two files, the Recognize.py file and the yolov8n.pt this last isn't necessary because ultralytics library download the model if he isn't found when you run the code.

The logic is simple, it's just create two borders at the left and right and apply an conditional when the people(person label of general YOLO model from ultralytics) touch the line, he is in the right, when touch the other line(left border) he is in the left, if he isn't touching none, he's in center.


in the code first we extract the "person" label from Ultralytics YOLO general model:
` 
#extracting the person class of model features
person_class_id = None
for class_id, class_name in model.names.items():
    if class_name.lower() == "person":
        person_class_id = class_id
        break `
        <\p>
