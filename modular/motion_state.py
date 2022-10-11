from enum import Flag, auto

class motion_state(Flag):
    LEFT = auto()
    RIGHT = auto()
    FORWARD = auto()
    BACKWARD = auto()
    STOP = auto()
