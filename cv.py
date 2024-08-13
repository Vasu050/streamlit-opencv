import cv2

image = cv2.imread(r'C:\Users\Vasu Jain\Desktop\web\project\myenv\project3\Nikon-D750-Image-Samples-2.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
'''cv2.imshow('MyWindow',image)
cv2.imshow('MyWindow',gray_image)'''
'''resized_image = cv2.resize(image, (1000, 800))
cv2.imshow('Resized Image', resized_image)'''
cv2.rectangle(image, (50, 50), (150, 150), (0, 0, 255), 2)
cv2.imshow('Image with Rectangle', image)
cv2.waitKey(0)
cv2.destroyAllWindows()