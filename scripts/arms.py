from naoqi import ALProxy

import math

motion = ALProxy("ALMotion", "152.23.23.200", 9559)
motion.wakeUp()

motion.setMoveArmsEnabled(True, True)