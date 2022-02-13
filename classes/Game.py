import pygame
import random
from constants import *
from classes.MovingObject import MovingObject
from classes.Obstacle import Obstacle
from classes.ImageObject import ImageObject
from classes.Mario import Mario
import time


class Game:
    def __init__(self, screen):
        self.__screen = screen
        self.__object_list = []
        self.__mario = None
        self.add_initial_objects()
        self.__can_move = True
        self.__is_game_over = False

    def is_game_over(self):
        self.check_if_game_over()
        return self.__is_game_over

    def add_initial_objects(self):
        background = ImageObject(self.__screen, 0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, 'Images/background.png')
        self.__object_list.append(background)

        self.__mario = Mario(self.__screen, SUPER_MARIO_START_X_POS, SUPER_MARIO_START_Y_POS,
                             SUPER_MARIO_WIDTH, SUPER_MARIO_HEIGHT, SUPER_MARIO_IMG_PATH)

        for i in range(3):
            self.__create_new_moving_object(i)

    def __create_new_moving_object(self, space_between_obj=1):
        rand_height = random.randint(0, 1)
        if rand_height == 1:
            # The moving object is on the ground
            rand_moving_object = random.randint(1, len(GROUND_MOVING_OBJECTS_IMAGES))
            moving_objects_image = GROUND_MOVING_OBJECTS_IMAGES[rand_moving_object - 1]
        else:
            # The moving object is on the sky
            rand_moving_object = random.randint(1, len(SKY_MOVING_OBJECTS_IMAGES))
            moving_objects_image = SKY_MOVING_OBJECTS_IMAGES[rand_moving_object - 1]

        y_pos = TOP_Y_YOS + rand_height * SPACE_BETWEEN_MOVING_OBJECTS_Y
        obstacle = Obstacle(self.__screen,
                            WINDOW_WIDTH - ENEMY_SIZE + SPACE_BETWEEN_MOVING_OBJECTS_X * space_between_obj,
                            y_pos, ENEMY_SIZE, ENEMY_SIZE, moving_objects_image, SPEED)

        self.__object_list.append(obstacle)

    def move_objects(self):
        for value in self.__object_list:
            if isinstance(value, MovingObject):
                value.move_object()

                if value.is_out_of_screen():
                    self.__object_list.remove(value)
                    self.__create_new_moving_object()

    def display_objects_to_screen(self):
        """
        The function goes over any object that is on the screen (using the dictionary that contains objects)
        and displays the objects on the screen.
        :return: None
        """
        for value in self.__object_list:
            value.display_image_to_screen()

        self.__mario.display_image_to_screen()



    def on_click(self, mouse_pos):
        """
        Tests on the click of a button and checks which button was pressed using the 'Current Screen' variable.
        :param mouse_pos: The position of the mouse click.
        :return: None
        """
        print("click")

    def move_mario(self, direction):
        if not self.__can_move:
            return
        if direction == "left":
            self.__mario.move_left()
        elif direction == "right":
            self.__mario.move_right()
        elif direction == "jump":
            self.make_mario_jump()
        elif direction == "bend":
            self.__mario.bend()

    def make_mario_jump(self):
        if not self.__can_move:
            return

        self.__can_move = False
        self.display_objects_to_screen()

        ans = self.__mario.jump()

        while not self.is_game_over() and ans != "done":
            self.move_objects()
            self.display_objects_to_screen()
            ans = self.__mario.jump()
            pygame.display.flip()

        # for i in range(10):
        #     self._y_pos -= MINI_MOVE_IN_Y
        #     pygame.display.flip()
        #     time.sleep(0.1)
        #
        # time.sleep(0.3)
        #
        # for i in range(10):
        #     self._y_pos += MINI_MOVE_IN_Y
        #     pygame.display.flip()
        #     time.sleep(0.1)

        self.__can_move = True

    def check_if_game_over(self):
        for obj in self.__object_list:
            if isinstance(obj, Obstacle):
                obj_location = {'x': obj.x_pos, 'y': obj.y_pos}
                obj_size = {'width': obj.width, 'height': obj.height}

                if self.__mario.is_object_on_image(obj_location, obj_size):
                    self.__is_game_over = True


"""
    def typing(self, ascii_val):
        
        The function is called as soon as one of the keyboard keys is pressed.
        :param ascii_val: The key on the keyboard that was pressed by the user (Its ascii value).
        :return: None
        
        # if ascii_val == LEFT_ARROW:
        if ascii_val == pygame.K_LEFT:
            self.__super_mario.move_left()
        # elif ascii_val == RIGHT_ARROW:
        elif ascii_val == pygame.K_RIGHT:
            self.__super_mario.move_right()
        # elif ascii_val == UP_ARROW:
        elif ascii_val == pygame.KEYUP:
            print("move up")
        # elif ascii_val == DOWN_ARROW:
        elif ascii_val == pygame.KEYDOWN:
            print("move down")
            """