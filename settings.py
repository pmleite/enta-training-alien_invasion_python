class Settings:

    def __init__(self):
        self.screen_width  = 0
        self.screen_heigth = 0
        self.bg_image      = "images/background.jpg"
        self.alien_image   = "images/alien.png"
        self.ship_image    = "images/ship.png"
        self.caption       = "Alien Invasion by Paulo Leite"
        self.ship_speed    = 0.8

        self.bullet_speed    = 1.0
        self.bullet_width    = 3
        self.bullet_height   = 15
        self.bullet_color    = (83,220,83)
        self.bullets_allowed = 10

        self.alien_speed      = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction  = 1
 
