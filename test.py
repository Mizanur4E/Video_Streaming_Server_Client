import cv2

path_to_video_file = "/home/nayan/Gulshan-02-New/Gulshan 02 New DVR-02_ch5_20221111075758_20221111180644.avi"
vid = cv2.VideoCapture(path_to_video_file)

_, frame = vid.read()

if (vid.isOpened()== False):
    print("Error opening video file")

# Read until video is completed
while (vid.isOpened()):

    # Capture frame-by-frame
    ret, frame = vid.read()
    if ret == True:
        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything done, release
# the video capture object
vid.release()

# Closes all the frames
cv2.destroyAllWindows()