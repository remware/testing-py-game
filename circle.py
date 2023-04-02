# Example showing a circle moving on screen
import pygame

class MovableCircle:
    # pygame setup
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0
        self.player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)

    def run(self):
        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("blue")

            pygame.draw.circle(self.screen, "red", self.player_pos, 40)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.player_pos.y -= 300 * dt
            if keys[pygame.K_s]:
                self.player_pos.y += 300 * dt
            if keys[pygame.K_a]:
                self.player_pos.x -= 300 * dt
            if keys[pygame.K_d]:
                self.player_pos.x += 300 * dt
            if keys[pygame.K_q]:
                self.running = False

            # flip() the display to put your work on screen
            pygame.display.flip()

            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            dt = self.clock.tick(60) / 1000

    def stop(self):
        pygame.quit()      

if __name__ == '__main__':
    me = MovableCircle()
    me.run()
    me.stop()
    
