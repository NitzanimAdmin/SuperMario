import pygame
from classes.ImageObject import ImageObject
from constants import WINDOW_WIDTH


class MovingObject(ImageObject):
    def __init__(self, screen, y_pos, width, height, img_path):
        ImageObject.__init__(self, screen, WINDOW_WIDTH, y_pos, width, height, img_path)
        self._speed = speed

    def move_object(self):
        self._x_pos += self._speed
