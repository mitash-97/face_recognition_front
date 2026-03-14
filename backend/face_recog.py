from deepface import DeepFace
import os

def recognize_face(img_path):
    try:
        result = DeepFace.find(
            img_path=img_path,
            db_path="faces",
            enforce_detection=False
        )

        if len(result[0]) > 0:
            identity_path = result[0]['identity'][0]
            student_id = os.path.basename(identity_path).split(".")[0]
            return student_id
        else:
            return "UNKNOWN"

    except Exception as e:
        print("Recognition error:", e)
        return "UNKNOWN"
