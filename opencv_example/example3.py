import numpy as np
import cv2

switch_case = {
    ord('a'):"a키",
    ord('b'):"b키",
    0xA1:"A키",
    int('0x42',16):"B키",
    2424832: "왼쪽",
    2490368:"윗쪽",
    2555904:"오른쪽",
    2621440:"아랫쪽"
}

image = np.ones((200,300),np.float64)
cv2.namedWindow('Keyboard Event')
cv2.imshow('Keyboard Event',image)

while True:
    key = cv2.waitKeyEx(100)
    if key == 27: break

    try:
        result = switch_case[key]
        print(result)
    except KeyError:
        result = -1

cv2.destroyAllWindows()