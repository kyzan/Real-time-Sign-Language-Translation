from PIL import Image, ImageTk
import tkinter as tk
import cv2
import os
import numpy as np
from keras.models import model_from_json
import operator
import time
import pyttsx3
import sys, os
import matplotlib.pyplot as plt
import hunspell
from activeScreen import makeScreen

KEY = None

class Application:
    def GUI(self):
        self.root = tk.Tk()

    def setGUI(self):
        self.root.configure(background="papaya whip")
        self.root.title("Real Time Sign Language Translation")
        self.root.protocol('WM_DELETE_WINDOW', self.destructor)
        self.root.geometry("900x1100")

    def makeElements(self):
        self.panel = tk.Label(self.root)
        self.panel2 = tk.Label(self.root) 
        self.T = tk.Label(self.root)
        self.T.config(text = "Real Time Sign Language Translation",font=("helvetica",36,"bold"), background="papaya whip")
        self.panel3 = tk.Label(self.root) 
        self.T1 = tk.Label(self.root)
        self.T1.config(text="",font=("helvetica",36,"bold"),background="papaya whip")
        self.panel4 = tk.Label(self.root) 
        self.T2 = tk.Label(self.root)
        self.T2.config(text ="Text :",font=("helvetica",36,"bold"),background="papaya whip")
        self.panel5 = tk.Label(self.root)
        self.T3 = tk.Label(self.root)
        self.T3.config(text ="",font=("helvetica",36,"bold"),background="papaya whip")
        self.T4 = tk.Label(self.root)
        self.T4.config(text = "Auto Fill",font = ("helvetica",36,"bold"),background="papaya whip") 
    
    def placeElements(self):
        
        self.panel.place(x = 135, y = 10, width = 640, height = 640)
        
        self.panel2.place(x = 460, y = 95, width = 310, height = 310)
        
        self.T.place(x=31,y = 17)
                 
        self.panel3.place(x = 500,y=640)
        
        self.T1.place(x = 10,y = 640)
                 
        self.panel4.place(x = 220,y=700)
        
        self.T2.place(x = 20,y = 700)
                 
        self.panel5.place(x = 350,y=760)
        
        self.T3.place(x = 10,y = 760)
                
        self.T4.place(x = 250,y = 820)
        

    def load_model(self, ext):
        json_file = open(self.directory+"/model-bw"+ext+".json", "r")
        model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(model_json)
        loaded_model.load_weights(self.directory+"/model-bw"+ext+".h5")
        return json_file, model_json, loaded_model

    def __init__(self):
        self.directory = 'model_final'

        self.current_image = KEY
        self.current_image2 = KEY
        
        
        self.json_file, self.model_json, self.loaded_model = self.load_model("")
        self.json_file_dru, self.model_json_dru, self.loaded_model_dru = self.load_model("_dru")
        self.json_file_tkdi, self.model_json_tkdi, self.loaded_model_tkdi = self.load_model("_tkdi")
        self.json_file_smn, self.model_json_smn, self.loaded_model_smn = self.load_model("_smn")
        
        self.hs = hunspell.HunSpell('/usr/share/hunspell/en_US.dic', '/usr/share/hunspell/en_US.aff')
        self.vs = cv2.VideoCapture(0)
        
        self.ct = {}
        self.ct['blank'] = 0
        self.blank_flag = 0
        for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
          self.ct[i] = 0

        self.GUI()
        self.setGUI()
        self.makeElements()
        self.placeElements()


        arr =[1, 2, 3, 'speak']
        for i in arr:
            self.Buttons(i)

        self.inp=""
        self.str=""
        self.word=""
        self.current_symbol=None
        self.photo=None
        self.video_loop()

    def Buttons(self,i):
        if i==1:
            self.bt1=tk.Button(self.root, command=self.action1,height = 0,width = 0)
            self.bt1.place(x = 26,y=890)
        elif i==2:
            self.bt2=tk.Button(self.root, command=self.action2,height = 0,width = 0)
            self.bt2.place(x = 325,y=890)
        elif i==3:
            self.bt3=tk.Button(self.root, command=self.action3,height = 0,width = 0)
            self.bt3.place(x = 625,y=890)
        elif i=='speak':
            self.bt6 =tk.Button(self.root, command=self.speak, text="Speak", height=10, width=10,background="papaya whip")
            self.bt6.place(x=20, y=100)

    def video_loop(self):
        
        ok, frame = self.vs.read()
        if ok:
            cv2image = cv2.flip(frame, 1)
            x1 = int(0.5*frame.shape[1])
            y1 = 10
            x2 = frame.shape[1]-10
            y2 = int(0.5*frame.shape[1])
            cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
            cv2image = cv2.cvtColor(cv2image, cv2.COLOR_BGR2RGBA)
            self.current_image = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=self.current_image)
            self.panel.imgtk = imgtk
            self.panel.config(image=imgtk, background="papaya whip")
            cv2image = cv2image[y1:y2, x1:x2]
            res = makeScreen(cv2image)
            self.predict(res)
            self.current_image2 = Image.fromarray(res)
            imgtk = ImageTk.PhotoImage(image=self.current_image2)
            self.panel2.imgtk = imgtk
            self.panel2.config(image=imgtk)
            self.panel3.config(text=self.current_symbol,font=("helvetica",45))
            self.panel4.config(text=self.word,font=("helvetica",45))
            self.panel5.config(text=self.str,font=("helvetica",45))
            predicts=self.hs.suggest(self.word)
            if(len(predicts) > 0):
                self.bt1.config(text=predicts[0],font = ("helvetica",18))
            else:
                self.bt1.config(text="")
            if(len(predicts) > 1):
                self.bt2.config(text=predicts[1],font = ("helvetica",19))
            else:
                self.bt2.config(text="")
            if(len(predicts) > 2):
                self.bt3.config(text=predicts[2],font = ("helvetica",18))
            else:
                self.bt3.config(text="")
              
        self.root.after(30, self.video_loop)
    
    def DRU(self,K):
        result_dru = self.loaded_model_dru.predict(K)
        prediction = {}
        prediction['D'] = result_dru[0][0]
        prediction['R'] = result_dru[0][1]
        prediction['U'] = result_dru[0][2]
        prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
        self.current_symbol = prediction[0][0]
    def TKDI(self, K):
        result_tkdi = self.loaded_model_tkdi.predict(K)
        prediction = {}
        prediction['D'] = result_tkdi[0][0]
        prediction['I'] = result_tkdi[0][1]
        prediction['K'] = result_tkdi[0][2]
        prediction['T'] = result_tkdi[0][3]
        prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
        self.current_symbol = prediction[0][0]
    def SMN(self, K):
        result_smn = self.loaded_model_smn.predict(K)
        prediction = {}
        prediction['M'] = result_smn[0][0]
        prediction['N'] = result_smn[0][1]
        prediction['S'] = result_smn[0][2]
        prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
        self.current_symbol = prediction[0][0]
    def Layer2(self, K):
        if(self.current_symbol == 'D' or self.current_symbol == 'R' or self.current_symbol == 'U'):
            self.DRU(K)
        elif(self.current_symbol == 'K' or self.current_symbol == 'T' or self.current_symbol == 'D' or self.current_symbol == 'I'):
            self.TKDI(K)
        if(self.current_symbol == 'S' or self.current_symbol == 'M' or self.current_symbol == 'U'):
            self.SMN(K)


#made using https://docs.python.org/3/library/tkinter.html and https://youtu.be/NQPV2344cGE
    def predict(self,test_image):
        test_image = cv2.resize(test_image, (128,128))
        K = test_image.reshape(1, 128, 128, 1)
        result = self.loaded_model.predict(test_image.reshape(1, 128, 128, 1))
        prediction={}
        prediction['blank'] = result[0][0]
        inde = 1
        for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            prediction[i] = result[0][inde]
            inde += 1
        
        prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
        
        self.current_symbol = prediction[0][0]
        self.Layer2(K)

        if(self.current_symbol == 'blank'):
            for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                self.ct[i] = 0
        self.ct[self.current_symbol] += 1
        if(self.ct[self.current_symbol] > 60):
            for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                if i == self.current_symbol:
                    continue
                tmp = self.ct[self.current_symbol] - self.ct[i]
                if tmp < 0:
                    tmp *= -1
                if tmp <= 20:
                    self.ct['blank'] = 0
                    for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        self.ct[i] = 0
                    return
            self.display()

    def display(self):
        self.ct['blank'] = 0
        for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            self.ct[i] = 0
        if self.current_symbol == 'blank':
            if self.blank_flag == 0:
                self.blank_flag = 1
                if len(self.str) > 0:
                    self.str += " "
                self.str += self.word
                self.word = ""
        else:
            if(len(self.str) > 16):
                self.str = ""
            self.blank_flag = 0
            self.word += self.current_symbol

    def speak(self):
        engine = pyttsx3.init()
        engine.setProperty('rate', 81)
        engine.say(self.word)
        engine.runAndWait()
    def action1(self):
    	predicts=self.hs.suggest(self.word)
    	if(len(predicts) >= 1):
            self.word=""
            self.str+=" "
            self.str+=predicts[0]
    def action2(self):
    	predicts=self.hs.suggest(self.word)
    	if(len(predicts) >= 2):
            self.word=""
            self.str+=" "
            self.str+=predicts[1]
    def action3(self):
    	predicts=self.hs.suggest(self.word)
    	if(len(predicts) >= 3):
            self.word=""
            self.str+=" "
            self.str+=predicts[2]

    def destructor(self):
        self.root.destroy()
        self.vs.release()
        cv2.destroyAllWindows()
    
    