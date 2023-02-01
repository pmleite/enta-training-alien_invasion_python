import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:

    def __init__(self):
        
        pygame.init()
        self.settings = Settings()
        self.bg_image = pygame.image.load(self.settings.bg_image)
        self.screen   = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width  = self.screen.get_rect().width
        self.settings.screen_heigth = self.screen.get_rect().height
        pygame.display.set_caption(self.settings.caption)
        self.ship     = Ship(self)
        self.bullets  = pygame.sprite.Group()
        self.aliens   = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update(self)
            self.bullets.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("bateu")

    def _update_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)
        self._check_bullt_alien_collisons()


    def _check_bullt_alien_collisons(self):
        collisions = pygame.sprite.groupcollide(self.bullets,
                                                self.aliens,
                                                True,
                                                True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()


    def _check_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                # Inicia Movimento (Muda as flags para true) 
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)

                # Interrompe o movimento (Muda as flags para false)  
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False  
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False  

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x   = available_space_x // (2 * alien_width)

        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_heigth -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, 
                                   alien_width,
                                   row_number, 
                                   alien_height)

    def _create_alien(self, alien_number,
                            alien_width,
                            row_number,
                            alien_height):  
                              
            alien        = Alien(self)
            alien.x      = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
            self.aliens.add(alien)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        self.screen.blit(self.bg_image, (0,0))     
        self.ship.blitme() 

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.aliens.draw(self.screen) 

        pygame.display.flip()

    

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()



