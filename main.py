import cv2
import easyocr
import matplotlib.pyplot as plt
import torch

# Path to the image file (replace with your actual image path)
image_path = 'path/to/your/image.jpg'


# Initialize EasyOCR reader with the specified language ('en' for English)
reader = easyocr.Reader(['en'], gpu=torch.cuda.is_available())

# Read the image from the specified path
img = cv2.imread(image_path)

# Perform text detection and recognition on the image
text_ = reader.readtext(img)

# Set the threshold for text confidence scores
threshold = 0.70

# Iterate over the detected text
for t in text_:
    bbox, text, score = t

    # If the confidence score is above the threshold, draw the bounding box and text
    if score > threshold:
        # Draw a rectangle around the detected text
        cv2.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 5)
        # Put the recognized text above the bounding box
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

# Convert the image from BGR (OpenCV format) to RGB (matplotlib format)
# and display the image with detected text
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
