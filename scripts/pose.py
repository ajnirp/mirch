from naoqi import ALProxy

motion = ALProxy("ALMotion", "152.23.17.251", 9559)
posture = ALProxy("ALRobotPosture", "152.23.17.251", 9559)

motion.rest()
posture.goToPosture("StandInit", 5)