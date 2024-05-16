import pygame
import random

# 초기화
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("블록 깨기 게임")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# 공 설정
ball_width = 10
ball = pygame.Rect(screen_width // 2 - ball_width // 2, screen_height // 2 - ball_width // 2, ball_width, ball_width)
ball_speed = [3, 3]

# 패들 설정
paddle_width = 400
paddle_height = 10
paddle = pygame.Rect(screen_width // 2 - paddle_width // 2, screen_height - 30, paddle_width, paddle_height)
paddle_speed = 6

# 블록 설정
block_width = 60
block_height = 20
blocks = []
rows = 5
cols = screen_width // block_width
for row in range(rows):
    for col in range(cols):
        block = pygame.Rect(col * block_width, row * block_height, block_width, block_height)
        blocks.append(block)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < screen_width:
        paddle.right += paddle_speed

    # 공 이동
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # 벽과 충돌 처리
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]
    if ball.bottom >= screen_height:
        running = False  # 공이 바닥에 닿으면 게임 종료

    # 패들과 충돌 처리
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]

    # 블록과 충돌 처리
    for block in blocks[:]:
        if ball.colliderect(block):
            blocks.remove(block)
            ball_speed[1] = -ball_speed[1]
            break

    # 화면 그리기
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, RED, ball)
    for block in blocks:
        pygame.draw.rect(screen, BLUE, block)
    pygame.display.flip()

    # 프레임 설정
    pygame.time.Clock().tick(60)

pygame.quit()
