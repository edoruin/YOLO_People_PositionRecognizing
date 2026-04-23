
<div align="center">
    <h1>YOLO People Position Recognition</h1>
</div>

<div align="center">
<p> Use YOLO and OpenCV to recognize the position of people within a camera's field of view.
</p>
</div>

![Python](https://img.shields.io/badge/Python-3.13.3-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![OpenCV](https://img.shields.io/badge/OpenCV-4.11.0.86-5C3EE8?style=for-the-badge&logo=opencv) ![Ultralytics](https://img.shields.io/badge/Ultralytics-8.3.152-FF6347?style=for-the-badge) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

### [Link to Original README](README.md)

---

<h3>Setup</h3>
Before running the code, ensure that you have installed the required libraries. The setup is simple and requires minimal configuration.

<h3>Explanation</h3>
<p>The project consists of a single file: `Recognize.py`. The Ultralytics library will automatically download the YOLO model if it is not found when you run the script.

The logic is straightforward: the script defines two boundaries on the left and right sides of the frame. It then applies a conditional check: if a detected person (labeled "person" in the general YOLO model) crosses either boundary, they are identified as being on the "LEFT" or "RIGHT". If they are between the boundaries, they are identified as being in the "CENTER".

First, we extract the "person" class ID from the Ultralytics YOLO model:
```python
# Extracting the person class ID from the model
person_class_id = None
for class_id, class_name in model.names.items():
    if class_name.lower() == "person":
        person_class_id = class_id
        break
```

We calculate the center point of the bounding box for the detected person. A point is drawn at this center, which is then used to determine if the person has crossed the boundary lines (left or right).

> [!NOTE]
> You can close the OpenCV window by pressing the "q" key. You can change this behavior on line 83 in the `waitKey` function.

```python
if first_center_x is not None:
                if first_center_x < left_boundary:
                    print("Person in left")
                    cv2.putText(frame, "LEFT", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    Posicion_Persona = 'person in left'

                elif first_center_x > right_boundary:
                    print("Person in right")
                    cv2.putText(frame, "RIGHT", (width - 200, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    Posicion_Persona = 'person in right'

                else:
                    cv2.putText(frame, "CENTER", (width // 2 - 50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    Posicion_Persona = 'person in center'
```

The rest of the code handles OpenCV frame recording and drawing the bounding boxes. This project is intended for use in security cameras, robotics, or any system requiring human presence detection.
