# attendance_capture.py
import cv2
from deepface import DeepFace
import mysql.connector
from datetime import datetime
import os

# Connect to database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",  # <-- replace with your MySQL password
    database="smart_attendance"
)
cursor = conn.cursor()

# Webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    temp_file = "current_frame.jpg"
    cv2.imwrite(temp_file, frame)

    try:
        # Find matching faces in the database
        result = DeepFace.find(img_path=temp_file, db_path="D:\\intern\\face_db", enforce_detection=False)

        if len(result) > 0:
            student_name = os.path.basename(result[0]['identity']).split(".")[0]
            cursor.execute("SELECT student_id FROM students WHERE name=%s", (student_name,))
            student_id = cursor.fetchone()[0]

            date_today = datetime.today().date()
            time_now = datetime.now().time()

            # Check if attendance already marked
            cursor.execute("SELECT * FROM attendance WHERE student_id=%s AND date=%s", (student_id, date_today))
            if cursor.fetchone() is None:
                cursor.execute(
                    "INSERT INTO attendance (student_id, date, time, status) VALUES (%s, %s, %s, %s)",
                    (student_id, date_today, time_now, "Present")
                )
                conn.commit()
                print(f"✅ {student_name} marked present.")

    except Exception as e:
        print("No face detected or error:", e)

    cv2.imshow("Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
conn.close()
