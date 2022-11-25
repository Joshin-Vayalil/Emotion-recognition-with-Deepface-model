# importing libraries

import cv2
import schedule
#from fer import FER
from deepface import DeepFace

cam = cv2.VideoCapture(0)
cv2.namedWindow("Webcam")

img_counter = 0

def capture():
    global img_counter
    img_name = 'D:\ER_DeepFace\cap_img/opencv_img_{}.png'.format(img_counter)
    #cv2.imwrite('Path/Image.jpg', image_name)
    cv2.imwrite(img_name, frame)
    print("Image captured")


    img = cv2.imread('D:\ER_DeepFace\cap_img\opencv_img_0.png')
    # plt.imshow(img[:,:,::-1])
    # plt.show()

    result = DeepFace.analyze(img, actions=["emotion"])
    print(result)

    # Activate the below line if you want to save all the images
    # img_counter += 1


# Set up schedule before loop , we can change the duration of the photo clicked below

schedule.every(5).seconds.do(capture)


while True:
    ret, frame = cam.read()

    if not ret:
        print("failed to grab frame")
        break

    cv2.imshow("test", frame)
    schedule.run_pending()

    k = cv2.waitKey(100)  # 1/10 sec delay; no need for separate sleep

    # Escape key for exiting
    if k % 256 == 27:
        print("Exiting the app")
        break

cam.release()
cam.destroyAllWindows()