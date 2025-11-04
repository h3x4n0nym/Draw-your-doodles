import cv2
import numpy as np
import pyautogui
import time

# გარკვეული დრო გიწევთ მოიცადოთ სანამ ხატვა დაიწყება
print("ჩაირთვება 5 წამში, გთხოვთ გახსნა სახატავი ფანჯარა(ემულატორი)")
time.sleep(5)

# ფოტოს ჩატვირთვა
img = cv2.imread("sample.jpg")
if img is None:
    raise FileNotFoundError("რესურსი არ მოიძებნა!")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# შეგიძლიათ შეცვალოთ ზომა სიჩქარის რეგულირებისთვის
max_dim = 700
h, w = gray.shape
scale = max_dim / max(h, w)
gray = cv2.resize(gray, (int(w * scale), int(h * scale)))

# კუთხეების აღმოჩენა
edges = cv2.Canny(gray, 100, 200)

# ერთიანი ფორმების აღსაქმელად
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# ეკრანის პოზიციონირება
screen_w, screen_h = pyautogui.size()
start_x = screen_w // 4
start_y = screen_h // 4

print(f"Drawing {len(contours)} contours...")

# ყველა კონტურის სახატავად
for contour in contours:
    if len(contour) < 5:
        continue  # ძალიან პატარა კონტურების გამოტოვება

    # საწყის პოზიციაზე გადასვლა
    x, y = contour[0][0]
    pyautogui.moveTo(start_x + x, start_y + y)
    pyautogui.mouseDown()

    # კონტურების ხაზების სახატავად
    for i, point in enumerate(contour):
        if i % 3 != 0:
            continue  # გარკვეული ნაწილის გამოტოვება სიჩქარისთის
        x, y = point[0]
        pyautogui.moveTo(start_x + x, start_y + y)

    pyautogui.mouseUp()
    time.sleep(0.01)  # დილეისთვის კონტურებზე გადასვლისას

print("✅ ხატვა დასრულებულია!")
