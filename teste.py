#lib
import cv2

#%%

# funcao principal de detecção 
def detectar_cone(img, print_img):

    #classificador = cv2.CascadeClassifier('cascade.xml')
    classificador = cv2.CascadeClassifier('cascade10.xml')

    imagemcinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    deteccoes = classificador.detectMultiScale(imagemcinza, scaleFactor = 1.1, minNeighbors = 4, flags=4, minSize = (50, 150))
    
    print(deteccoes)
    if len(deteccoes) > 0:
        print(f"\nFoi(Foram) detectado {len(deteccoes)} elemento(s)\n")
    
        x = deteccoes[:, 0]
        y = deteccoes[:, 1]
        l = deteccoes[:, 2]
        a = deteccoes[:, 3]
        
        #detectar o maior valor de x
        err_la = 0
        aux_i = 0
        
        for i in range(len(x)):
            if (err_la < (l[i] * a[i])):
                err_la = l[i] * a[i]
                aux_i = i
        
        err_la = x[aux_i] - len(img[0])/2
        
        if print_img:
            for(x, y,l, a) in deteccoes:
                cv2.rectangle(img, (x, y),(x + l, y + a), (0,255,0), 2)
                cv2.imshow('Detector de faces', imagem)

            cv2.waitKey(0)
            cv2.destroyAllWindows()
        
        return err_la
        

imagem = cv2.imread('cone.jpg')
#imagem = cv2.imread('pylon.jpg')
    
err = detectar_cone(imagem, print_img = False)
print(f"erro: {err}")
