import cv2
path = "C:\\Users\\User\\Downloads\\6053381.jpg"
img1 = cv2.imread(path)
print(img1.shape)
height,width = 600,600
imgResize1 = cv2.resize(img1,(height,width))
print(imgResize1.shape)
#cv2.imshow("0ld",img1)
cv2.imshow("new",imgResize1)
cv2.waitKey(0)