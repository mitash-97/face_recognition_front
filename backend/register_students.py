from deepface import DeepFace
import os
import shutil

student_folder = "D:\\intern\\students"
db_folder = "D:\\intern\\face_db"

for filename in os.listdir(student_folder):
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        img_path = os.path.join(student_folder, filename)
        # Create embeddings for each student
        DeepFace.extract_faces(img_path=img_path, target_path=db_folder)
print("Student face embeddings created.")
