# Level management for UFO game

import pygame
import random
from platforms import Platform
from enemies import Enemy
from powerup import PowerUp
from flag import Flag

class Level:
    def __init__(self, screen_width, screen_height, level_num=1):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.level_num = level_num
        self.platforms = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.power_ups = pygame.sprite.Group()
        self.flags = pygame.sprite.Group()
        self.camera_x = 0
        self.level_width = screen_width * 3
        self.setup_level()
    
    def setup_level(self):
        # clear any previous sprites (safe re-use)
        self.platforms.empty()
        self.enemies.empty()
        self.power_ups.empty()
        self.flags.empty()

        if self.level_num == 1:
            self.setup_level_1()
        elif self.level_num == 2:
            self.setup_level_2()
        elif self.level_num == 3:
            # easier custom layout for level 3
            self.setup_level_3_easy()
        else:
            self.setup_generated_level(self.level_num)
    
    def setup_level_1(self):
        # Screen 1 (x: 0-800)
        self.platforms.add(Platform(0, 550, 800, 50))
        self.platforms.add(Platform(100, 450, 150, 20))
        self.platforms.add(Platform(400, 400, 150, 20))
        self.platforms.add(Platform(200, 300, 150, 20))
        
        self.enemies.add(Enemy(300, 500))
        self.enemies.add(Enemy(600, 450))
        self.power_ups.add(PowerUp(400, 360))
        
        # Screen 2 (x: 800-1600)
        self.platforms.add(Platform(800, 550, 800, 50))
        self.platforms.add(Platform(900, 450, 150, 20))
        self.platforms.add(Platform(1100, 380, 150, 20))
        self.platforms.add(Platform(1300, 300, 150, 20))
        self.platforms.add(Platform(1500, 350, 150, 20))
        
        self.enemies.add(Enemy(1000, 500))
        self.enemies.add(Enemy(1400, 400))
        self.power_ups.add(PowerUp(1100, 340))
        
        # Screen 3 (x: 1600-2400)
        self.platforms.add(Platform(1600, 550, 800, 50))
        self.platforms.add(Platform(1700, 450, 150, 20))
        self.platforms.add(Platform(1900, 350, 150, 20))
        self.platforms.add(Platform(2100, 280, 150, 20))
        self.platforms.add(Platform(2300, 400, 150, 20))
        
        self.enemies.add(Enemy(1800, 500))
        self.enemies.add(Enemy(2200, 400))
        self.flags.add(Flag(2350, 480))
    
    def setup_level_2(self):
        # Screen 1 (x: 0-800)
        self.platforms.add(Platform(0, 550, 800, 50))
        self.platforms.add(Platform(150, 480, 120, 20))
        self.platforms.add(Platform(350, 420, 120, 20))
        self.platforms.add(Platform(550, 360, 120, 20))
        
        self.enemies.add(Enemy(250, 500))
        self.enemies.add(Enemy(700, 450))
        self.enemies.add(Enemy(450, 380))
        self.power_ups.add(PowerUp(550, 320))
        
        # Screen 2 (x: 800-1600)
        self.platforms.add(Platform(800, 550, 800, 50))
        self.platforms.add(Platform(850, 450, 120, 20))
        self.platforms.add(Platform(1050, 380, 120, 20))
        self.platforms.add(Platform(1250, 300, 120, 20))
        self.platforms.add(Platform(1450, 380, 120, 20))
        
        self.enemies.add(Enemy(950, 500))
        self.enemies.add(Enemy(1150, 400))
        self.enemies.add(Enemy(1550, 420))
        self.power_ups.add(PowerUp(1250, 260))
        
        # Screen 3 (x: 1600-2400)
        self.platforms.add(Platform(1600, 550, 800, 50))
        self.platforms.add(Platform(1650, 480, 120, 20))
        self.platforms.add(Platform(1850, 400, 120, 20))
        self.platforms.add(Platform(2050, 320, 120, 20))
        self.platforms.add(Platform(2250, 380, 120, 20))
        
        self.enemies.add(Enemy(1750, 500))
        self.enemies.add(Enemy(1950, 420))
        self.enemies.add(Enemy(2150, 340))
        self.enemies.add(Enemy(2350, 400))
        self.power_ups.add(PowerUp(2050, 280))
        self.flags.add(Flag(2350, 480))
    
    def setup_level_3_easy(self):
        # easier progression across three screens
        ground_y = 550
        # wide ground across full level width
        self.platforms.add(Platform(0, ground_y, self.level_width, 50))

        # Gentle, closely spaced platforms to help the player
        easy_platforms = [
            (100, 480, 180), (320, 430, 180), (540, 380, 180),
            (860, 480, 180), (1080, 430, 180), (1300, 380, 180),
            (1660, 480, 180), (1880, 430, 180), (2100, 380, 180)
        ]
        for x, y, w in easy_platforms:
            self.platforms.add(Platform(x, y, w, 20))

        # Very few enemies (one per screen) and placed away from tricky gaps
        self.enemies.add(Enemy(600, ground_y - 50))
        self.enemies.add(Enemy(1400, ground_y - 50))
        self.enemies.add(Enemy(2000, ground_y - 50))

        # More power-ups to ease difficulty
        self.power_ups.add(PowerUp(500, 340))
        self.power_ups.add(PowerUp(1200, 340))
        self.power_ups.add(PowerUp(1800, 340))

        # Flag near the far right but not too punishing
        self.flags.add(Flag(self.level_width - 100, ground_y - 70))
    
    def setup_generated_level(self, lvl):
        # Deterministic randomness per level
        random.seed(lvl)
        ground_y = 550
        
        # Ground covering all three screens
        self.platforms.add(Platform(0, ground_y, self.level_width, 50))
        
        # Scatter platforms across the level_width
        num_platforms = 8 + (lvl % 5)  # slight variance
        for i in range(num_platforms):
            w = random.choice([80, 120, 150])
            x = random.randint(50, self.level_width - 200)
            y = random.randint(220, ground_y - 120)
            self.platforms.add(Platform(x, y, w, 20))
        
        # Spawn enemies scaled by level
        num_enemies = 3 + (lvl // 2)
        for i in range(num_enemies):
            ex = random.randint(100, self.level_width - 100)
            ey = ground_y - 50
            self.enemies.add(Enemy(ex, ey))
        
        # Place a few power-ups
        num_pu = max(1, (lvl // 3))
        for i in range(num_pu):
            px = random.randint(120, self.level_width - 200)
            py = random.randint(200, ground_y - 140)
            self.power_ups.add(PowerUp(px, py))
        
        # Flag at the far right end of the level
        self.flags.add(Flag(self.level_width - 50, ground_y - 70))
    
    def update_camera(self, player):
        self.camera_x = player.rect.centerx - self.screen_width // 3
        self.camera_x = max(0, min(self.camera_x, self.level_width - self.screen_width))
    
    def get_offset(self):
        return -self.camera_x
    
    def update(self):
        self.platforms.update()
        self.enemies.update()
        self.power_ups.update()
        self.flags.update()
