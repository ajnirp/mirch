# -*- coding: utf-8 -*-

from naoqi import ALProxy

tts = ALProxy("ALTextToSpeech", "152.23.16.130", 9559)
tts.say("hello world")