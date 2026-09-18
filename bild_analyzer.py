import cv2
import numpy as np

# Bild laden
image = cv2.imread("/home/bat/CODE/HSV-color-test/bild2.JPG")

if image is None:
    print("Bild nicht gefunden!")
    exit()

# ---------- Bild verkleinern ----------
scale = 0.2

height, width = image.shape[:2]

new_width = int(width * scale)
new_height = int(height * scale)

display = cv2.resize(image, (new_width, new_height))

# ---------- HSV erzeugen ----------
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# ---------- Klickfunktion ----------
def click(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:

        # Koordinaten zurückskalieren
        original_x = int(x / scale)
        original_y = int(y / scale)

        # Pixel holen
        hsv_pixel = hsv[original_y, original_x]
        bgr_pixel = image[original_y, original_x]

        h = int(hsv_pixel[0])
        s = int(hsv_pixel[1])
        v = int(hsv_pixel[2])

        print("\n-------------------")
        print(f"Position: x={original_x}, y={original_y}")
        print(f"HSV: H={h}, S={s}, V={v}")
        print(f"BGR: {bgr_pixel}")

        # Vorschaufenster mit angeklickter Farbe
        color_preview = np.zeros((200, 200, 3), dtype=np.uint8)

        color_preview[:] = bgr_pixel

        cv2.imshow("Color Preview", color_preview)

# ---------- Fenster ----------
cv2.namedWindow("Bild")

cv2.setMouseCallback("Bild", click)

# ---------- Hauptloop ----------
while True:

    cv2.imshow("Bild", display)

    key = cv2.waitKey(1)

    if key == 27:  # ESC
        break

cv2.destroyAllWindows()