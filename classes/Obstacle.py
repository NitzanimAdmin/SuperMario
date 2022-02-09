import pygame
from classes.MovingObject import MovingObject


class Obstacle(MovingObject):
    def __init__(self, screen, y_pos, width, height, img_path, speed):
        MovingObject.__init__(self, screen, y_pos, width, height, img_path, speed)
