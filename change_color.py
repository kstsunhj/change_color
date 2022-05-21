from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import os

from sympy import im
project_dir = os.path.dirname(os.path.abspath(__file__))
input = os.path.join(project_dir,'train_c')
output = os.path.join(project_dir,'train_c')
origin_color = [[60,180,90],[110,40,40],[50,10,70],[180,200,60],[100,100,100]]#annotated color
next_color=[[7,7,7],[8,8,8],[11,11,11],[12,12,12],[13,13,13]]#change color
def modify():
    os.chdir(input)
    for image in os.listdir(os.getcwd()):
        #print(os.path.join(input,image))
        #img = Image.open(os.path.join(input,image))
        image = image.split('.')
        if(image[0][-5:] == 'pix_b'):
            #print(os.path.join(input,image[0] + '.' + image[1]))
            img = Image.open(os.path.join(input,image[0] + '.' + image[1]))
            arr = np.array(img)
            for i in arr:
                for j in i:
                    for k in range(5):
                        if j[0] == origin_color[k][0] and j[1] == origin_color[k][1] and j[2] == origin_color[k][2]:
                            j[0] = next_color[k][0]
                            j[1] = next_color[k][1]
                            j[2] = next_color[k][2]
            for i in arr:
                for j in i:
                    if j[0] > 13 or j[1] > 13 or j[2] > 13:
                        j[0] = 0
                        j[1] = 0
                        j[2] = 0
            plt.imsave(os.path.join(output,image[0] + '.' + image[1]),arr)
                        
modify()
