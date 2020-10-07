import cv2

rgb_img = cv2.imread("eyenix.png")
gray_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2GRAY)

cv2.imshow("rgb_img",rgb_img)
cv2.imshow("gray_img",gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
