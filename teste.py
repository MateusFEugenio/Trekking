import cv2

imagem = cv2.imread('pylon.jpg')
classificador = cv2.CascadeClassifier('cascade.xml')

deteccoes = classificador.detecMultiScale(imagemcinza, scaleFactor=1.09,minNeighbors=5,
minSize=(30,30),maxSize=(40,40))

print(deteccoes)
print(len(detccoes))

for(x, y,l, a) in deteccoes:
    cv2.rectangle(imagem, (x, y),(x + l, y + a)(0,255,0),2)

    cv2.imshow('Detector de faces', imagem)
    cv2.waitkey(0)
    cv2.destroyallwindos( )