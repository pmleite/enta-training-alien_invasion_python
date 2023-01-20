import sys
import pygame
from settings import Settings
from ship import Ship

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

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update(self)
            self._update_screen()
            

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
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False  
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False  

    def _update_screen(self):
            self.screen.blit(self.bg_image, (0,0))     
            self.ship.blitme()   
            pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()



