import cv2
import numpy as np

# Load the image
image = cv2.imread("court_frame.png")  # Replace with your image path
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray, 50, 150)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Sort by area and take the largest contour (assuming it's the court)
contours = sorted(contours, key=cv2.contourArea, reverse=True)

court_corners = []  # List to store detected court corners

if contours:
    largest_contour = contours[0]  # Biggest shape (court)

    # Approximate the contour to a quadrilateral
    epsilon = 0.02 * cv2.arcLength(largest_contour, True)
    approx = cv2.approxPolyDP(largest_contour, epsilon, True)

    if len(approx) == 4:  # If it has four corners, store them
        court_corners = approx.reshape(4, 2)
        print("Automatically Detected Court Coordinates:", court_corners)
    
        # Draw detected points on the image
        for point in court_corners:
            cv2.circle(image, tuple(point), 10, (0, 0, 255), -1)

# Function for manual point selection (if automatic detection fails)
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Clicked Coordinates: ({x}, {y})")
        court_corners.append([x, y])
        cv2.circle(image, (x, y), 10, (255, 0, 0), -1)
        cv2.imshow("Select Points", image)

# If detection is inaccurate, then manual selection
if len(court_corners) != 4:
    print("Click on the four corners of the court manually.")
    cv2.imshow("Select Points", image)
    cv2.setMouseCallback("Select Points", mouse_callback)
    cv2.waitKey(0)

# Display final detected court
cv2.imshow("Detected Court", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
