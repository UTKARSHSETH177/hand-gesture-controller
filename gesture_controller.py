import cv2
import mediapipe as mp
import pyautogui
import time

def count_fingers(lst):
    cnt = 0
    thresh = (lst.landmark[0].y * 100 - lst.landmark[9].y * 100) / 2

    # Thumb
    if (lst.landmark[5].x * 100 - lst.landmark[4].x * 100) > 6:
        cnt += 1

    # Index
    if (lst.landmark[5].y * 100 - lst.landmark[8].y * 100) > thresh:
        cnt += 1

    # Middle
    if (lst.landmark[9].y * 100 - lst.landmark[12].y * 100) > thresh:
        cnt += 1

    # Ring
    if (lst.landmark[13].y * 100 - lst.landmark[16].y * 100) > thresh:
        cnt += 1

    # Pinky
    if (lst.landmark[17].y * 100 - lst.landmark[20].y * 100) > thresh:
        cnt += 1

    return cnt

def main():
    cap = cv2.VideoCapture(0)
    mp_draw = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=1)

    prev_count = -1
    start_time = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        if results.multi_hand_landmarks:
            hand_lms = results.multi_hand_landmarks[0]
            cnt = count_fingers(hand_lms)

            now = time.time()
            if cnt != prev_count:
                if start_time is None:
                    start_time = now
                elif now - start_time > 0.2:
                    if cnt == 1:
                        pyautogui.press("right")
                    elif cnt == 2:
                        pyautogui.press("left")
                    elif cnt == 3:
                        pyautogui.press("up")
                    elif cnt == 4:
                        pyautogui.press("down")
                    elif cnt == 5:
                        pyautogui.press("space")

                    prev_count = cnt
                    start_time = None

            mp_draw.draw_landmarks(frame, hand_lms, mp_hands.HAND_CONNECTIONS)

        cv2.imshow("Hand Gesture Controller", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # Esc key
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
