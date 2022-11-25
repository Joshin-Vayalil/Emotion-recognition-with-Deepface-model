#deepface model

#from image import capture
from deepface import DeepFace
import cv2
#from fer import FER

#def emot():
img = cv2.imread('D:\ER_DeepFace\Test_imgs\img15.jpg')
#plt.imshow(img[:,:,::-1])
#plt.show()


result =DeepFace.analyze(img, actions=["emotion"])
#result = FER(mtcnn=True).detect_emotions(img)

print(result)
'''
capture()

schedule.every(15).seconds.do(emot())
while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
'''