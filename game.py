import pygame,random,os
pygame.init()
bg = (0,0,0)
enemy_x = random.randint(0, 640 - 50)
enemy_y = random.randint(0, 480 - 50)
points = 0

player_y = 50
player_x = 50
pygame.display.set_caption("some random aim trainer")
screen = pygame.display.set_mode((640,480))
while True:
  screen.fill((0,0,0))

  player = pygame.draw.rect(screen,(0,0,0),(player_x, player_y, 50,50))
  enemy = pygame.draw.rect(screen,(255, 0, 0),(enemy_x, enemy_y , 50,50))

  pygame.display.update()
  events = pygame.event.get()
  for key in events:
        if key.type==pygame.QUIT:
            exit()
  keys = pygame.key.get_pressed()
  mousemoved = pygame.mouse.get_focused()
  if mousemoved:
     mouse_pos = pygame.mouse.get_pos()
     player_x = mouse_pos[0] - 25
     player_y = mouse_pos[1] - 25

  if key.type == pygame.KEYDOWN:
            if key.key == pygame.K_LEFT or key.key == pygame.K_a:
                player_x -= 1
                
            if key.key == pygame.K_RIGHT or key.key == pygame.K_d:
                player_x += 1
                
            if key.key == pygame.K_UP or key.key == pygame.K_w:
                player_y -= 1
                
            if key.key == pygame.K_DOWN or key.key == pygame.K_s:
                player_y += 1
                
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
      # kill the enemy
      enemy_x = random.randint(0, 640 - 50)
      enemy_y = random.randint(0, 480 - 50)
      pygame.display.update()
      os.system('cls')
      print(f"Points: {points}")