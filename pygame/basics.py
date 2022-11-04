

def load_image(filename, display_surface = None):
    img_surface = pg.image.load(filename).convert()
    if display_surface is not None:
        display_surface.blit(img_surface)
    else:
        return img_surface

def render_text(text, font = 'freesansbold.ttf', size = 18, antialias = True, color = 'BLACK'):
    text_font = pg.font.Font(font, size)
    text_surface = text_font.render(text, antialias, color)
    return text_surface


def main():
    print("Starting Game")

    print("Initialising pygame")
    pg.init()

    print("Setting up Display")
    pg.display.set_mode(DEFAULT_PARAMETERS.WINDOW_SIZE)
    pg.display.set_caption("Hello World!")

    print("Update display")
    pg.display.update()

    print("Starting main Game Playing Loop")
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and (event.key == pg.K_ESCAPE or event.key == pg.K_q):
                print("Received Quit Event:", event)
                running = False

    print("Game Over")
    pg.quit()

    return

if __name__ == '__main__':
    game = BoxGame()
    game.start()
