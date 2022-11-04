import random
import time
import pygame
import numpy as np

# CONSTANTS
BLUE = (0,0,255)
WHITE = (0, 0, 0)
BACKGROUND = WHITE
FRAME_REFRESH_RATE = 60
DISPLAY_WIDTH = 640
DISPLAY_HEIGHT = 480

STARSHIP_SPEED = 3
max_meteor_speed = 4

INITIAL_NUMBER_OF_METEORS = 10
MAX_NUMBER_OF_CYCLES = 1000
NEW_METEOR_CYCLE_INTERVAL = 20

class Game:
    def __init__(self):
        print('Initialising PyGame')
        pygame.init()

        self.display_surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        pygame.display.set_caption("Starship Meteors")

        self.clock = pygame.time.Clock()

        self.starship = Starship(self)
        self.starship.draw()

        self.meteors = []
        for _ in range(INITIAL_NUMBER_OF_METEORS):
            self._new_meteor()

    def play(self):
        global max_meteor_speed
        is_running = True
        starship_collided = False
        cycle_count = 0
        move_x = 0
        move_y = 0

        while is_running and not starship_collided:
            cycle_count += 1
            
            if cycle_count == MAX_NUMBER_OF_CYCLES:
                self._display_message("WINNER!")
                break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._display_message("Closing the game")
                    is_running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        print("Closing the game")
                        is_running = False

                    # WASD commands
                    elif event.key == pygame.K_w or event.key == pygame.K_UP:
                        move_y = -1
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        move_x = -1
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        move_y = 1
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        move_x = 1
                    elif event.key == pygame.K_p:
                        self._pause()


                elif event.type == pygame.KEYUP:
                    move_x =  0
                    move_y = 0
                    keyState = pygame.key.get_pressed()
                    if keyState[pygame.K_w]:
                        move_y = -1
                    elif keyState[pygame.K_a]:
                        move_x = -1
                    elif keyState[pygame.K_s]:
                        move_y = 1
                    elif keyState[pygame.K_d]:
                        move_x = 1

            self.display_surface.fill(BACKGROUND)
            self.starship.move(move_x, move_y)
            self.starship.draw()

            for meteor in self.meteors:
                meteor.move()
                meteor.draw()
                starship_collided = self._check_collision(meteor)

                if starship_collided:
                    self._display_message("Game Over!")
                    break

                if meteor.is_out():
                    self.meteors.remove(meteor)
                    self._new_meteor()

            pygame.display.update()

            # Determine if new mateors should be added
            if cycle_count % NEW_METEOR_CYCLE_INTERVAL == 0:
                max_meteor_speed *= 1.01


            self.clock.tick(FRAME_REFRESH_RATE)

        time.sleep(1)
        pygame.quit()

    def _check_collision(self, meteor):
        return self.starship.rect().colliderect(meteor.rect())

    def _pause(self):
        self._display_message("Pause...")
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        paused = False
                        break

    def _display_message(self, message):
        print(message)
        text_font = pygame.font.Font('freesansbold.ttf', 48)
        text_surface  = text_font.render(message, True, BLUE, WHITE)
        text_rectangle = text_surface.get_rect()
        text_rectangle.center = (DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2)
        self.display_surface.fill(WHITE)
        self.display_surface.blit(text_surface, text_rectangle)
        pygame.display.update()

    def _new_meteor(self):
        meteor = Meteor(self)

        x =  np.random.normal(self.starship.x, DISPLAY_WIDTH/4)
        x = np.clip(x, 0, DISPLAY_WIDTH)
        y = 10
        meteor.set_position(x, y)
        self.meteors.append(meteor)


class GameObject():

    def __init__(self, game, image_filename=None):
        self.game = game

        if image_filename is not None:
            self.load_image(image_filename)

    def set_position(self, x=0, y=0):
        self.x = x
        self.y = y

    def load_image(self, filename):
        self.image = pygame.image.load(filename).convert()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        if self.width > self.height:
            self.height = int(30 * self.height/self.width)
            self.width = 30
        else:
            self.width = int(30 * self.width/self.height)
            self.height = 30

        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        self.game.display_surface.blit(self.image, (self.x, self.y))

    def move(self, dx, dy, speed):
        self.x += dx * speed
        self.y += dy * speed

        if self.x < 0:
            self.x = 0
        elif self.x + self.width > DISPLAY_WIDTH:
            self.x = DISPLAY_WIDTH - self.width

        if self.y < 0:
            self.y = 0
        elif self.y + self.height > DISPLAY_HEIGHT:
            self.y = DISPLAY_HEIGHT - self.height


class Starship(GameObject):

    def __init__(self, game):
        super().__init__(game, "images/img.png")
        self.set_position(DISPLAY_WIDTH / 2, DISPLAY_HEIGHT - 40)

    def move(self, dx, dy):
        super().move(dx, dy, STARSHIP_SPEED)

    def rect(self):
        return pygame.Rect(self.x+10, self.y+10, self.width-10, self.height - 10)

class Meteor(GameObject):
    def __init__(self, game):
        super().__init__(game, "images/img_1.png")
        self.speed = np.random.randint(1, max_meteor_speed)

    def move(self):
        self.y += self.speed

    def is_out(self):
     return self.y > DISPLAY_HEIGHT

def main():
    print("Starting game")
    game = Game()
    game.play()
    print("Game Over")

if __name__ == '__main__':
    main()