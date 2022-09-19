import pygame

# Tennis court Class
class tennisCourt:
    def __init__(self):
        self.courtArea_x_m = 11
        self.courtArea_y_m = 24
        self.netStartPosition = [0,self.courtArea_y_m/2]
        self.netEndPosition_= [self.courtArea_x_m, self.courtArea_y_m/2]
        self.courtColor = pygame.Color(94, 214, 39)

# Tennis balls' basket Class
class ballsBasket:
    def __init__(self):
        self.basketSize_x_m = 0.5
        self.basketSize_y_m = 0.5
        self.basketSize_h_m = 0.5
        self.basketColor = pygame.Color(0, 0, 0)
        self.basketCapacity = (self.basketSize_x_m * self.basketSize_y_m)*self.basketSize_h_m
        self.basketPosition = []

# Tennis balls Class
class tennisBall:
    def __init__(self):
        self.ballSize_x_m = 0.025
        self.ballSize_y_m = 0.025
        self.ballColor = pygame.Color(247, 247, 5)
        self.ballPosition = []

# Ball's boy Class
class ballsBoy:
    def __init__(self):
        self.boyPosition = []
        self.boyColor = pygame.Color(232, 212, 176)

# Create instances
Court = tennisCourt()
Basket = ballsBasket()
Ball = tennisBall()
Boy = balssBoy()

print('Hello game')
