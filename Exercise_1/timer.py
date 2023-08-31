# importing cv2 module
import cv2

# read the image
img = cv2.imread("f.png")

# showing the images
cv2.imshow('P', img)
cv2.imshow('Q', img)

print(img.shape)

# Destroying the window named P before
# calling the waitKey() function
cv2.destroyWindow('Q')

# using the wait key function to delay the
# closing of windows till any key is pressed
cv2.waitKey(0)
