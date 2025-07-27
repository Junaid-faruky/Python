import pygame, random
pygame.init()

# Setup
win = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

# Ball
ball = pygame.Rect(300, 200, 15, 15)
ball_speed = [3, 3]

# Paddle
paddle = pygame.Rect(270, 350, 60, 10)

# Bricks
bricks = [pygame.Rect(x*60, y*20, 58, 18) for x in range(10) for y in range(5)]

# Game loop
run = True
while run:
    win.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Move paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0: paddle.move_ip(-5, 0)
    if keys[pygame.K_RIGHT] and paddle.right < 600: paddle.move_ip(5, 0)

    # Move ball
    ball.move_ip(*ball_speed)

    # Bounce
    if ball.left <= 0 or ball.right >= 600: ball_speed[0] *= -1
    if ball.top <= 0: ball_speed[1] *= -1
    if ball.colliderect(paddle): ball_speed[1] *= -1

    # Brick collision
    for brick in bricks[:]:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_speed[1] *= -1
            break

    # Game over
    if ball.bottom >= 400:
        run = False

    # Draw
    pygame.draw.rect(win, (255,255,255), paddle)
    pygame.draw.ellipse(win, (255,0,0), ball)
    for brick in bricks:
        pygame.draw.rect(win, (0,255,0), brick)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
