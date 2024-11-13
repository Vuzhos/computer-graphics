from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
W = 1600
H = 900

c = 4 / 3 * np.tan(np.pi / 8)

points = np.array([
    [-1, 0, 0],
    [-1, c, 0],
    [-c, 1, 0],
    [0, 1, 0],
    [c, 1, 0],
    [1, c, 0],
    [1, 0, 0]])

def display():
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glMap1f(GL_MAP1_VERTEX_3, 0.0, 1.0, points)
    glEnable(GL_MAP1_VERTEX_3)
    glColor(0, 0, 0, 0)
    glLineWidth(10)
    glBegin(GL_LINE_STRIP)
    glColor(0, 0, 0, 0)
    for i in range(31):
        glEvalCoord1f(i / 30.0)
    glEnd()

    glMap1f(GL_MAP1_VERTEX_3, 0.0, 1.0, -points)
    glEnable(GL_MAP1_VERTEX_3)
    glColor(0, 0, 0, 0)
    glBegin(GL_LINE_STRIP)

    for i in range(31):
        glEvalCoord1f(i / 30.0)
    glEnd()

    glPointSize(10.0)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POINTS)
    for i in range(7):
        glVertex3fv(points[i])
    for i in range(7):
        glVertex3fv(-points[i])
    glEnd()
    glFlush()

if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitWindowSize(W, H)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b'lab6')
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, W / H, 1.0, 30.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5.0)
    
    glClearColor(0.0, 0.0, 0.0, 0.0)
    
    glutDisplayFunc(display)
    glutMainLoop()
