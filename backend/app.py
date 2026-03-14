import cv2
from deepface import DeepFace
import numpy as np
import datetime

# Initialize webcam
cap = cv2.VideoCapture(0)  # 0 for default camera

if not cap.isOpened():
    print("Cannot open webcam")
    exit()

# Dictionary to track attendance
attendance = {}

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    try:
        # Convert BGR to RGB for DeepFace
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Analyze the face
        result = DeepFace.analyze(frame_rgb,
                                  actions=['age', 'gender', 'race', 'emotion'],
                                  enforce_detection=False)
        
        # DeepFace returns a list even for single face
        face_data = result[0]

        age = face_data['age']
        gender = face_data['dominant_gender']
        race = face_data['dominant_race']
        emotion = face_data['dominant_emotion']
        region = face_data['region']

        x, y, w, h = region['x'], region['y'], region['w'], region['h']

        # Draw rectangle around face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display information
        info_text = f"{gender}, {age}, {race}, {emotion}"
        cv2.putText(frame, info_text, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

        # Mark attendance (using race+gender+age as identifier for demo)
        student_id = f"{race}_{gender}_{age}"
        if student_id not in attendance:
            attendance[student_id] = datetime.datetime.now().strftime("%H:%M:%S")

    except Exception as e:
        print("Face analysis failed:", e)

    # Show the webcam feed
    cv2.imshow("Smart Classroom Attendance", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

# Print attendance
print("\n--- Attendance ---")
for student, time in attendance.items():
    print(f"{student}: Present at {time}")
