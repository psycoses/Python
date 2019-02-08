import pygame
import tkinter as tk 
from tkinter import *
import os
import time
import sys

W = 1280
H = 720

root = tk.Tk()
embed = tk.Frame(root, width=W,height=H)
embed.grid(columnspan = (W), rowspan = H) # Adds grid 

os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'

screen = pygame.display.set_mode((W,H))

time_start = time.time()
fps_time = time.time()
seconds = 0
minutes = 0
x = 1
fps = 0
usernameEntry = Entry(root)
passwordEntry = Entry(root)
username=''
password=''
	
def main():
	#load background
	try:
		background = pygame.image.load('D:/Python/Game/Resources/Images/background.jpg').convert()
	except ImportError:
		print("could not load background")	
	#update to background
	screen.blit(background, [0,0])
	#make window non-resizable
	root.resizable(False,False)
	#initalization of disyplay/font and update of display
	pygame.display.init()
	pygame.display.update()
	pygame.font.init()

#calling main setup once
main()

def showLoad():
	
	myFont = pygame.font.SysFont('monaco', 72)
	load = myFont.render('My Game', True, (255,255,255))
	loadPlace = load.get_rect()
	loadPlace.midtop = (W/2,H/2-250)
	screen.blit(load,loadPlace)
	
	#username and password entry
	global usernameEntry
	global passwordEntry 
	
	Label(root, text='Username ').grid(row=int(H/2),column=int(W/2)-10)
	Label(root, text='Password  ').grid(row=int(H/2+5),column=int(W/2)-10)
	
	root.loginButt = Button(root., text='Login', command=checkLogin).grid(row=int(H/2 + 10),column=int(W/2))
	
	usernameEntry.grid(row=int(H/2),column=int(W/2))
	passwordEntry.grid(row=int(H/2+5),column=int(W/2))
	
	#updating pygame window
	pygame.display.flip()
	pygame.display.update()
	root.update()
	
def checkLogin():
	if usernameEntry.get() == 'theinprisoned' and passwordEntry.get() == 'test':
		print('Login Successfull')
		print(usernameEntry.get())
		print(passwordEntry.get())
		return True
	else:
		return False
	
def time_FPS():
	global minutes
	global seconds
	global fps
	global time_start
	global fps_time
	sys.stdout.write("\r{minutes} Minutes {seconds} Seconds ".format(minutes=minutes, seconds=seconds))
	sys.stdout.flush()
	time.sleep(1)
	seconds = int(time.time() - time_start) - minutes * 60
	if seconds >= 60:
		minutes += 1
		seconds = 0
		
	fps+=1
	if (time.time() - fps_time) > x:
		print("FPS: ", fps / (time.time() - fps_time))
		fps = 0
		fps_time = time.time()
		 

def displayGame():
		myFont = pygame.font.SysFont('monaco', 72)
		load = myFont.render('Game loaded', True, (255,255,255))
		loadPlace = load.get_rect()
		loadPlace.midtop = (W/2,H/2-250)
		screen.blit(load,loadPlace)
		pygame.display.flip()
		pygame.display.update()
		root.update()


	#if usernameEntry.get() == 'theinprisoned' and passwordEntry.get() == 'test':
	#	displayGame()

showLoad()
while True:
	time_FPS()
	pygame.display.update()
	root.update()
	
	if checkLogin() == True:
		displayGame()
	
	
