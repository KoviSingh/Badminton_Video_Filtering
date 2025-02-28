# Badminton_Video_Filtering
# **Badminton Court Detection Using Computer Vision**

## **Overview**
This project detects a badminton court from an image or video using **OpenCV** and **contour detection**. It provides both **automatic detection** and **manual selection** for better accuracy.

## **Features**
- **Automatic Detection**: Identifies the court using contour approximation.
- **Manual Selection**: Allows users to click on the four court corners if automatic detection fails.
- **Video Processing**: Masks and processes court area from video frames.
- **Flipping & Masking**: Supports flipping video and masking only the court region.

## **Technologies Used**
- **Python 3.x**
- **OpenCV** (`cv2`)
- **NumPy**

## **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/badminton-court-detection.git
   cd badminton-court-detection
   ```
2. Install dependencies:
   ```bash
   pip install opencv-python numpy
   ```

## **Usage**
### **1. Detect Court from Image**
Run the script to detect the court from an image:
```bash
python detect_court.py
```

### **2. Process Badminton Court in a Video**
Run the script to apply masking and flipping:
```bash
python process_video.py
```

## **Project Workflow**
1. **Preprocessing**: Convert image to grayscale, apply edge detection.
2. **Contour Detection**: Extracts largest quadrilateral as the court.
3. **Manual Selection (if needed)**: Allows clicking on court corners.
4. **Video Processing**: Masks court area and processes each frame.

## **Example Output**
### **Image Court Detection**
![Court Detection](https://your-image-link.com)

### **Video Court Processing**
![Video Output](https://your-video-link.com)

## **Limitations**
- Detection accuracy depends on **lighting** and **camera angle**.
- May fail for **blurred or low-contrast courts**.
- Manual selection is required if **court lines are not clear**.
- **Automatic Selection not working currently**


---
**Author:** Kovidh Singh

