import pygame
from ImageObject import ImageObject
from constants import WINDOW_WIDTH


class MovingObject(ImageObject):
    def __init__(self, screen, y_pos, height, img_path, speed):
        ImageObject.__init__(self, screen, WINDOW_WIDTH, y_pos, WINDOW_WIDTH, height, img_path)
        self._speed = speed

    def move_object(self):
        self._x_pos += self._speed
