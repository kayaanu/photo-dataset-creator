import cv2
import os
import time

def capture_images(throw, hand, amount):
    SHUTTER_SPEED = 0.100 #Takes photo every 100 milliseconds
    IMAGE_SIZE = 400
    
    # Create the images directory if it doesn't exist
    output = f"{throw}_{hand}"
    os.makedirs(output, exist_ok=True)
    
    # Open webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("ERR: webcam closed.")
        return
    
    # Take photos
    for i in range(amount):
        ret, frame = cap.read()
        if not ret:
            print(f"ERR: Could not read frame {i}")
            break
        
        # Get center crop of 400x400 pixels
        height, width, _ = frame.shape
        start_x = (width - IMAGE_SIZE) // 2
        start_y = (height - IMAGE_SIZE) // 2
        cropped = frame[start_y:start_y+IMAGE_SIZE, start_x:start_x+IMAGE_SIZE]
        
        # Save image
        filename = os.path.join(output, f"{throw}_{i+1:04d}.jpg")
        cv2.imwrite(filename, cropped)
        print(f"Saved {filename}")
        
        time.sleep(SHUTTER_SPEED)
    
    cap.release()
    print("COMPLETE.")

if __name__ == "__main__":
    throw = input('Throw:')
    hand = input("Hand: ")
    amount = int(input("Amount: "))
    capture_images(throw, hand, amount)
