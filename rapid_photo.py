import cv2
import os
import time

def capture_images():
    
    # throws = ["paper", "rock", "scissors"]
    # hands  = ["left", "right"]
    
    # Create the images directory if it doesn't exist
    throw = "paper"
    hand = "right"
    
    output = f"{throw}_{hand}"
    os.makedirs(output, exist_ok=True)
    
    # Open webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("ERR: Could not open webcam.")
        return
    
    for i in range(50):
        ret, frame = cap.read()
        if not ret:
            print(f"ERR: Could not read frame {i}")
            break
        
        # Get center crop of 360*360 pixels
        height, width, _ = frame.shape
        start_x = (width - 360) // 2
        start_y = (height - 360) // 2
        cropped_frame = frame[start_y:start_y+360, start_x:start_x+360]
        
        # Save image
        filename = os.path.join(output, f"{throw}_{i+1:03d}.jpg")
        cv2.imwrite(filename, cropped_frame)
        print(f"Saved {filename}")
        
        time.sleep(0.25)  # Wait for 250ms
    
    cap.release()
    print("Photos complete.")

if __name__ == "__main__":
    capture_images()
