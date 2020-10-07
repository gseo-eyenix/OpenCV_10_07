import cv2

rgb_image = cv2.imread('eyenix.png')

cv2.imshow('eyenix.png',rgb_image)
cv2.waitKey(0)

cv2.destroyAllWindows()


