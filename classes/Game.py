import pygame
from constants import *
from classes.MovingObject import MovingObject
from classes.ImageObject import ImageObject


class Game:
    def __init__(self, screen):
        self.__screen = screen
        self.__object_list = []
        self.add_initial_objects()

    def add_initial_objects(self):
        background = ImageObject(self.__screen, 0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, 'Images/background.png')
        self.__object_list.append(background)

        yuval = MovingObject(self.__screen, 100, 50, 50, 'Images/blue_enemy.png', 20)
        yuval.display_image_to_screen()
        self.__object_list.append(yuval)


    def move_objects(self):
        for value in self.__object_list:
            if isinstance(value, MovingObject):
                value.move_object()

    def display_objects_to_screen(self):
        """
        The function goes over any object that is on the screen (using the dictionary that contains objects)
        and displays the objects on the screen.
        :return: None
        """
        for value in self.__object_list:
            value.display_image_to_screen()

    def on_click(self, mouse_pos):
        """
        Tests on the click of a button and checks which button was pressed using the 'Current Screen' variable.
        :param mouse_pos: The position of the mouse click.
        :return: None
        """
        print("click")

    def typing(self, ascii_val):
        """
        The function is called as soon as one of the keyboard keys is pressed.
        :param ascii_val: The key on the keyboard that was pressed by the user (Its ascii value).
        :return: None
        """
        if ascii_val == LEFT_ARROW:
            print("move left")
        elif ascii_val == RIGHT_ARROW:
            print("move right")
        elif ascii_val == UP_ARROW:
            print("move up")
        elif ascii_val == DOWN_ARROW:
            print("move down")
