import pygame,random,os
pygame.init()

bg = (0,0,0)

enemy_x = random.randint(0, 640 - 50)
enemy_y = random.randint(0, 480 - 50)
player_size = 50
player_width = player_size
player_height = player_size
points = 0

player_y = 50
player_x = 50
pygame.display.set_caption("some random aim trainer")
screen = pygame.display.set_mode((640,480))
while True:
  screen.fill((0,0,0))
  font = pygame.font.Font('freesansbold.ttf', 32)
  text = font.render(str(points), True, (255,255,255), (0,0,0))
  textRect = text.get_rect()
  textRect.center = (320, 240)
  player = pygame.draw.rect(screen,(0,0,0),(player_x, player_y, player_width, player_height))
  screen.blit(text, textRect)
  enemy = pygame.draw.rect(screen,(255, 0, 0),(enemy_x, enemy_y , 50,50))

  pygame.display.update()
  events = pygame.event.get()
  for key in events:
        if key.type==pygame.QUIT:
            exit()
  keys = pygame.key.get_pressed()
  if keys[pygame.K_ESCAPE]:
    exit()
  mousemoved = pygame.mouse.get_focused()
  if mousemoved:
     mouse_pos = pygame.mouse.get_pos()
     player_x = mouse_pos[0] - player_width / 2
     player_y = mouse_pos[1] - player_height / 2

  def alert():
    print("crash: wall")
#   if player_y > 431:
#       player_y = player_y - 1
#       alert()
#   if player_x < 0:
#       player_x = player_x + 1
#       alert()
#   if player_y < 0:
#       player_y = player_y + 1
#       alert()
#   if player_x > 589:
#        player_x = player_x - 1
#        alert()
  if player.collidepoint(enemy.center):
      points+=1
      enemy_x = random.randint(0, 640 - 50)
      enemy_y = random.randint(0, 480 - 50)
      pygame.display.update()
