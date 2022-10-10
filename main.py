import pygame
import random

# Scale factor
scale = 28

# Number of balls
ballsAmount = 25

# Tennis court Class
class tennisCourt:
    def __init__(self):
        self.courtArea_x_m = 11
        self.courtArea_y_m = 24
        self.courtColor = pygame.Color(134, 210, 111)
        self.netColor = pygame.Color(0, 0, 0)
        self.netStartPosition = [0, self.courtArea_y_m/2]
        self.netEndPosition = [self.courtArea_x_m, self.courtArea_y_m/2]
        self.netThickness = 3


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
        self.ballSize_x_m = 0.066
        self.ballSize_y_m = 0.066
        self.ballColor = pygame.Color(247, 247, 5)
        self.ballPosition = []

# Ball's boy Class
class ballsBoy:
    def __init__(self):
        self.boyPosition = []
        self.boyColor = pygame.Color(232, 212, 176)

# Init game
pygame.init()

# Create instances
Court = tennisCourt()
Basket = ballsBasket()
Ball = tennisBall()
Boy = ballsBoy()
ballsList = []

# Defining window size
window_x = Court.courtArea_x_m * scale
window_y = Court.courtArea_y_m * scale

# Displaying game window
courtWindow = pygame.display.set_mode((window_x, window_y))
courtWindow.fill(Court.courtColor)

# Displaying net
pygame.draw.rect(courtWindow, Court.netColor, pygame.Rect(
    Court.netStartPosition[0] * scale, Court.netStartPosition[1] * scale, Court.netEndPosition[1] * scale, Court.netThickness))

# Generating and displaying balls
for i in range(ballsAmount):
    ballsList.append(tennisBall())
    ballsList[-1].ballPosition = [random.randrange(0, window_x), random.randrange(0, window_y)]
    pygame.draw.circle(courtWindow, Ball.ballColor, ballsList[-1].ballPosition, Ball.ballSize_x_m*scale*2)

while True:
    pygame.display.update()




