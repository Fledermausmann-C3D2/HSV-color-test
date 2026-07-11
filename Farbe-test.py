import numpy as np
import cv2

# HSV-Farbe
hsv_color = np.uint8([[[5, 120, 120]]])

# HSV → BGR
bgr_color = cv2.cvtColor(hsv_color, cv2.COLOR_HSV2BGR)

# Bild erzeugen
image = np.full((200, 200, 3), bgr_color[0][0], dtype=np.uint8)

# Anzeigen
cv2.imshow("Color", image)

# Warten bis Taste gedrückt wird
cv2.waitKey(0)

# Fenster schließen
cv2.destroyAllWindows()