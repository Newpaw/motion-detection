import cv2
import datetime
import os

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def detect_motion_and_record():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    # Initialize variables for motion detection
    motion_detected = False
    recording = False
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    out = None
    frames_recorded = 0
    frames_to_record = 30 * 10  # 30 seconds at 10 FPS

    # Background subtraction method
    fgbg = cv2.createBackgroundSubtractorMOG2()

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Apply background subtraction
        fgmask = fgbg.apply(frame)

        # Find contours
        contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) < 500:
                continue
            motion_detected = True

            if not recording:
                # Start recording
                recording = True
                frames_recorded = 0
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                folder = datetime.datetime.now().strftime("%Y/%m")
                create_directory(folder)
                out = cv2.VideoWriter(f'{folder}/motion_{timestamp}.avi', cv2.VideoWriter_fourcc(*'XVID'), 10, (frame_width, frame_height))

            break
        else:
            motion_detected = False

        if recording:
            # Write the frame to the video file
            out.write(frame)
            frames_recorded += 1

            if frames_recorded >= frames_to_record:
                # Stop recording after 30 seconds
                recording = False
                out.release()

        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Break the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    if out is not None:
        out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_motion_and_record()
