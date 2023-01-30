from PIL import Image
import sys
import random

def helpme():
    print("\nCommands(*optional):")
    print('help')
    print('grayscale()')
    print('invert()')
    print('contrast(ratio), r=1 normal image, r=-1 inverted')
    print('noise(amount)')
    print('pixelize(size)')
    print('edgeDetect(threshold,*pxldif)')
    print('colorEdgeDetect(threshold,*pxldif,*debug)')
    print('deepfry()')
    print("\nExample: python imageFilters.py example.jpg 'invert()' 'noise(50)'")

try:
    imagename = str(sys.argv[1])
except IndexError:
    helpme()
    quit()

if imagename == 'help':
    helpme()
    quit()

im = Image.open(imagename)
pix = im.load()
print(im.size, flush=True)

def grayscale():
    for i in range (0,im.size[0]): # j is y value
        for j in range (0,im.size[1]): # i is x value
            avg = (pix[i,j][0] + pix[i,j][1] + pix[i,j][2])/3
            avg = int(avg)
            tup2 = (avg,avg,avg,255)
            pix[i,j] = tup2
    print("Convert to Grayscale Done!", flush=True)

def edgeDetect(edgeThreshold, pixelDifference=1):
    grayscale()
    for i in range (0,im.size[0]-pixelDifference): # j is y value
        for j in range (0,im.size[1]-pixelDifference): # i is x value
            if abs(pix[i,j][0] - pix[i+pixelDifference,j][0]) > edgeThreshold or abs(pix[i,j][0] - pix[i,j+pixelDifference][0]) > edgeThreshold:
                tup2 = (0,0,0,255)
            else:
                tup2 = (255,255,255,255)
            pix[i,j] = tup2
    print("Edge Detection Done!", flush=True)

def colorEdgeDetect(edgeThreshold, pixelDifference=1, debug=0):
    for i in range (0,im.size[0]-pixelDifference): # j is y value
        for j in range (0,im.size[1]-pixelDifference): # i is x value
            tup2 = (0,0,0,255)
            if abs(pix[i,j][0] - pix[i+pixelDifference,j][0]) > edgeThreshold or abs(pix[i,j][0] - pix[i,j+pixelDifference][0]) > edgeThreshold:
                tup2 = tuple(map(lambda i, j: i + j, tup2, (255,0,0,0)))
            if abs(pix[i,j][1] - pix[i+pixelDifference,j][1]) > edgeThreshold or abs(pix[i,j][1] - pix[i,j+pixelDifference][1]) > edgeThreshold:
                tup2 = tuple(map(lambda i, j: i + j, tup2, (0,255,0,0)))
            if abs(pix[i,j][2] - pix[i+pixelDifference,j][2]) > edgeThreshold or abs(pix[i,j][2] - pix[i,j+pixelDifference][2]) > edgeThreshold:
                tup2 = tuple(map(lambda i, j: i + j, tup2, (0,0,255,0)))
            if tup2 == (0,0,0,255):
                    tup2 = (255,255,255,255)
            elif tup2 == (255,255,255,255):
                tup2 = (0,0,0,255)
            if debug != 1:
                if tup2 != (255,255,255,255):
                    tup2 = (0,0,0,255)
            pix[i,j] = tup2
    print("Colored Edge Detection Done!", flush=True)

def contrast(ratio): # 1 is normal image, 0 is flat gray, -1 is inverted
    ratio-=1
    for i in range (0,im.size[0]): # j is y value
        for j in range (0,im.size[1]): # i is x value
            contRed = int(pix[i,j][0]+((pix[i,j][0]-128)*ratio))
            contGreen = int(pix[i,j][1]+((pix[i,j][1]-128)*ratio))
            contBlue = int(pix[i,j][2]+((pix[i,j][2]-128)*ratio))
            tup2 = (contRed,contGreen,contBlue,255)
            pix[i,j] = tup2
    print("Contrast Adjustment Done!", flush=True)

def invert():
    for i in range (0,im.size[0]): # j is y value
        for j in range (0,im.size[1]): # i is x value
            tup2 = (255-pix[i,j][0],255-pix[i,j][1],255-pix[i,j][2],255)
            pix[i,j] = tup2
    print("Inversion Done!", flush=True)

def noise(amount):
    for i in range (0,im.size[0]): # j is y value
        for j in range (0,im.size[1]): # i is x value
            redVal = int(pix[i,j][0] + (random.random()*(amount*2)-amount))
            greenVal = int(pix[i,j][1] + (random.random()*(amount*2)-amount))
            blueVal = int(pix[i,j][2] + (random.random()*(amount*2)-amount))
            tup2 = (redVal,greenVal,blueVal,255)
            pix[i,j] = tup2
    print("Noise Done!",flush=True)

def pixelizeMain(pixelSize=50):
    for i in range (0,im.size[0]-(im.size[0]%pixelSize),pixelSize): # j is y value
        for j in range (0,im.size[1]-(im.size[1]%pixelSize),pixelSize): # i is x value
            redTotal = 0
            greenTotal = 0
            blueTotal = 0
            for k in range(i,i+pixelSize):
                for l in range(j,j+pixelSize):
                    redTotal+=pix[k,l][0]
                    greenTotal+=pix[k,l][1]
                    blueTotal+=pix[k,l][2]
            redAvg=int(redTotal/(pixelSize*pixelSize))
            greenAvg=int(greenTotal/(pixelSize*pixelSize))
            blueAvg=int(blueTotal/(pixelSize*pixelSize))
            for k in range(i,i+pixelSize):
                for l in range(j,j+pixelSize):
                    tup2 = (redAvg,greenAvg,blueAvg,255)
                    pix[k,l] = tup2
    im1 = im.crop((0,0,im.size[0]-(im.size[0]%pixelSize),im.size[1]-(im.size[1]%pixelSize)))
    print("Pixelization Done!",flush=True)
    return im1

def pixelize(pixelSize):
    global im
    im = pixelizeMain(pixelSize)

def deepfry():
    for i in range (0,im.size[0]): # j is y value
        for j in range (0,im.size[1]): # i is x value
            if pix[i,j][0] > pix[i,j][1] and pix[i,j][0] > pix[i,j][1]:
                tup2 = (255,0,0,255)
            elif pix[i,j][1] > pix[i,j][2] and pix[i,j][1] > pix[i,j][2]:
                tup2 = (0,255,0,255)
            elif pix[i,j][2] > pix[i,j][0] and pix[i,j][2] > pix[i,j][1]:
                tup2 = (0,0,255,255)
            else:
                tup2 = (255,255,255,255)
            pix[i,j] = tup2
    print("Deepfry Done!",flush=True)

for f in range(2,len(sys.argv)):
    funcname = sys.argv[f]
    eval(funcname)

im.save(imagename[:len(imagename)-4]+"_edit"+imagename[len(imagename)-4:])

#7680,4320 Inversion: 24.5 sec