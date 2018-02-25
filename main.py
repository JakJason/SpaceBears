import pygame


def main():
    ## Game Variables
    finished = False
    fps = 60
    game_title = 'SpaceBears'
    display_width = 1920    ## My screen size
    display_height = 1080   ## My screen size

    center_width = display_width/2
    center_height = display_height/2

    ## Initate game
    pygame.init()
    gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.RESIZABLE)
    pygame.display.set_caption(game_title)
    clock = pygame.time.Clock()

    ## Gameloop
    while not finished:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    finished = True

            print(event)

        pygame.display.update()

        clock.tick(fps)

    ## Quit program
    pygame.quit()
    quit()

if __name__ == '__main__':
    main()
