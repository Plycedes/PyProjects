import cv2
import os

img = cv2.imread("HumanHead.png")

directory = r'D:\New folder'

os.chdir(directory)

print("Before saving image:")
print(os.listdir(directory))

filename = 'savedImage.png'

cv2.imwrite(filename, img)

print("After saving image:")
print(os.listdir(directory))

print("Succesfully saved")
