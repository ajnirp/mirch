#### Moving Pepper around

Edit the `ALProxy` constructor line in `walk.py` to Pepper's IP address. To get Pepper's IP address, press the power button once while it is on. Then run `python walk.py` and issue commands of the form `x y theta`. Example: `-1 0 -40` will make Pepper move 1m backwards while rotating 40 degrees clockwise. `navigate.py` is an example of Pepper executing an RVO path.

### TODO

1. Transfer a gait expressing emotions in the upper body onto Pepper (see: "Real Time Whole Body Motion Mapping" and "Working with MoCap file formats" in the papers/ directory).
2. Package that as a Choregraphe movement and loop it (or implement that with the Nao Python API - a lot more complicated).
3. Start both animations (upper-body movement + locomotion) simultaneously.