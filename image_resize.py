import cv2

img = cv2.imread("eyenix.png")
print("img.shape = {0}".format(img.shape))

resize_img = cv2.resize(img,(300,300))
print("resize_img.shape = {0}".format(resize_img.shape))

cv2.imshow("img",img)
cv2.imshow("resize img",resize_img)
cv2.waitKey()

cv2.destroyAllWindows()
