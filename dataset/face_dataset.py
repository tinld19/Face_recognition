import cv2
import os

cam = cv2.VideoCapture(0)
cam.set(0, 640)  # set video width
cam.set(0, 480)  # set video height
face_detector = cv2.CascadeClassifier(
    '../Cascades/haarcascade_frontalface_default.xml')
# For each person face id
face_id = input('\n enter user id end press <return> ==>  ')
print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0

# Parent Directory path
parent_dir = "/Users/mac/Documents/Computer Vision/CPV project/dataset/"
path = os.path.join(parent_dir, face_id)
os.mkdir(path)
os.chdir(path)
while (True):
    ret, img = cam.read()
    img = cv2.flip(img, 1)  # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        count += 1
        # Save the captured image into the datasets folder
        cv2.imwrite(str(count) + ".jpg", gray[y:y+h, x:x+w])
        cv2.imshow('image', img)
    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break
    elif count >= 30:  # Take 30 face sample and stop video
        break
# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
