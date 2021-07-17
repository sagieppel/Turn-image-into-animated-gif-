# Turn image to animated gif using 3 animation modes: "explode"  "melt" "diffuse"

import PIL.Image as Image
import numpy as np

#------------------input parameterss---------------------------------------------------------------
InputImage="Input.jpg" # Input image patg
OutputGifName="Out.gif" # Output gif file path
Mode="melt" #"explode"  #Animation Modes: "explode"  "melt" "diffuse"

NumFrames=40 # Number of frames for animation
duration=80  # Frame duration in millisecond

Reverse  = False # Reverse frames order True/False
Palladrum = False  # Palladrum frames order True/False

#---------------Read image-------------------------------------------------------------------
pic=Image.open(InputImage)
im=np.array(pic.getdata()).reshape(pic.size[1], pic.size[0], 3)
im=im.astype(np.uint8)
h,w,d=im.shape
print(h,w)
cx=w/2
cy=h/2

#------------------------------diffuse-----------------------------------------------------------------
def diffuse():
    ImArray=[]
    for i in range(NumFrames):
        print("Frame ", i, "out of ", NumFrames)
        for i in range(1000):
            x = np.random.randint(w)
            y = np.random.randint(h)
            for jj in range(30):
                dx = np.random.randint(-4,4)
                dy = np.random.randint(-4,4)
                if x < cx: dx *= -1
                if y < cy: dy *= -1

                x1 = x + dx
                y1 = y + dy

                if not (x1>=w or x1<0 or y1>=h or y1<0):
                               im[y1,x1]=im[y,x]
        ImArray.append(Image.fromarray(im))
    if Reverse: ImArray = ImArray[::-1]  # Inverse frames order
    if Palladrum: ImArray = ImArray+ImArray[::-1]  # Palladrum frames order
    ImArray[0].save(OutputGifName, save_all=True, append_images=ImArray[1:] , duration=duration, loop=10000)


#--------------------------explode--------------------------------------------------------------------------
def explode():
    ImArray = []
    for i in range(NumFrames):
        print("Frame ", i, "out of ", NumFrames)
        for i in range(1000):
          x = np.random.randint(w)
          y = np.random.randint(h)
          for iii in range(30):
            r= np.random.randint(10)
            dx = x-cx
            dy = y-cy
            dc = (dy**2+dx**2)**0.5
            dx /= dc+0.001
            dy /= dc+0.001

            dx*=r
            dy*=r
            if np.random.rand()<0.5:
                dx+=np.random.randint(3)-1
            if np.random.rand() < 0.5:
                dy += np.random.randint(3) - 1

            x1 = x + int(dx)
            y1 = y + int(dy)

            if (x1 >= w or x1 < 0 or y1 >= h or y1 < 0): break
            im[y1, x1] = im[y, x]

        ImArray.append(Image.fromarray(im))
    if Reverse: ImArray=ImArray[::-1] # Inverse frames order
    if Palladrum: ImArray = ImArray + ImArray[::-1]  # Palladrum frames order
    ImArray[0].save(OutputGifName, save_all=True, append_images=ImArray[1:] , duration=duration, loop=10000)
#-----------------------------melt--------------------------------------------------------------------------------------

def melt():
    ImArray = []
    for i in range(NumFrames):
        print("Frame ", i, "out of ", NumFrames)
        for i in range(1000):
          x = np.random.randint(w)
          y = np.random.randint(h)
          for iii in range(30):

            dy = np.random.randint(6)
            dx=np.random.randint(-3,3)
            x1 = x + int(dx)
            y1 = y + int(dy)
            if (x1 >= w or x1 < 0 or y1 >= h or y1 < 0): break
            im[y1, x1] = im[y, x]
        ImArray.append(Image.fromarray(im))
    if Reverse: ImArray = ImArray[::-1]  # Inverse frames order
    if Palladrum: ImArray = ImArray + ImArray[::-1]  # Palladrum frames order
    ImArray[0].save(OutputGifName, save_all=True, append_images=ImArray[1:] , duration=duration, loop=10000)
#----------------------Main----------------------------------------------------------------
print("mode")
if Mode=="explode": explode()
if Mode=="melt": melt()
if Mode=="diffuse": diffuse()