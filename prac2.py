import pygame
import sys
import math

pygame.init()
WIDTH,HEIGHT=800,600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("2D Transformation")

WHITE=(255,255,255)
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)


Clock=pygame.time.Clock()

shape_width,shape_height=100,60
original_shape=pygame.Surface((shape_width,shape_height))
original_shape.fill(RED)

angle=0
scale_factor=1.0
position=[350,270]

running=True
while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

        scale_shape=pygame.transform.scale(original_shape,(int(shape_width*scale_factor),int(shape_height*scale_factor)))
        rotate_shape=pygame.transform.rotate(scale_shape,angle)
        rect=rotate_shape.get_rect(center=(position[0],position[1]))
        screen.blit(rotate_shape,rect)

        angle+=1
        scale_factor+=0.005
        if scale_factor>2:
            scale_factor=1.0

        pygame.draw.rect(screen,BLUE,(50,50,shape_width,shape_height),2)
        pygame.display.flip()
        Clock.tick(60)

pygame.quit()
sys.exit()








        
