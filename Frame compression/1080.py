# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 18:55:50 2020

@author: vipvi
"""
#import opencv
import cv2
class Life:
    n_rows=0
    n_cols=0
    #create constructor to initialize path
    def __init__(self,r,c):
        self.path="Life.y4m"
        self.n_rows=r
        self.n_cols=c
    def GetFrame(self):
        #get frames from path
        frame = cv2.VideoCapture(self.path) 
        # intialize counter
        counter = 0
        # set boolean variable frameConvert
        frameConvert = 1
        #while condition is True
        while frameConvert: 
            #if counter is less than number of frames, iterate and read frames
            #each frame has 16 patches
            if counter<13200: #(825 frames * 16 patches = 13200 patches)
                #read frames
                frameConvert, img = frame.read() 
                #get the height, width of image
                height, width, ch = img.shape
                #divide frame into 16*16 patch
                pheight = height/self.n_rows
                pwidth = width/self.n_cols
                #create an images array to store patches
                res = []
                #iterate through all rows and columns of image
                for i in range(0,self.n_rows):
                    for j in range(0,self.n_cols):
                        #get dimensions of each patch
                        new_img = img[int(i*pheight):int((i+1)*pheight),int(j*pwidth):int((j+1)*pwidth)]
                        #append all patches together
                        res.append(new_img)
                #iterate through all rows and columns of image
                for i in range(0,self.n_rows):
                    for j in range(0,self.n_cols):
                        #write to dimension of each patch and save in folder 720 as png
                        cv2.imwrite("Frame(1080)\\frame%d.png" % counter, res[i*self.n_cols+j]) 
                        #increment counter until condition fails
                        counter += 1
            else:
                #exits if condition fails
                frameConvert = 0
l = Life(4,4)
l.GetFrame()
