import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

pygame.init()

display_width = 800
display_height =600
display = pygame.display.set_mode((display_width,display_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('3d transformation')

glClearColor(0.0,0.0,0.0,1.0)
glEnable(GL_DEPTH_TEST)
glMatrixMode(GL_PROJECTION)
gluPerspective(45,(display_width/display_height),0.1,50.0)
glMatrixMode(GL_MODELVIEW)

vertices = np.array([
    [-1,-1,-1],
    [1,-1,-1],
    [1,1,-1],
    [-1,1,-1],
    [-1,-1,1],
    [1,-1,1],
    [1,1,1],
    [-1,1,1]
],dtype=np.float32)

edges = np.array([
    [0,1],[1,2],[2,3],[3,0],
    [4,5],[5,6],[6,7],[7,4],
    [0,4],[1,5],[2,6],[3,7]
],dtype=np.uint32)

translation_matrix = np.eye(4, dtype=np.float32)
translation_matrix[3, :3] = [0,0,-5]
rotation_matrix = np.eye(4,dtype=np.float32)
scaling_matrix = np.eye(4, dtype= np.float32)
scaling_matrix[0,0] = 1.5
scaling_matrix[1,1] =1.5
scaling_matrix[2,2] =1.5

running = True
angle = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glMultMatrixf(translation_matrix)
    glRotate(angle,1,1,0)
    glMultMatrixf(rotation_matrix)
    glMultMatrixf(scaling_matrix)
    
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
    
    angle += 0.5
    
    pygame.display.flip()
    
pygame.quit()
