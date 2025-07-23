import cv2
import mediapipe as mp
import os
import time

# MediaPipe Hands initialization
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)
mp_draw = mp.solutions.drawing_utils

# ADB commands for media control
ADB_PLAY_PAUSE = 'adb shell input keyevent 85'  # Play/Pause toggle
ADB_REWIND = 'adb shell input keyevent 21'      # Left arrow = rewind
ADB_FORWARD = 'adb shell input keyevent 22'     # Right arrow = forward

# Debounce setup
last_action_time = 0
debounce_seconds = 1.2

def count_extended_fingers(hand_landmarks):
    # Count how many fingers (index, middle, ring, pinky) are extended
    finger_tips = [8, 12, 16, 20]
    finger_pips = [6, 10, 14, 18]
    count = 0
    for tip, pip in zip(finger_tips, finger_pips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:
            count += 1
    return count

def send_command(cmd):
    print(f"Sending command: {cmd}")
    os.system(cmd)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)  # Mirror image for natural interaction
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)
    current_time = time.time()

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        num_fingers = count_extended_fingers(hand_landmarks)

        if (current_time - last_action_time) > debounce_seconds:
            if num_fingers == 4:  # Open palm
                send_command(ADB_PLAY_PAUSE)
                last_action_time = current_time
            elif num_fingers == 1:  # One finger extended => rewind
                send_command(ADB_REWIND)
                last_action_time = current_time
            elif num_fingers == 2:  # Two fingers extended => forward
                send_command(ADB_FORWARD)
                last_action_time = current_time

    cv2.putText(
        frame,
        "1 finger=Rewind  |  2 fingers=Forward  |  4 fingers=Play/Pause",
        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2
    )
    cv2.imshow("Gesture Control", frame)
    if cv2.waitKey(5) & 0xFF == 27:  # ESC key to exit
        break

cap.release()
cv2.destroyAllWindows()
