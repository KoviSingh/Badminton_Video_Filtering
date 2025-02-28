import cv2
import numpy as np

# Load video
video_path = "sample_video.mp4"
cap = cv2.VideoCapture(video_path)

# Get video properties
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Define output video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for output video
out = cv2.VideoWriter("masked_flipped_output.mp4", fourcc, fps, (frame_width, frame_height))

# Define polygon coordinates (court area)
pts = np.array([[750, 575], [1200, 575], [1654, 963], [269, 961]], np.int32)
pts = pts.reshape((-1, 1, 2))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  

    flipped_frame = cv2.flip(frame, -1) 

    # Create a black mask
    mask = np.zeros(flipped_frame.shape[:2], dtype=np.uint8)

    # Fill the polygon with white
    cv2.fillPoly(mask, [pts], 255)

    # Apply mask (keep only inside the polygon)
    result = cv2.bitwise_and(flipped_frame, flipped_frame, mask=mask)

    # Write the processed frame to output video
    out.write(result)

    # Display the masked frame (optional)
    cv2.imshow("Masked & Flipped Video", result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()
