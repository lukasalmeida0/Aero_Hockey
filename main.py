import pygame

pygame.init()
pygame.font.init()

jogando_song = pygame.mixer.Sound('assets/jogando.wav')
hit = pygame.mixer.Sound("assets/ping.wav")

pygame.display.set_caption('AERO HOCKEY')
icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)

display = pygame.display.set_mode((1280, 720))

menu_img = pygame.image.load('assets/menu_ah.png')

gameover_img = pygame.image.load('assets/gameover_ah.png')
gameover1 = pygame.image.load('assets/vitoria1.png')
gameover2 = pygame.image.load('assets/vitoria2.png')


campo_img = pygame.image.load('assets/fundo_ah.jpeg')
campo = campo_img.get_rect()

player1_img = pygame.image.load('assets/p1.png')
player1 = player1_img.get_rect(left=30)
player1_speed = 10 # velocidade que o player 1 vai se movimentar

score1 = 0
score2 = 0


player2_img = pygame.image.load('assets/p2.png')
player2 = player2_img.get_rect(right=1250)
player2_speed = 10 # velocidade que o player 2 vai se movimentar

ball_img = pygame.image.load('assets/ball.png')
ball = ball_img.get_rect(center= [1280 / 2, 720 / 2])
ball_dir_x = 10 # direção da bola no eixo x
ball_dir_y = 10 # direção da bola no eixo y

font = pygame.font.Font(None, 50)
placar1 = font.render(str(score1), True, 'black')
placar2 = font.render(str(score2), True, 'black')


fade_img = pygame.Surface((1280, 720)).convert_alpha()
fade = fade_img.get_rect()
fade_img.fill('black')
fade_alpha = 255


fps = pygame.time.Clock()
loop = True
cena = 'menu'

jogando_song.play(-1)
    

while loop:

    if cena == 'single':

        player1.y += player1_speed # Movimento player 1
        player2.y = ball.y - 75 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player1_speed = -10

                if event.key == pygame.K_s:
                    player1_speed = 10

        # # # COLISÃO ------------------------------------------
        if ball.colliderect(player1) or ball.colliderect(player2):
            ball_dir_x *= -1
            hit = pygame.mixer.Sound("assets/ping.wav")
            hit.play()

        # # # CONDIÇÃO PARA DERROTA ----------------------------
        if ball.x < 29:
            cena = 'gameover'
            fade_alpha = 255
        
        if fade_alpha > 0:
            fade_alpha -= 9
            fade_img.set_alpha(fade_alpha)

        # # # SCORE --------------------------------------------
        if ball.colliderect(player1):
            score1 += 1
            placar1 = font.render(str(score1), True, 'black')

        # # # LIMITE DA MOVIMETAÇÃO P1 -------------------------
        if player1.y <= 0:
            player1.y = 0
        if player1.y >=720 - 150:
            player1.y = 720 - 150

        # # # LIMITE DA MOVIMENTAÇÃO P2 ------------------------
        if player2.y <= 0:
            player2.y = 0
        if player2.y >=720 - 150:
            player2.y = 720 - 150

        # # # MOVIMENTO BOLA Y ---------------------------------
        if ball.y <= 0:
            ball_dir_y *= -1
        if ball.y >= 720 - 15:
            ball_dir_y *= -1
        
        # # # MOVIMENTO BOLA X ---------------------------------
        if ball.x <= 0:
            ball.x = 600
            ball_dir_x *= -1
        if ball.x >= 1280:
            ball.x = 600
            ball_dir_x *= -1

        ball.x += ball_dir_x
        ball.y += ball_dir_y

        # # # DESENHANDO NA TELA -------------------------------
        display.fill((0, 0, 0))
        display.blit(campo_img, campo)
        display.blit(player1_img, player1)
        display.blit(player2_img, player2)
        display.blit(ball_img, ball)
        display.blit(placar1, (640, 30))
        display.blit(fade_img, fade)

    if cena == 'multi':

        player1.y += player1_speed # Movimento player 1
        player2.y += player2_speed # Movimento player 2


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player1_speed = -10

                if event.key == pygame.K_s:
                    player1_speed = 10

                if event.key == pygame.K_UP:
                    player2_speed = -10
                
                if event.key == pygame.K_DOWN:
                    player2_speed = 10

        # # # COLISÃO ------------------------------------------
        if ball.colliderect(player1) or ball.colliderect(player2):
            ball_dir_x *= -1
            hit.play()

        # # # SCORE --------------------------------------------
        if ball.x > 1279:
            score1 += 1
            placar1 = font.render(str(score1), True, 'black')
        
        if ball.x < 1:
            score2 += 1
            placar2 = font.render(str(score2), True, 'black')

        # # # CONDIÇÃO PARA DERROTA ----------------------------
        if score1 > 9:
            cena = 'gameover1'
            fade_alpha = 255

        if score2 > 9:
            cena = 'gameover2'
            fade_alpha = 255
        
        if fade_alpha > 0:
            fade_alpha -= 9
            fade_img.set_alpha(fade_alpha)


        # # # LIMITE DA MOVIMETAÇÃO P1 -------------------------
        if player1.y <= 0:
            player1.y = 0
        if player1.y >=720 - 150:
            player1.y = 720 - 150

        # # # LIMITE DA MOVIMENTAÇÃO P2 ------------------------
        if player2.y <= 0:
            player2.y = 0
        if player2.y >=720 - 150:
            player2.y = 720 - 150

        # # # MOVIMENTO BOLA Y ---------------------------------
        if ball.y <= 0:
            ball_dir_y *= -1
            hit.play()
        if ball.y >= 720 - 35:
            ball_dir_y *= -1
            hit.play()
        
        # # # MOVIMENTO BOLA X ---------------------------------
        if ball.x <= 0:
            ball.x = 600
            ball_dir_x *= -1
        if ball.x >= 1280:
            ball.x = 600
            ball_dir_x *= -1

        ball.x += ball_dir_x
        ball.y += ball_dir_y

        # # # DESENHANDO NA TELA -------------------------------
        display.fill((0, 0, 0))
        display.blit(campo_img, campo)
        display.blit(player1_img, player1)
        display.blit(player2_img, player2)
        display.blit(ball_img, ball)
        display.blit(placar1, (440, 30))
        display.blit(placar2, (740, 30))
        display.blit(fade_img, fade)

    if cena == 'menu':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = False
                if event.key == pygame.K_SPACE:
                    score1 = 0
                    placar1 = font.render(str(score1), True, 'black')
                    score2 = 0
                    placar2 = font.render(str(score2), True, 'black')
                    player1.y = 0
                    player2.y = 0 
                    ball.x = 640
                    ball.y = 320
                    cena = 'multi'
                    fade_alpha = 255

                if event.key == pygame.K_RETURN:
                    score1 = 0
                    placar1 = font.render(str(score1), True, 'black')
                    player1.y = 0
                    player2.y = 0 
                    ball.x = 640
                    ball.y = 320
                    cena = 'single'
                    fade_alpha = 255

        if fade_alpha > 0:
            fade_alpha -= 9
            fade_img.set_alpha(fade_alpha)

        display.fill((0, 0, 0))
        display.blit(menu_img, menu_img.get_rect())      
        display.blit(fade_img, fade) 
    
    if cena == 'gameover':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    cena = 'menu'
                    fade_alpha = 255

        if fade_alpha > 0:
            fade_alpha -= 9
            fade_img.set_alpha(fade_alpha)

        
        display.fill((0, 0, 0))
        display.blit(gameover_img, gameover_img.get_rect())
        display.blit(fade_img, fade)
        
    if cena == 'gameover1':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    cena = 'menu'
                    fade_alpha = 255

        if fade_alpha > 0:
            fade_alpha -= 9
            fade_img.set_alpha(fade_alpha)

        
        display.fill((0, 0, 0))
        display.blit(gameover1, gameover1.get_rect())
        display.blit(fade_img, fade)

    if cena == 'gameover2':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    cena = 'menu'
                    fade_alpha = 255

        if fade_alpha > 0:
            fade_alpha -= 9
            fade_img.set_alpha(fade_alpha)

        
        display.fill((0, 0, 0))
        display.blit(gameover2, gameover2.get_rect())
        display.blit(fade_img, fade)

    fps.tick(60)
    pygame.display.flip()