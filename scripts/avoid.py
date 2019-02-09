from naoqi import ALProxy

import sys

if len(sys.argv) != 2:
    print('usage: python avoid.py <ip-address>', file=sys.stderr)
    sys.exit(0)

nav = ALProxy("ALNavigation", sys.argv[1], 9559)

if not nav.navigateTo(3.0, 0.0):
    print('Failed to navigate')
