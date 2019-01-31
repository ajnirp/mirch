import naoqi
import time

motion = naoqi.ALProxy("ALMotion", "152.23.17.251", 9559)
motion.wakeUp()

motion.move(-0.2, 0, 0)
time.sleep(5)
print('done sleeping')
motion.stopMove()
motion.rest()