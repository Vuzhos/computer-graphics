from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
W = 1600
H = 900

LOOK_AT = np.array([1, 1, 10.0, 0.0, 0.0, 0.0, 0.0, 1, 0.0])
rot_x=0.0
rot_y=0.0
rot_z=0.0
mouseOldX = 0
mouseOldY = 0

scene_number = 1

A = 1
B = 2
D = 5

def keyboard(key, _, __):
    global scene_number 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    if key == b'2': scene_number = 1
    elif key == b'3': scene_number = 2
    elif key == b'w': LOOK_AT[2] -= 0.1
    elif key == b's': LOOK_AT[2] += 0.1
    elif key == b'd': LOOK_AT[0] += 0.1
    elif key == b'a': LOOK_AT[0] -= 0.1
    
    if key in [b'w', b's', b'd', b'a', b'4', b'5', b'6']:
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        if key == b'4': glOrtho(-3.0, 3.0, -3.0, 3.0, 0.5, 25)
        elif key == b'5': gluPerspective(160, W / H, 0.5, 25)
        elif key == b'6': glFrustum(-1.0, 1.0, -1.0, 1.0, 0.5, 25)
        else: gluPerspective(120, W / H, 0.5, 25)
        gluLookAt(*LOOK_AT)
        glMatrixMode(GL_MODELVIEW)
    glutPostRedisplay()

def draw_table():
    glPushMatrix()
    glTranslate(0, -0.1, 0)
    glScalef(1, 0.1, 1)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(-0.45, -0.55, -0.45)
    glScalef(0.1, 1, 0.1)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.45, -0.55, -0.45)
    glScalef(0.1, 1, 0.1)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.45, -0.55, 0.45)
    glScalef(0.1, 1, 0.1)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(-0.45, -0.55, 0.45)
    glScalef(0.1, 1, 0.1)
    glutSolidCube(1)
    glPopMatrix()

def draw_teapot():
    glPushMatrix()
    glutSolidTeapot(0.1)
    glPopMatrix()

def draw_pen():
    glPushMatrix()
    glTranslate(0, -0.02, 0)
    glutSolidCylinder(0.02, 0.17, 200, 200)
    glPopMatrix()

def draw_book():
    glPushMatrix()
    glScale(0.3, 0.05, 0.2)
    glutSolidCube(1)
    glPopMatrix()

def scene_1():
    np.random.seed(1000)
    for i in range(3):
        #glPushMatrix()
        for j in range(4):
            glPushMatrix()
            glTranslate(2*i, 0, 2*j)
            
            glPushMatrix()
            glColor(131/255, 86/255, 62/255, 1)
            draw_table()
            glPopMatrix()
            
            glPushMatrix()
            glColor(76/255, 43/255, 32/255, 1)
            r = np.random.rand(3)-0.5
            r[1] = 0
            glTranslate(*r)
            draw_book()
            glPopMatrix()
            
            glPushMatrix()
            glColor(0, 0, 180/255, 1)
            r = np.random.rand(3) - 0.5
            r[1] = 0
            glTranslate(*r)
            draw_pen()
            glPopMatrix()
            
            glPushMatrix()
            glColor(139/255, 0, 0, 1)
            r = np.random.rand(3) - 0.5
            r[1] = 0
            glTranslate(*r)
            draw_teapot()
            glPopMatrix()

            glPopMatrix()

def scene_2():
    scene_1()
    phi = np.arctan2(B, A)
    
    glPushMatrix()
    glColor(1, 1, 1, 1)
    glLoadIdentity()
    glTranslate(-D / A, 0, 0)
    glRotate(-phi * 180 / np.pi, 0, 1, 0)
    glScalef(0.1, 1, 40)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glLoadIdentity()
    glColor(1, 1, 1, 1)
    glTranslate(-D / A, 0, 0)
    glRotate(-phi * 180 / np.pi, 0, 1, 0)
    glScale(-1, 1, 1)
    glRotate(phi * 180 / np.pi, 0, 1, 0)
    glTranslate(D/A, 0, 0)
    scene_1()
    glPopMatrix()
    
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    if scene_number == 1:
        scene_1()
    elif scene_number == 2:
        scene_2() 
    glFlush()
    glutSwapBuffers()

if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(W, H)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"lab3")

    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_FLAT)
    glEnable(GL_DEPTH_TEST)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(120, W / H, 0.5, 25)
    gluLookAt(*LOOK_AT)
    glMatrixMode(GL_MODELVIEW)
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMainLoop()
