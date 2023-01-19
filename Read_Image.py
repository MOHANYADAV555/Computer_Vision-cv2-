import cv2
# checking  cv2 package working or not
print("Package Imported")

img = cv2.imread("C:\\Users\\User\\Downloads\\6053381.jpg")
print("The Great Business Man")

cv2.imshow("output",img)

cv2.waitKey(0)