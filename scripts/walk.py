from naoqi import ALProxy

import math
import sys

motion = ALProxy("ALMotion", "152.23.151.210", 9559)
# motion.wakeUp()

def quit():
	print('exiting')
	sys.exit(0)

command = None
while True:
	command = raw_input('command: ')
	if command.strip() in ['quit', 'exit']:
		quit()
	if command.strip() == '':
		continue
	try:
		x, y, theta = map(float, command.split())
		theta = theta * math.pi / 180.0
		print('moving to', x, y, theta)
		motion.moveTo(x, y, theta)
		# motion.waitUntilMoveIsFinished()
	except Exception:
		quit()