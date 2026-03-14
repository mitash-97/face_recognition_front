import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="faceuser",
    password="1234",
    database="face_attendance"
)

cursor = db.cursor()
