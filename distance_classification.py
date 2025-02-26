import cv2

# Load the image
image = cv2.imread("Plaksha_Faculty.jpg")

# Display the image
cv2.imshow("Loaded Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
