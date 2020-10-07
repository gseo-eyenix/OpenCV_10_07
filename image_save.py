import cv2

rgb_img = cv2.imread("eyenix.png")

cv2.imwrite("/home/gseo/opencv_HW/save_image/eyenix_color.jpg",rgb_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
