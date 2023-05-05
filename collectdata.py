import os
import cv2

cap = cv2.VideoCapture(0)
os.chdir(r"D:/Desktop/Sign Language Detection/Sign Language Detection")
directory = ("D:/Desktop/Sign Language Detection/Sign Language Detection/Image")

while True:
    _, frame = cap.read()
    
    count = {
        'a': len(os.listdir(os.path.join(directory, "D:/Desktop/Sign Language Detection/Sign Language Detection/Image/A"))),
        'b': len(os.listdir(os.path.join(directory, "D:/Desktop/Sign Language Detection/Sign Language Detection/Image/B"))),
        'c': len(os.listdir(os.path.join(directory, "D:/Desktop/Sign Language Detection/Sign Language Detection/Image/C"))),
        'd': len(os.listdir(os.path.join(directory, "D:/Desktop/Sign Language Detection/Sign Language Detection/Image/D"))),
        'e': len(os.listdir(os.path.join(directory, "D:/Desktop/Sign Language Detection/Sign Language Detection/Image/E"))),
        'f': len(os.listdir(os.path.join(directory, "D:/Desktop/Sign Language Detection/Sign Language Detection/Image/F"))),
        'g': len(os.listdir(os.path.join(directory, "D:/Desktop/Sign Language Detection/Sign Language Detection/Image/G"))),
        'h': len(os.listdir(os.path.join(directory, "D:/Desktop/Sign Language Detection/Sign Language Detection/Image/H"))),
        'i': len(os.listdir(os.path.join(directory, "D:/Desktop/Sign Language Detection/Sign Language Detection/Image/I"))),
        'j': len(os.listdir(os.path.join(directory, "D:/Desktop/Sign Language Detection/Sign Language Detection/Image/J"))),
        'k': len(os.listdir(os.path.join(directory, "D:/Desktop/Sign Language Detection/Sign Language Detection/Image/K"))),
        'l': len(os.listdir(os.path.join(directory, "D:/Desktop/Sign Language Detection/Sign Language Detection/Image/L"))),
        'm': len(os.listdir(os.path.join(directory, "D:/Desktop/Sign Language Detection/Sign Language Detection/Image/M"))),
        'n': len(os.listdir(os.path.join(directory, "D:/Desktop/Sign Language Detection/Sign Language Detection/Image/N"))),
        'o': len(os.listdir(os.path.join(directory, "D:/Desktop/Sign Language Detection/Sign Language Detection/Image/O"))),
        'p': len(os.listdir(os.path.join(directory, "D:/Desktop/Sign Language Detection/Sign Language Detection/Image/P"))),
        'q': len(os.listdir(os.path.join(directory, "D:/Desktop/Sign Language Detection/Sign Language Detection/Image/Q"))),
        'r': len(os.listdir(os.path.join(directory, "D:/Desktop/Sign Language Detection/Sign Language Detection/Image/R"))),
        's': len(os.listdir(os.path.join(directory, "D:/Desktop/Sign Language Detection/Sign Language Detection/Image/S"))),
        't': len(os.listdir(os.path.join(directory, "D:/Desktop/Sign Language Detection/Sign Language Detection/Image/T"))),
        'u': len(os.listdir(os.path.join(directory, "D:/Desktop/Sign Language Detection/Sign Language Detection/Image/U"))),
        'v': len(os.listdir(os.path.join(directory, "D:/Desktop/Sign Language Detection/Sign Language Detection/Image/V"))),
        'w': len(os.listdir(os.path.join(directory, "D:/Desktop/Sign Language Detection/Sign Language Detection/Image/W"))),
        'x': len(os.listdir(os.path.join(directory, "D:/Desktop/Sign Language Detection/Sign Language Detection/Image/X"))),
        'y': len(os.listdir(os.path.join(directory, "D:/Desktop/Sign Language Detection/Sign Language Detection/Image/Y"))),
        'z': len(os.listdir(os.path.join(directory, "D:/Desktop/Sign Language Detection/Sign Language Detection/Image/Z")))
    }
   
    row = frame.shape[1]
    col = frame.shape[0]
    cv2.rectangle(frame,(0,40),(300,400),(255,255,255),2)
    cv2.imshow("data",frame)
    cv2.imshow("ROI",frame[40:400,0:300])
    frame=frame[40:400,0:300]
    interrupt = cv2.waitKey(1)
    if interrupt & 0xFF == ord('2'):
        break
    if interrupt & 0xFF == ord('a'):
        print((count['a']))
        print(directory)
        if not cv2.imwrite(directory+'/A/'+str(count['a'])+'.png',frame):
            raise Exception("NOT able to save")
    if interrupt & 0xFF == ord('b'):
        cv2.imwrite(directory+'/B/'+str(count['b'])+'.png',frame)
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite(directory+'/C/'+str(count['c'])+'.png',frame)
    if interrupt & 0xFF == ord('d'):
        cv2.imwrite(directory+'/D/'+str(count['d'])+'.png',frame)
    if interrupt & 0xFF == ord('e'):
        cv2.imwrite(directory+'/E/'+str(count['e'])+'.png',frame)
    if interrupt & 0xFF == ord('f'):
        cv2.imwrite(directory+'/F/'+str(count['f'])+'.png',frame)
    if interrupt & 0xFF == ord('g'):
        cv2.imwrite(directory+'/G/'+str(count['g'])+'.png',frame)
    if interrupt & 0xFF == ord('h'):
        cv2.imwrite(directory+'/H/'+str(count['h'])+'.png',frame)
    if interrupt & 0xFF == ord('i'):
        cv2.imwrite(directory+'/I/'+str(count['i'])+'.png',frame)
    if interrupt & 0xFF == ord('j'):
        cv2.imwrite(directory+'/J/'+str(count['j'])+'.png',frame)
    if interrupt & 0xFF == ord('k'):
        cv2.imwrite(directory+'/K/'+str(count['k'])+'.png',frame)
    if interrupt & 0xFF == ord('l'):
        cv2.imwrite(directory+'/L/'+str(count['l'])+'.png',frame)
    if interrupt & 0xFF == ord('m'):
        cv2.imwrite(directory+'/M/'+str(count['m'])+'.png',frame)
    if interrupt & 0xFF == ord('n'):
        cv2.imwrite(directory+'/N/'+str(count['n'])+'.png',frame)
    if interrupt & 0xFF == ord('o'):
        cv2.imwrite(directory+'/O/'+str(count['o'])+'.png',frame)
    if interrupt & 0xFF == ord('p'):
        cv2.imwrite(directory+'/P/'+str(count['p'])+'.png',frame)
    if interrupt & 0xFF == ord('q'):
        cv2.imwrite(directory+'/Q/'+str(count['q'])+'.png',frame)
    if interrupt & 0xFF == ord('r'):
        cv2.imwrite(directory+'/R/'+str(count['r'])+'.png',frame)
    if interrupt & 0xFF == ord('s'):
        cv2.imwrite(directory+'/S/'+str(count['s'])+'.png',frame)
    if interrupt & 0xFF == ord('t'):
        cv2.imwrite(directory+'/T/'+str(count['t'])+'.png',frame)
    if interrupt & 0xFF == ord('u'):
        cv2.imwrite(directory+'/U/'+str(count['u'])+'.png',frame)
    if interrupt & 0xFF == ord('v'):
        cv2.imwrite(directory+'/V/'+str(count['v'])+'.png',frame)
    if interrupt & 0xFF == ord('w'):
        cv2.imwrite(directory+'/W/'+str(count['w'])+'.png',frame)
    if interrupt & 0xFF == ord('x'):
        cv2.imwrite(directory+'/X/'+str(count['x'])+'.png',frame)
    if interrupt & 0xFF == ord('y'):
        cv2.imwrite(directory+'/Y/'+str(count['y'])+'.png',frame)
    if interrupt & 0xFF == ord('z'):
        cv2.imwrite(directory+'/Z/'+str(count['z'])+'.png',frame)


cap.release()
cv2.destroyAllWindows()