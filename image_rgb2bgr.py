import cv2

rgb_img = cv2.imread("eyenix.png")
bgr_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR)

cv2.imshow("rgb_img",rgb_img)
cv2.imshow("bgr_img",bgr_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
