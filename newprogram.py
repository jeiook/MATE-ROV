#!/usr/bin/env python

import pygame
import socket

IP = '192.168.7.2'
PORT = 22
TRIGGER = 0
X_AXIS = 0
Y_AXIS = 1
Z_AXIS = 2

pygame.joystick.init()
rjoystick = pygame.joystick.Joystick(0)
rjoystick.init()
size = [500, 500]
screen = pygame.display.set_mode(size)

motor = [0, 0, 0, 0]
angle = [0, 0, 0, 0]

while True:
	for event in pygame.event.get(): # User did something; This seems to be required
		if event.type == pygame.QUIT:
			quit()
	#for i in range( rjoystick.get_numbuttons() ):
	#you can put rjoystick.get_numbuttons() inside the condition for compactness
	if rjoystick.get_button( 0 ) == 1:
		print "\n\n\n\n\n\n\n\n\n\n\nTrigger\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
	if rjoystick.get_axis( 0 ) != 0:
