import pygame as pg
from utils import *


class BoxGame():

    def __init__(self):
        pg.init()
        self.display = pg.display.set_mode(DEFAULT_PARAMETERS.WINDOW_SIZE)
        self.display.fill(COLORS.WHITE)
        pg.display.set_caption("Box Game!")
        pg.display.update()
        self.clock = pg.time.Clock()

    def start(self):
        print("Starting...")
        self.main_loop()

    def main_loop(self):
        running = True
        while running:
            for event in pg.event.get():
                running = self.check_event(event)
                pg.display.update()
                self.clock.tick(DEFAULT_PARAMETERS.FRAME_REFRESH_RATE)

        self.close_game()

    def check_event(self, event):
        if self.__closing_event(event):
            return False
        elif self.__mouse_event(event):
            x, y = event.pos
            pg.draw.rect(self.display, COLORS.BLUE, [x, y, 10, 10])
            return True
        else:
            return True


    def __closing_event(self, event):
        return event.type == pg.QUIT or event.type == pg.KEYDOWN and (event.key == pg.K_ESCAPE or event.key == pg.K_q)

    def __mouse_event(self, event):
        return event.type == pg.MOUSEBUTTONDOWN

    def close_game(self):
        print("Game Over!")
        pg.quit()


if __name__ == '__main__':
    game = BoxGame()
    game.start()