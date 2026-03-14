from deepface import DeepFace

# Use the correct filename
img_path = "D:\\intern\\backend\\test.jpeg"

# Analyze the face in the image
try:
    result = DeepFace.analyze(img_path, actions=['age', 'gender', 'race', 'emotion'])
    print("Analysis Result:")
    print(result)
except Exception as e:
    print("Error:", e)
