import qi
import time

session = qi.Session()
session.connect('tcp://152.23.16.130:9559')
motion = session.service('ALMotion')
motion.setStiffnesses('Body', 1)
# motion.setAngles(['LShoulderPitch', 'LShoulderRoll', 'LElbowYaw'], [-1, 0.25, -1.5], 0.3)
motion.setAngles(['LWristYaw'], [-1.8], 0.2)
# motion.moveTo(0.2,0,0)