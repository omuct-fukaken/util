import cv2

capture_datas=[]

for i in range(10):
    capture=cv2.VideoCapture(i)
    capture.read()
    if capture.isOpened():
        capture_datas.append({'num':i,'capture':capture})


while True:
    for capture_data in capture_datas:
        _,img=capture_data['capture'].read()
        cv2.imshow(str(capture_data['num']),img)
        cv2.waitKey(1)