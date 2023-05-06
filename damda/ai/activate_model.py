from face_predict import face_prediction

import matplotlib.colors as colors


answer , red, green, blue = face_prediction('./best_model(cpu).pkl',r'./haarcascade_frontalface_default.xml')

r = (red/(red+green+blue))*255
g = (green/(red+green+blue))*255
b = (blue/(red+green+blue))*255
print(answer,red,green,blue)

r, g, b = r/255, g/255, b/255
rgb_color = (r, g, b)
hex_color = colors.to_hex(rgb_color)
print(hex_color)  # 출력 결과: #7cd40b 


# pip3 install torch torchvision torchaudio matplotlib konlpy
# cv2.cvtColor function does not exist 에러가 나는 이유 
# error: (-215:assertion failed) !_src.empty() >>> src가 없음
# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) >>> frame이 없다는 뜻
# frame print 찍어보니 ret, frame, gray 존재함 
# faces = faceCascade.detectMultiScale(gray,1.1,4)에 결과값이 ()으로 비어있음