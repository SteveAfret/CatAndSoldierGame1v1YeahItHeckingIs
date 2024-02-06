from pygame import *
from random import *

win_width = 900
win_height = 900

# 1
window = display.set_mode((win_width, win_height))
display.set_caption('Великая Игра Степана')
background = transform.scale(image.load('galaxy_2.jpg'), (win_width, win_height))


class GameSprite(sprite.Sprite):
    def __init__(self, picture, w, h, x, y):
        super().__init__()
        self.image = transform.scale(image.load(picture), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_xspeed, player_yspeed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.xspeed = player_xspeed
        self.yspeed = player_yspeed

    def update(self):
        if player.rect.x <= win_width - 80 and player.xspeed > 0 or player.rect.x >= 0 and player.xspeed < 0 or player2.rect.x <= win_width - 80 and player2.xspeed > 0 or player2.rect.x >= 0 and player2.xspeed < 0:
            self.rect.x += self.xspeed
        walls_touched = sprite.spritecollide(self, barriers, False)

        if self.xspeed > 0:
            for p in walls_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.xspeed < 0:
            for p in walls_touched:
                self.rect.left = max(self.rect.left, p.rect.right)

        if player.rect.y <= win_height - 105 and player.yspeed > 0 or player.rect.y >= 0 and player.yspeed < 0 or player2.rect.y <= win_height - 105 and player2.yspeed > 0 or player2.rect.y >= 0 and player2.yspeed < 0:
            self.rect.y += self.yspeed
        walls_touched = sprite.spritecollide(self, barriers, False)

        if self.yspeed > 0:
            for p in walls_touched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.yspeed < 0:
            for p in walls_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)
        if player.rect.x >= 820:
            player.rect.x = 820
        if player.rect.x <= 0:
            player.rect.x = 0
        if player2.rect.x >= 820:
            player2.rect.x = 820
        if player2.rect.x <= 0:
            player2.rect.x = 0
        if player.rect.y >= 795:
            player.rect.y = 795
        if player.rect.y <= 0:
            player.rect.y = 0
        if player2.rect.y >= 795:
            player2.rect.y = 795
        if player2.rect.y <= 0:
            player2.rect.y = 0


class Moveable(GameSprite):
    side = 'up'

    def __init__(self, picture, w, h, x, y, speed):
        GameSprite.__init__(self, picture, w, h, x, y)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def update(self):
        if ran == 1:
            if self.rect.y <= win_height - 888:
                self.side = 'down'
            if self.rect.y >= win_height - 512:
                self.side = 'up'
            if self.side == 'up':
                self.rect.y -= self.speed
            else:
                self.rect.y += self.speed
        elif ran == 2:
            if self.rect.y <= win_height - 666:
                self.side = 'down'
            if self.rect.y >= win_height - 525:
                self.side = 'up'
            if self.side == 'up':
                self.rect.y -= self.speed
            else:
                self.rect.y += self.speed
        elif ran == 3:
            if self.rect.y <= win_height - 900:
                self.side = 'down'
            if self.rect.y >= win_height - 300:
                self.side = 'up'
            if self.side == 'up':
                self.rect.y -= self.speed
            else:
                self.rect.y += self.speed
        elif ran == 4:
            if self.rect.y <= win_height - 900:
                self.side = 'down'
            if self.rect.y >= win_height - 500:
                self.side = 'up'
            if self.side == 'up':
                self.rect.y -= self.speed
            else:
                self.rect.y += self.speed
        elif ran == 5:
            if self.rect.y <= win_height - 900:
                self.side = 'down'
            if self.rect.y >= win_height - 500:
                self.side = 'up'
            if self.side == 'up':
                self.rect.y -= self.speed
            else:
                self.rect.y += self.speed


class Bullet(GameSprite):
    def __init__(self, image, w, h, x, y, speed):
        GameSprite.__init__(self, image, w, h, x, y)
        self.speed = speed
        self.visible = False

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > win_width + 10 or self.rect.x < win_width - 10:
            self.kill()

    def reset(self):
        if self.visible == True:
            super().reset()


v1 = 0
v2 = 0
Already = 0
FINAL_END = False
while FINAL_END == False:
    global ran
    ran = randint(1, 5)
    # ran = 5
    if ran == 1:
        player = Player('shutterstock_1220361823-[Converted]-2.png', 80, 105, 69, 420, 50, 50)
        player2 = Player('Asset 1@4x (1).png', 80, 105, 750, 420, 50, 50)
        # wall1 = GameSprite('wall1red.png', 40, 500, 460, 201)
        wall1 = Moveable('wall1red.png', 40, 500, 460, 201, 9)
        wall2 = GameSprite('wall2red.png', 320, 30, 318, 458)
        wall3 = wall2
        wall4 = wall1
        final = GameSprite('Asset 25@4x.png', 45, 45, 850, 460)
        final2 = GameSprite('Asset 18@4x.png', 40, 50, 15, 460)
        bulletcat = Bullet('bulletcat.png', 20, 5, 8888, 8888, 9)
        bulletsoldait = Bullet('bulletsoldait.png', 20, 5, 8888, 8888, 9)
        wall1.speed = 15
        wall4.speed = 15
    if ran == 2:
        player = Player('shutterstock_1220361823-[Converted]-2.png', 80, 105, 424, 20, 50, 50)
        player2 = Player('Asset 1@4x (1).png', 80, 105, 430, 760, 400, 50)
        # wall1 = GameSprite('wall1red.png', 40, 500, 460, 201)
        wall1 = Moveable('wall1blu.png', 30, 300, 190, 400, 9)
        wall2 = GameSprite('wall2blu.png', 800, 30, 0, 680)
        wall3 = GameSprite('wall2blu.png', 800, 30, 100, 200)
        wall4 = Moveable('wall1blu.png', 30, 300, 700, 200, 9)
        final = GameSprite('Asset 25@4x.png', 45, 35, 450, 800)
        final2 = GameSprite('Asset 18@4x.png', 40, 50, 450, 40)
        bulletcat = Bullet('bulletcat.png', 20, 5, 900, 900, 9)
        bulletsoldait = Bullet('bulletsoldait.png', 20, 5, 8888, 8888, 9)
        wall1.speed = 5
        wall4.speed = 5
    if ran == 3:
        player = Player('shutterstock_1220361823-[Converted]-2.png', 80, 105, 820, 800, 50, 50)
        player2 = Player('Asset 1@4x (1).png', 80, 105, 0, 0, 50, 50)
        # wall1 = GameSprite('wall1red.png', 40, 500, 460, 201)
        wall1 = Moveable('wall1red.png', 40, 300, 430, 600, 9)
        wall2 = GameSprite('wall2red.png', 444, 55, 0, 200)
        wall3 = GameSprite('wall2red.png', 444, 55, 456, 680)
        wall4 = Moveable('wall1red.png', 40, 300, 430, 0, 9)
        final = GameSprite('Asset 25@4x.png', 45, 45, 22, 35)
        final2 = GameSprite('Asset 18@4x.png', 40, 50, 845, 845)
        bulletcat = Bullet('bulletcat.png', 20, 5, 8888, 8888, 9)
        bulletsoldait = Bullet('bulletsoldait.png', 20, 5, 8888, 8888, 9)
        wall1.speed = 15
        wall4.speed = 15
    if ran == 4:
        player = Player('shutterstock_1220361823-[Converted]-2.png', 80, 105, 540, 420, 50, 50)
        player2 = Player('Asset 1@4x (1).png', 80, 105, 280, 420, 50, 50)
        # wall1 = GameSprite('wall1red.png', 40, 500, 460, 201)
        wall1 = Moveable('wall1blu.png', 40, 500, 430, 400, 9)
        wall2 = GameSprite('wall2blu.png', 444, 55, 230, 680)
        wall3 = GameSprite('wall2blu.png', 444, 55, 230, 200)
        wall4 = Moveable('wall1blu.png', 40, 500, 430, 0, 9)
        final = GameSprite('Asset 25@4x.png', 45, 45, 380, 460)
        final2 = GameSprite('Asset 18@4x.png', 40, 50, 480, 460)
        bulletcat = Bullet('bulletcat.png', 20, 5, 8888, 8888, 9)
        bulletsoldait = Bullet('bulletsoldait.png', 20, 5, 8888, 8888, 9)
        wall1.speed = 10
        wall4.speed = 10
    if ran == 5:
        player = Player('shutterstock_1220361823-[Converted]-2.png', 80, 105, 300, 300, 50, 50)
        player2 = Player('Asset 1@4x (1).png', 80, 105, 510, 300, 50, 50)
        # wall1 = GameSprite('wall1red.png', 40, 500, 460, 201)
        wall1 = Moveable('wall1red.png', 40, 500, 430, 201, 9)
        wall2 = GameSprite('wall2red.png', 320, 30, 290, 458)
        wall3 = GameSprite('wall2blu.png', 444, 55, 230, 200)
        wall4 = Moveable('wall1blu.png', 40, 500, 430, 0, 9)
        final = GameSprite('Asset 25@4x.png', 45, 45, 475, 335)
        final2 = GameSprite('Asset 18@4x.png', 40, 50, 380, 333)
        bulletcat = Bullet('bulletcat.png', 20, 5, 8888, 8888, 9)
        bulletsoldait = Bullet('bulletsoldait.png', 20, 5, 8888, 8888, 9)
        wall1.speed = 8
        wall4.speed = 8

    barriers = sprite.Group()
    barriers.add(wall1)
    barriers.add(wall2)
    barriers.add(wall3)
    barriers.add(wall4)
    bullets = sprite.Group()
    bullets.add(bulletcat)
    bullets.add(bulletsoldait)
    players = sprite.Group()
    players.add(player)
    players.add(player2)

    game = True
    bulletcat.speed = 0
    bulletsoldait.speed = 0
    player.yspeed = 0.00001
    player.xspeed = 0.00001
    player2.yspeed = 0.00001
    player2.xspeed = 0.00001
    finish = False

    if Already != 1:
        img = image.load('ПРАВИЛА.png')
        window.blit(background, (0, 0))
        window.fill((255, 255, 255))
        window.blit(transform.scale(img, (win_width, win_height)), (0, 0))
        display.update()
        time.delay(12345)
    while game:
        time.delay(50)
        for e in event.get():
            if e.type == QUIT:
                game = False
                FINAL_END = True
            elif e.type == KEYDOWN:
                if e.key == K_UP:
                    player2.yspeed = -15
                elif e.key == K_RIGHT:
                    player2.xspeed = 10
                elif e.key == K_LEFT:
                    player2.xspeed = -15
                elif e.key == K_DOWN:
                    player2.yspeed = 15
                elif e.key == K_w:
                    player.yspeed = -15
                elif e.key == K_d:
                    player.xspeed = 15
                elif e.key == K_a:
                    player.xspeed = -10
                elif e.key == K_s:
                    player.yspeed = 15
                elif e.key == K_RETURN:
                    if bulletsoldait.visible == False:
                        bulletsoldait.reset()
                        bulletsoldait.rect.x = player2.rect.x + 30
                        bulletsoldait.rect.y = player2.rect.y + 70
                        bulletsoldait.visible = True
                        bulletsoldait.speed = -20
                elif e.key == K_e:
                    collidebulletcat = 1
                    if bulletcat.visible == False:
                        bulletcat.reset()
                        bulletcat.rect.x = player.rect.x + 36
                        bulletcat.rect.y = player.rect.y + 60
                        bulletcat.visible = True
                        bulletcat.speed = 20


            elif e.type == KEYUP:
                if e.key == K_UP:
                    player2.yspeed = 0.00001
                elif e.key == K_RIGHT:
                    player2.xspeed = 0.00001
                elif e.key == K_LEFT:
                    player2.xspeed = 0.00001
                elif e.key == K_DOWN:
                    player2.yspeed = 0.00001
                elif e.key == K_w:
                    player.yspeed = 0.00001
                elif e.key == K_d:
                    player.xspeed = 0.00001
                elif e.key == K_a:
                    player.xspeed = 0.00001
                elif e.key == K_s:
                    player.yspeed = 0.0001

            if not finish:
                barriers.draw(window)
                bullets.draw(window)
                if sprite.collide_rect(player2, bulletcat):
                    finish = True
                    img = image.load('winner_1.jpg')
                    window.blit(background, (0, 0))
                    window.fill((255, 255, 255))
                    window.blit(transform.scale(img, (win_width, win_height)), (0, 0))
                if sprite.collide_rect(player, bulletsoldait):
                    finish = True
                    img = image.load('winner_2.jpg')
                    window.blit(background, (0, 0))
                    window.fill((255, 255, 255))
                    window.blit(transform.scale(img, (win_width, win_height)), (0, 0))
                if sprite.collide_rect(bulletcat, wall3) or sprite.collide_rect(bulletcat,
                                                                                wall4) or sprite.collide_rect(bulletcat,
                                                                                                              wall1) or sprite.collide_rect(
                        bulletcat, wall2) or bulletcat.rect.x >= win_width:
                    bulletcat.visible = False
                    bulletcat.speed = 0
                if sprite.collide_rect(bulletsoldait, wall3) or sprite.collide_rect(bulletsoldait,
                                                                                    wall4) or sprite.collide_rect(
                        bulletsoldait, wall1) or sprite.collide_rect(bulletsoldait, wall2) or bulletsoldait.rect.x <= 0:
                    bulletsoldait.visible = False
                    bulletsoldait.speed = 0
                if sprite.collide_rect(player, player2):
                    finish = True
                    img = image.load('fail_1.jpg')
                    window.fill((255, 255, 255))
                    window.blit(background, (0, 0))
                    window.blit(transform.scale(img, (win_width, win_height)), (0, 0))
                if sprite.collide_rect(player, final):
                    finish = True
                    img = image.load('winner_1.jpg')
                    window.blit(background, (0, 0))
                    window.fill((255, 255, 255))
                    window.blit(transform.scale(img, (win_width, win_height)), (0, 0))
                if sprite.collide_rect(player2, final2):
                    finish = True
                    img = image.load('winner_2.jpg')
                    window.blit(background, (0, 0))
                    window.fill((255, 255, 255))
                    window.blit(transform.scale(img, (win_width, win_height)), (0, 0))
        bulletcat.update()
        bulletsoldait.update()
        display.update()
        display.update()
        player.update()
        player2.update()
        wall1.update()
        wall4.update()
        if sprite.collide_rect(player2, bulletcat):
            finish = True
            v1 += 1
            img = image.load('winner_1.jpg')
            window.blit(background, (0, 0))
            window.fill((255, 255, 255))
            window.blit(transform.scale(img, (win_width, win_height)), (0, 0))
        if sprite.collide_rect(player, bulletsoldait):
            finish = True
            v2 += 1
            img = image.load('winner_2.jpg')
            window.blit(background, (0, 0))
            window.fill((255, 255, 255))
            window.blit(transform.scale(img, (win_width, win_height)), (0, 0))
        if sprite.collide_rect(bulletcat, wall3) or sprite.collide_rect(bulletcat, wall4) or sprite.collide_rect(
                bulletcat, wall1) or sprite.collide_rect(bulletcat, wall2):
            bulletcat.visible = False
            bulletcat.speed = 0
        if sprite.collide_rect(bulletsoldait, wall3) or sprite.collide_rect(bulletsoldait,
                                                                            wall4) or sprite.collide_rect(bulletsoldait,
                                                                                                          wall1) or sprite.collide_rect(
                bulletsoldait, wall2):
            bulletsoldait.visible = False
            bulletsoldait.speed = 0
        if finish != True:
            window.blit(background, (0, 0))
            bulletcat.reset()
            bulletsoldait.reset()
            player.reset()
            player2.reset()
            wall1.reset()
            wall2.reset()
            wall3.reset()
            wall4.reset()
            final.reset()
            final2.reset()
        if finish == True:
            print('Кот:', v1, 'Солдат:', v2)
            display.update()
            bulletcat = Bullet('bulletcat.png', 20, 5, 8888, 8888, 9)
            bulletsoldait = Bullet('bulletsoldait.png', 20, 5, 8888, 8888, 9)
            time.delay(4321)
            Already = 1
            finish = False
            break