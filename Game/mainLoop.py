import pygame
import tkinter as tk
from tkinter import *
import os
import time
import sys

#Constants
Width = 1280
Height = 720

#creation of tkinter window
root = tk.Tk()
embed = tk.Frame(root, width=Width,height=Height)
embed.grid(columnspan = (Width), rowspan = Height) # Adds grid 

#inputs pygame window into Tkinter window
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'

#creation of pygame window
screen = pygame.display.set_mode((Width,Height))

#timer and FPS counter Constants
time_start = time.time()
fps_time = time.time()
seconds = 0
minutes = 0
x = 1
fps = 0
#username constants
usernameEntry = Entry(root)
passwordEntry = Entry(root)
username=''
password=''


def checkLogin():
	displayGame()

# used to load background graphics aswell as exit button and login buttons
def loadBG():
	#initalization of display/font and update of display
	pygame.display.init()
	pygame.display.update()
	pygame.font.init()

	#load up background
	try:
		background = pygame.image.load('D:/Python/Game/Resources/Images/background.jpg').convert()
	except ImportError:
		print("could not load background")	
	#update to background
	screen.blit(background, [0,0])
	#make window non-resizable
	root.resizable(False,False)
	
	#game name and font loading
	myFont = pygame.font.SysFont('monaco', 72)
	load = myFont.render('My Game', True, (255,255,255))
	loadPlace = load.get_rect()
	loadPlace.midtop = (Width/2,Height/2-250)
	screen.blit(load,loadPlace)
	
	#username and password entry
	global usernameEntry
	global passwordEntry 
	
	Label(root, text='Username ').grid(row=int(Height/2),column=int(Width/2)-10)
	Label(root, text='Password  ').grid(row=int(Height/2+5),column=int(Width/2)-10)
	
	root.loginButt = Button(root, text='Login', command=checkLogin).grid(row=int(Height/2 + 10),column=int(Width/2))
	
	usernameEntry.grid(row=int(Height/2),column=int(Width/2))
	passwordEntry.grid(row=int(Height/2+5),column=int(Width/2))
loadBG()

def displayGame():
	myFont2 = pygame.font.SysFont('monaco', 72)
	load2 = myFont.render('Game loaded', True, (255,255,255))
	loadPlace2 = load.get_rect()
	loadPlace2.midtop = (Width/2,Height/2-250)
	screen.blit(load,loadPlace)
	pygame.display.flip()
	pygame.display.update()
	root.update()


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


while True:
		time_FPS()
		pygame.display.update()
		root.update()
