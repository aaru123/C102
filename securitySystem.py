import cv2
import dropbox
import time
import random

start_time= time.time()


#vco = video capture object

def take_snapshot ():
    no = 0
    #initialize cv2
    vco = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera is on
        ret,frame= vco.read()  
        #cv2.imwrite()   method is used to save an image to any storage device
        numStr = no + 1
        imageName ="img"+str(numStr)+".png"
        cv2.imwrite(imageName,frame)
        result= False
    return imageName
    print("snapshot taken")

    #release the camera
    vco.release()
    #close all the windows that were started in the process
    cv2.destroyAllWindows()

def upload_file(imageName):
    access_token = "sl.A-mgPXy8g9_huNhnKqXVOIGHjKIZ7A_krYSdAMZvqRKcLVvP73Bt1zHaK2cCsu6mRJqRD1cdKtulb_Wv6BBl-1sNbcfLbMdZ3tm4W6K-mVrtK2V8A7cKQtPUAneAsgRJK8_yxrU"
    file =imageName
    file_from = file
    file_to="/testFolder/"+(imageName)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)

main()



