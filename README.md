
# Driver Drowsiness Detection System

Real-time driver drowsiness detection using MediaPipe Face Mesh and OpenCV to prevent accidents caused by fatigue.

---

## Objective

To build a real-time system that monitors a driver's facial landmarks through a webcam and detects signs of drowsiness — such as prolonged eye closure — triggering a visual alert to prevent accidents.

---

## Problem Statement

Driver fatigue is one of the leading causes of road accidents globally. This system uses computer vision to continuously monitor the driver's eye state and raises an alert when drowsiness is detected — simulating the kind of driver monitoring systems used in modern vehicles like Tesla and Volvo.

---

## Tools Used

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| OpenCV (cv2) | Webcam access, image processing, and real-time display |
| MediaPipe | Face Mesh model for 468 facial landmark detection |

---

## How It Works

```
Webcam Feed
     ↓
Capture & Flip Frame (OpenCV)
     ↓
Convert BGR to RGB
     ↓
MediaPipe Face Mesh — detect 468 landmarks
     ↓
Extract Eye Landmarks
     ↓
Monitor Eye State (Open / Closing / Closed)
     ↓
Trigger Drowsiness Alert if eyes closed
     ↓
Display Real-time Annotated Output
```

---

## Steps

### 1. Webcam Capture
- Opens webcam using `cv2.VideoCapture(0)`
- Reads frames continuously in a loop
- Flips frame horizontally for natural mirror view

### 2. Preprocessing
- Converts BGR frame (OpenCV default) to RGB (MediaPipe requirement)
- Ensures compatibility between the two libraries

### 3. Face Mesh Processing
- MediaPipe Face Mesh detects 468 facial landmarks per frame
- `refine_landmarks=True` enables precise iris and eye landmarks
- Returns normalized (x, y, z) coordinates for each landmark

### 4. Eye Landmark Extraction
- Specific landmark indices are used to track eye positions
- Both left and right eye landmarks are monitored simultaneously
- Landmark coordinates are converted from normalized values to pixel positions

### 5. Drowsiness Detection
- Eye state is monitored across consecutive frames
- If eyes remain closed beyond a defined threshold — drowsiness alert is triggered
- Visual warning displayed on screen to alert the driver

### 6. Landmark Visualization
- 468 green landmark points drawn on the face in real time
- Provides visual confirmation that face tracking is active

---

## Key Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| static_image_mode | False | Video mode for real-time tracking |
| max_num_faces | 1 | Monitors one driver at a time |
| refine_landmarks | True | Enables precise eye and iris landmarks |
| min_detection_confidence | 0.5 | Minimum confidence to detect face |
| min_tracking_confidence | 0.5 | Minimum confidence to track landmarks |

---

## Key Insights

1. **468 landmarks for precision** — MediaPipe maps 468 precise points across the face, allowing accurate tracking of eye open/close state even under different lighting conditions
2. **Real-time processing** — system processes live webcam frames fast enough for continuous driver monitoring
3. **Mirror flip** — frame is flipped horizontally so landmark positions align naturally with the driver's actual face orientation
4. **Normalized to pixel conversion** — landmark coordinates are multiplied by frame width and height to get actual pixel positions for drawing and analysis
5. **Practical application** — this technology is the foundation of Driver Monitoring Systems (DMS) used in modern vehicles

---

## Real World Application

This project simulates the Driver Monitoring Systems found in:
- Tesla Autopilot — monitors driver attention
- Volvo — detects driver drowsiness and intervenes
- Mobileye — fleet safety monitoring systems

---

## Setup

**Create and activate virtual environment:**

# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python -m venv venv
source venv/bin/activate

## How to Run

1. Clone the repository
   git clone https://github.com/Aditya93-ai/driver-drowsiness-detection

2. Create and activate virtual environment
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # Mac/Linux

3. Install dependencies
   pip install opencv-python mediapipe

4. Run the script
   python drowsy_detection.py

5. Exit — Press Q to quit

---

## Project Structure

```
driver-drowsiness-detection/
├── drowsy_detection.py     # Main detection script
└── README.md               # Project documentation
```

---

## Future Improvements

- Add EAR (Eye Aspect Ratio) calculation for more precise drowsiness measurement
- Integrate sound alarm using pygame for audio alert
- Add yawn detection using mouth landmark distances
- Deploy on Raspberry Pi for real embedded vehicle use

---

## Author

**Aditya Subash** — BCA Graduate 2025 | Data Analytics Portfolio  
GitHub: [Aditya93-ai](https://github.com/Aditya93-ai)
