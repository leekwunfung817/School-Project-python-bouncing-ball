import pygame
import random

background = (0, 0, 0)
ball_color = (255, 255, 255)
window_width = 700
window_height = 500
ball_size = 25

speed = 60
minimum_speed = -10
maximum_speed = 10


class BallObject:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0

    def change(self):
        self.x += self.change_x
        self.y += self.change_y

        if self.y > window_height - ball_size or self.y < ball_size:
            self.change_y *= -1
        if self.x > window_width - ball_size or self.x < ball_size:
            self.change_x *= -1


def BallFactory():
    ball = BallObject()
    ball.x = random.randrange(ball_size, window_width - ball_size)
    ball.y = random.randrange(ball_size, window_height - ball_size)
    ball.change_x = random.randrange(minimum_speed, maximum_speed)
    ball.change_y = random.randrange(minimum_speed, maximum_speed)
    print(str(ball.change_x))
    print(str(ball.change_y))
    return ball


def main():
    pygame.init()
    size = [window_width, window_height]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Bouncing Balls")
    done = False
    clock = pygame.time.Clock()
    ball_list = []
    ball = BallFactory()
    ball_list.append(ball)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ball = BallFactory()
                    ball_list.append(ball)
        for ball in ball_list:
            ball.change()
        screen.fill(background)
        for ball in ball_list:
            pygame.draw.circle(screen, ball_color, [ball.x, ball.y], ball_size)
        clock.tick(speed)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
