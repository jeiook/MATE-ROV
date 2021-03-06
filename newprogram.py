#!/usr/bin/env python

import sys, os
import pygame
import pexpect.pxssh
import pxssh
import getpass

# Assuming these:
# motor0 - front left
# motor1 - back left
# motor2 - front right
# motor3 - back right

IP = "192.168.7.2"
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

"""try:
	s = pxssh.pxssh()
	username = "root"
	password = ""
	s.login(IP, username, password)
	s.sendline ('cd /home/debian/Desktop')
	s.prompt()
	print s.before

except pxssh.ExceptionPxssh, e:
	print "pxssh failed on login."
	print str(e)
"""
sys.stdout = os.devnull
sys.stderr = os.devnull

while True:
	for event in pygame.event.get(): # Checks if something happened; This seems to be required for the joystick things to happen.
		if event.type == pygame.QUIT:
			quit()
	if rjoystick.get_button( TRIGGER ) == 1:
		#s.sendline ('python trigger.py')
		#s.prompt()
		sys.stdout = sys.__stdout__
		sys.stderr = sys.__stderr__
		#print s.before
		sys.stdout = os.devnull
		sys.stderr = os.devnull
	if rjoystick.get_axis( X_AXIS ) >= 15000:
		#s.sendline ('roll_right.py')
		#s.prompt()
		sys.stdout = sys.__stdout__
		sys.stderr = sys.__stderr__		
		#print s.before
		sys.stdout = os.devnull
		sys.stderr = os.devnull
	if rjoystick.get_axis( X_AXIS ) <= -15000:
		#s.sendline ('roll_left.py')
		#s.prompt()
		sys.stdout = sys.__stdout__
		sys.stderr = sys.__stderr__		
		#print s.before
		sys.stdout = os.devnull
		sys.stderr = os.devnull
	if rjoystick.get_axis( Y_AXIS ) >= 15000:
		#s.sendline ('python pitch_up.py')
		#s.prompt()
		sys.stdout = sys.__stdout__
		sys.stderr = sys.__stderr__		
		#print s.before
		sys.stdout = os.devnull
		sys.stderr = os.devnull
	if rjoystick.get_axis( Y_AXIS ) <= -15000:
		#s.sendline ('python pitch_down.py')
		#s.prompt()
		sys.stdout = sys.__stdout__
		sys.stderr = sys.__stderr__		
		#print s.before
		sys.stdout = os.devnull
		sys.stderr = os.devnull
	if rjoystick.get_axis( Z_AXIS ) >= 15000:
		#s.sendline ('python yaw_right.py')
		#s.prompt()
		sys.stdout = sys.__stdout__
		sys.stderr = sys.__stderr__		
		#print s.before
		sys.stdout = os.devnull
		sys.stderr = os.devnull
	if rjoystick.get_axis( Z_AXIS ) >= 15000:
		#s.sendline ('python yaw_left.py')
		#s.prompt()
		sys.stdout = sys.__stdout__
		sys.stderr = sys.__stderr__				
		#print s.before
		sys.stdout = os.devnull
		sys.stderr = os.devnull
	if rjoystick.get_button( 1 ) == 1:
                quit()
