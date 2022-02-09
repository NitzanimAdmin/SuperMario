import pygame


class ImageObject:
    def __init__(self, screen, x_pos, y_pos, width, height, img_path):
        self._screen = screen
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._width = width
        self._height = height
        self._img_path = img_path


    def display_image_to_screen(self):
        """
        Add the image of the given size to the screen in the desired location.
        :return: None
        """
        # Add the image to the screen
        img = pygame.image.load(self._img_path)
        img = pygame.transform.scale(img, (self._width, self._height))
        self._screen.blit(img, (self._x_pos, self._y_pos))

        # Update the screen
        pygame.display.flip()
