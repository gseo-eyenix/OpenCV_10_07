import cv2

img = cv2.imread('eyenix.png')
blur = cv2.blur(img,(5,5))

cv2.imshow('Original',img)
cv2.imshow('Result',blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
