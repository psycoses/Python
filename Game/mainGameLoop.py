import pygame
import tkinter as tk 
from tkinter import *
import os

W = 1280
H = 720

root = tk.Tk()
embed = tk.Frame(root, width=W,height=H)
embed.grid(columnspan = (W+100), rowspan = H) # Adds grid
embed.pack(expand=True) 


os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'

screen = pygame.display.set_mode((W,H))
screen.fill(pygame.Color(255,160,122))

root.resizable(False,False)
pygame.display.init()
pygame.display.update()

def draw():
	pygame.draw.circle(screen, (0,0,0), (int(W/2),int(H/2)), 125)
	pygame.display.update()
	root.update()

while True:
	pygame.display.update()
	root.update()
	draw()
	
