from naoqi import ALProxy

motion = ALProxy("ALMotion", "152.23.17.251", 9559)
motion.wakeUp()

motion.moveTo(0.5, 0, 0, [['MaxVelXY', 0.02]])
# motion.waitUntilMoveIsFinished()