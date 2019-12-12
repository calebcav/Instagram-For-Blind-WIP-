from imageai.Detection import ObjectDetection
import os

def listOfObjects(nameOfFile):
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

    execution_path = os.getcwd()

    obj_detector = ObjectDetection()
    obj_detector.setModelTypeAsRetinaNet()
    obj_detector.setModelPath(os.path.join(execution_path, "resnet50_coco_best_v2.0.1.h5"))
    obj_detector.loadModel()
    detections = obj_detector.detectObjectsFromImage(input_image=os.path.join(execution_path, f"{nameOfFile}.jpg"), output_image_path=f"{nameOfFile}2.jpg")

    lst = []
    
    for obj in detections:
        if obj["percentage_probability"] > 50:
            lst.append((obj["name"], obj["percentage_probability"]))
    
    lst.sort(key = lambda x: float(x[1]), reverse = True)

    return lst

