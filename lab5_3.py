from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
W = 1600
H = 900

m_x = -0.5
m_y = 0.0
m_z = 4.0

LOOK_AT = np.array([0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0])
rot_x=0.0
rot_y=0.0
rot_z=0.0
mouseOldX = 0
mouseOldY = 0

def keyboard(key, _, __):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    if key == b'w': LOOK_AT[2] -= 0.1
    elif key == b's': LOOK_AT[2] += 0.1
    elif key == b'd': LOOK_AT[0] += 0.1
    elif key == b'a': LOOK_AT[0] -= 0.1
    
    if key in [b'w', b's', b'd', b'a']:
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60.0, W / H, 1.0, 30.0)
        gluLookAt(*LOOK_AT)
        glMatrixMode(GL_MODELVIEW)
    glutPostRedisplay()

def motion(x, y):
    global rot_x, rot_y, rot_z, mouseOldY, mouseOldX
    rot_x -= ((mouseOldY - y) * 180.0) / 500.0
    rot_y += 0
    rot_z -= ((mouseOldX - x) * 180.0) / 500.0    
    if (rot_x > 360): rot_x -= 360
    if (rot_x < -360): rot_x += 360
    if (rot_y > 360): rot_y -= 360
    if (rot_y < -360): rot_y += 360
    if (rot_z > 360): rot_z -= 360
    if (rot_z < -360): rot_z += 360
    mouseOldX = x
    mouseOldY = y
    glutPostRedisplay()

def mouse(button, state, x, y):
    if state == GLUT_DOWN:
        mouseOldX = x
        mouseOldY = y
        
def rotate():
    glRotatef(rot_x, 1.0, 0.0, 0.0)
    glRotatef(rot_y, 0.0, 1.0, 0.0)
    glRotatef(rot_z, 0.0, 0.0, 1.0)

def scene():
    glPushMatrix()
    glTranslatef(2.5, 0.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)
    glutSolidCube(1.0)
    glPopMatrix()

def mirror(type):
    glLineWidth(10)
    glBegin(type)
    n = 100
    for i in range(2*n):
        glVertex3f(m_x, m_y - np.sin(np.pi * i / n), m_z - 2 * np.cos(np.pi * i / n))
    glEnd()

def display():
    glClearStencil(0)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -7.0)
    rotate()

    glClear(GL_STENCIL_BUFFER_BIT)
    glStencilFunc(GL_ALWAYS, 1, 1)
    glStencilOp(GL_REPLACE, GL_REPLACE, GL_REPLACE)
    mirror(GL_TRIANGLE_FAN)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glColor3f(0, 0, 0)
    mirror(GL_LINE_LOOP)

    glStencilOp(GL_KEEP, GL_KEEP, GL_KEEP)
    glStencilFunc(GL_NOTEQUAL, 1, 1)
    scene()

    glStencilFunc(GL_EQUAL, 1, 1)
    glTranslatef(m_x, m_y, m_z)
    glScalef(-1.0, 1.0, 1.0)
    glTranslatef(-m_x, -m_y, -m_z)
    scene()

    glutSwapBuffers()

if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_STENCIL | GLUT_DEPTH)
    glutInitWindowSize(W, H)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b'lab5')
    
    glClearColor(1, 1, 1, 0.0)
    glEnable(GL_STENCIL_TEST)
    glEnable(GL_DEPTH_TEST)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, W / H, 1.0, 30.0)
    glMatrixMode(GL_MODELVIEW)
    
    
    
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(mouse)
    glutMotionFunc(motion)
    glutMainLoop()
