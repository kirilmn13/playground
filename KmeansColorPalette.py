# %%
import os
from PIL import Image
import matplotlib.pyplot as plt
import cv2
from sklearn.cluster import KMeans
from collections import Counter
# %%

img = Image.open("img/1.jpg")  #Objeto PIL
imgcv = cv2.imread("img/1.jpg")  #numpy array BGR
imgcv = cv2.cvtColor(imgcv,cv2.COLOR_BGR2RGB) #cambiar BGR RGB
imagelist = imgcv.reshape((imgcv.shape[0]*imgcv.shape[1],3))
print(imagelist.shape)

# %%
def mrgb2hex(img):
    hex= "{:02x}{:02x}{:02x}".format(int(img[0]),int(img[1]),int(img[2]))
    return hex

print(mrgb2hex([255,0,0]))
# %%
clt = KMeans(n_clusters=4)
labels = clt.fit_predict(imagelist)
labelcount= Counter(labels)
print(labelcount)
totalcount = Counter(labelcount.values())
centercolors= list(clt.cluster_centers_) 
print(centercolors)
orderedcolors = [centercolors[i]/255 for i  in labelcount.keys()]
print(labelcount.values())
colorlabels = [mrgb2hex(orderedcolors[i]*255) for i in labelcount.keys()]
print(colorlabels)
plt.pie(labelcount.values(), labels=colorlabels, colors=orderedcolors,startangle=90)
plt.axis("equal")
plt.show


