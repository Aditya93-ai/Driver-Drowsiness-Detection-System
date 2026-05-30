import cv2
import mediapipe as mp
import math

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Webcam
cap = cv2.VideoCapture(0)

# Eye landmarks (approximate)
LEFT_EYE_TOP = 159
LEFT_EYE_BOTTOM = 145

# Function to calculate distance
def calculate_distance(p1, p2):

    return math.sqrt(
        (p1.x - p2.x) ** 2 +
        (p1.y - p2.y) ** 2
    )

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb_frame)

    status = "AWAKE"

    if results.multi_face_landmarks:

        for face_landmarks in results.multi_face_landmarks:

            h, w, _ = frame.shape

            # Draw landmarks
            for landmark in face_landmarks.landmark:

                x = int(landmark.x * w)
                y = int(landmark.y * h)

                cv2.circle(frame, (x, y), 1, (0,255,0), -1)

            # Eye landmarks
            top = face_landmarks.landmark[LEFT_EYE_TOP]
            bottom = face_landmarks.landmark[LEFT_EYE_BOTTOM]

            # Calculate eye opening distance
            eye_distance = calculate_distance(top, bottom)

            # Detect closed eyes
            if eye_distance < 0.01:
                status = "DROWSY"

                cv2.putText(
                    frame,
                    "DROWSINESS ALERT!",
                    (50,100),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,0,255),
                    3
                )

    # Display status
    cv2.putText(
        frame,
        f"Status: {status}",
        (50,50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255,0,0),
        2
    )

    cv2.imshow("Driver Monitoring System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
