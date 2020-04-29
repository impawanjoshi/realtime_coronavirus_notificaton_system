from tkinter import *
import tkinter.messagebox
from plyer import notification
import os
from bs4 import BeautifulSoup
import urllib.request
import time

global root,e1,s,imgpath,d,data


def des():
	global root,e1,states,s,data,d
	c = 0
	s = e1.get()
	s = s.title()
	for li in data:
		if s in li:
			d = li
			#print(li)
			c = 1
			break 
	if c != 1:
		root.destroy()
		createWindow()
	else:
		root.destroy()

def createWindow():
	global root,e1,imgpath
	root = Tk()
	root.resizable(0,0)
	root.geometry("+500+300")
	imgpath = os.path.abspath(os.getcwd()) + "\\" + "corona.ico"
	root.iconbitmap(imgpath)
	Label(root, text="Enter state name").grid(row=0)
	e1 = Entry(root)
	e1.grid(row=0, column=1)
	Button(root, text='Show', command=des).grid(row=3, column = 1,sticky=W, pady=4)
	root.mainloop()

def notifyme(title,message):
	global imgpath
	notification.notify(title = title,message = message,app_icon = imgpath,timeout = 10)

def scrap_data():
	l = []
	data = ""
	link = "https://www.mohfw.gov.in/"
	source = urllib.request.urlopen(link).read()

	soup = BeautifulSoup(source,"html.parser")

	for tr in soup.find_all('tbody'):
		data += tr.get_text()
	data = data[1:]

	d = data.split("\n\n")

	for item in d[0:33]:
		l.append(item.split("\n"))

	li = [x for x in l if x != ['']]

	for i in li:
		if i[0] != '':
			i.insert(0,'')

	return li

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
    	root = Tk()
    	root.withdraw()
    	tkinter.messagebox.showinfo("Alert","No internet")
    	return False


r = 0

if connect():
	print("connected")
else:
	print("no internet!")

while True:
	data = scrap_data()
	if r == 0:
		createWindow()
	msg = "Cases in "+ d[2]+ "\n" +"active : " + d[3]+ "\n"+ "Cured : "+ d[4]+ "\n"+ "Death : " + d[5]

	notifyme("Covid-19",msg)
	r = 1

	#break
	time.sleep(1800)












