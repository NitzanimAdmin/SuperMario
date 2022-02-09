from classes.Game import *
import pygame
from classes.MovingObject import MovingObject
new_game = None


def main():
    pygame.init()
    # Create the screen and show it
    screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(screen_size)

    # pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    # Set background
    background_img_path = 'Images/background.png'
    background = pygame.image.load(background_img_path)
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))
    screen.blit(background, (0, 0))

    pygame.display.set_caption('Super Mario')

    global new_game
    new_game = Game(screen)
    # yesss = MovingObject(screen, 40, 60, 60, 'Images/blue_enemy.png')
    # Display all drawings we have defined
    pygame.display.flip()

    status = running()
    while status:
        # Check if the player wants to end the game
        status = running()

    # Close The window
    pygame.quit()


def running():
    """
    The function checks when the game will end.
    In addition, the function checks the mouse click events.
    :return: None
    """
    status = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            status = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 1 is the left mouse button, 2 is middle, 3 is right.
            if event.button == 1:
                new_game.on_click(event.pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                status = False
            else:
                new_game.typing(event.key)
    return status


main()