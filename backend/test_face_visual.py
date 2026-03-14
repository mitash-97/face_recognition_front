from deepface import DeepFace
import cv2

# Load image
img_path = "test.jpeg"
img = cv2.imread(img_path)

# Analyze face
result = DeepFace.analyze(img_path=img_path, actions=['age', 'gender', 'race', 'emotion'])
result = result[0]  # Access the first dictionary in the list

# Prepare text
text = f"Age: {result['age']}, Gender: {result['dominant_gender']}, Emotion: {result['dominant_emotion']}, Race: {result['dominant_race']}"

# Put text on image
cv2.putText(img, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

# Show image
cv2.imshow("Face Analysis", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
