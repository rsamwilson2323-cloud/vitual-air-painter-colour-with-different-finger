# 🎨 Virtual Air Painter

Virtual Air Painter is an AI-powered drawing application built using **Python 🐍, OpenCV 🎥, MediaPipe ✋, and NumPy 📊**.

The application allows users to draw in the air using hand gestures captured by a webcam. Different finger counts automatically switch drawing colors, while a closed fist saves the artwork and clears the canvas for a new drawing.

Perfect for computer vision learning, gesture recognition projects, digital art, and touchless interaction systems.

---

# ✨ Features

✋ Hand Gesture Recognition

* Real-time hand tracking using MediaPipe

🎨 Air Drawing

* Draw in the air using your index finger

🌈 Multi-Color Drawing

* 2 Fingers → White
* 3 Fingers → Red
* 4 Fingers → Blue
* 5 Fingers → Green

📷 Live Webcam Tracking

* Uses webcam for gesture detection

💾 Auto Save Artwork

* Closed palm automatically saves the drawing

🗑 Auto Canvas Clear

* Clears canvas after saving

🖥 Fullscreen Drawing Mode

* Immersive drawing experience

⚡ Real-Time Processing

* Smooth and responsive drawing

---

# 📂 Project Structure

```text id="b2m8k4"
vitual-air-painter-colour-with-different-finger/
│
├── Virtual Air Painter.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash id="w6j4r9"
git clone https://github.com/rsamwilson2323-cloud/vitual-air-painter-colour-with-different-finger.git

cd vitual-air-painter-colour-with-different-finger
```

---

## 2️⃣ Install Dependencies

```bash id="q8p2x7"
pip install -r requirements.txt
```

Or install manually:

```bash id="d4h9n1"
pip install opencv-python mediapipe numpy
```

---

# 📦 Requirements

```text id="x5m3c8"
opencv-python
mediapipe
numpy
```

---

# ▶️ Usage

Run the application:

```bash id="j7n4k2"
python "Virtual Air Painter.py"
```

The webcam will start automatically.

To exit:

```text id="y9v6r3"
Press ENTER
```

---

# 🎮 Gesture Controls

| Fingers Raised          | Action                   |
| ----------------------- | ------------------------ |
| 1 Finger                | Cursor Only / No Drawing |
| 2 Fingers               | Draw White               |
| 3 Fingers               | Draw Red                 |
| 4 Fingers               | Draw Blue                |
| 5 Fingers               | Draw Green               |
| 0 Fingers (Closed Palm) | Save & Clear Canvas      |

---

# 🧠 How It Works

✋ Hand Detection

* Uses MediaPipe Hands to detect landmarks

🔢 Finger Counting

* Counts raised fingers in real time

🎨 Color Selection

* Automatically selects drawing color based on finger count

🖌 Drawing Engine

* Tracks index finger movement and draws on a virtual canvas

💾 Save Function

* Closed palm gesture saves artwork as BMP image

🗑 Canvas Reset

* Automatically clears the canvas after saving

---

# 📸 Example Workflow

```text id="g8t2w6"
Raise 2 Fingers → Draw White

Raise 3 Fingers → Draw Red

Raise 4 Fingers → Draw Blue

Raise 5 Fingers → Draw Green

Close Palm → Save Artwork
```

---

# 🚀 Future Improvements

🌈 Custom Color Picker

📏 Adjustable Brush Size

🖼 Image Import Support

🧠 AI Shape Recognition

✍ Handwriting Recognition

☁ Cloud Artwork Storage

📱 Mobile Version

---

# 🎯 Learning Concepts

* Computer Vision
* Hand Tracking
* Gesture Recognition
* OpenCV
* MediaPipe
* Digital Drawing Systems
* Human-Computer Interaction

---

# ⚠️ Disclaimer

This project is intended for educational, creative, and research purposes only.

Performance may vary depending on lighting conditions and camera quality.

---

# 👨‍💻 Author

**R. Sam Wilson**

🌐 GitHub

https://github.com/rsamwilson2323-cloud

💼 LinkedIn

https://www.linkedin.com/in/sam-wilson-14b554385

---

# 📜 License

This project is licensed under the MIT License.
