import cv2
import mediapipe as mp
import numpy as np
import time
import os

# ------------------------------
# SETUP
# ------------------------------
SAVE_DIR = "paint"
os.makedirs(SAVE_DIR, exist_ok=True)

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.5
)

# ------------------------------
# PERFECT FINGER COUNT FUNCTION
# ------------------------------
def count_fingers(lm):
    tips = [4, 8, 12, 16, 20]
    fingers = []

    # Thumb
    if lm[tips[0]].x < lm[tips[0]-1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other 4 fingers
    for id in range(1, 5):
        fingers.append(1 if lm[tips[id]].y < lm[tips[id]-2].y else 0)

    return sum(fingers)

# ------------------------------
# MAIN
# ------------------------------
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
h, w, c = frame.shape

# ----- FULL SCREEN -----
cv2.namedWindow("Painter", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Painter", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

canvas = np.zeros((h, w, 3), np.uint8)

prev_x, prev_y = None, None
palm_closed = False
last_save_time = 0

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    finger_count = 0
    draw_mode = False
    used_color = None

    if result.multi_hand_landmarks:
        handLms = result.multi_hand_landmarks[0]
        lm = handLms.landmark

        # ⭐ Finger count
        finger_count = count_fingers(lm)

        # --------------------------
        # ⭐ COLOR MODE
        # --------------------------
        if finger_count == 1:
            draw_mode = False
            used_color = None

        elif finger_count == 2:
            draw_mode = True
            used_color = (255,255,255)   # white

        elif finger_count == 3:
            draw_mode = True
            used_color = (0,0,255)       # red

        elif finger_count == 4:
            draw_mode = True
            used_color = (255,0,0)       # blue

        elif finger_count == 5:
            draw_mode = True
            used_color = (0,255,0)       # green

        else:
            draw_mode = False

        # --------------------------
        # ⭐ Index Finger Coordinates
        # --------------------------
        x = int(lm[8].x * w)
        y = int(lm[8].y * h)

        # --------------------------
        # ⭐ Palm Close = Save + Clear
        # --------------------------
        if finger_count == 0:
            if not palm_closed and time.time() - last_save_time > 1:
                filename = f"{SAVE_DIR}/paint_{int(time.time())}.bmp"
                cv2.imwrite(filename, canvas)
                print("Saved:", filename)

                # Clear screen
                canvas = np.zeros((h, w, 3), np.uint8)

                palm_closed = True
                last_save_time = time.time()
        else:
            palm_closed = False

        # --------------------------
        # ⭐ Drawing
        # --------------------------
        if draw_mode and used_color is not None:
            if prev_x is None:
                prev_x, prev_y = x, y

            cv2.line(canvas, (prev_x, prev_y), (x, y), used_color, 8)
            prev_x, prev_y = x, y
        else:
            prev_x, prev_y = None, None

        mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

    else:
        prev_x, prev_y = None, None

    # --------------------------
    # Combine Frame + Drawing
    # --------------------------
    output = cv2.addWeighted(frame, 0.6, canvas, 0.4, 0)
    cv2.putText(output, f"Fingers: {finger_count}", (10,30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    cv2.imshow("Painter", output)

    # ENTER key exits
    if cv2.waitKey(1) & 0xFF == 13:
        break

cap.release()
cv2.destroyAllWindows()
