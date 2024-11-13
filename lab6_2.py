from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
W = 1600
H = 900

rot_x=0.0
rot_y=0.0
rot_z=0.0
mouseOldX = 0
mouseOldY = 0
LOOK_AT = np.array([1, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 1, 0.0])

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
    rot_z += ((mouseOldX - x) * 180.0) / 500.0    
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

points = np.array([
    [
        [2, -2, 0],
        [3, -1, 0],
        [3, 1, 0],
        [2, 2, 0]
    ],
    [
        [1, -3, 0],
        [2, -3, 5],
        [2, 3, 5],
        [1, 3, 0]
    ],
    [
        [-1, -3, 0],
        [-2, -3, 5],
        [-2, 3, 5],
        [-1, 3, 0]
    ],
    [
        [-2, -2, 0],
        [-3, -1, 0],
        [-3, 1, 0],
        [-2, 2, 0]
    ],
])

neg_points = np.array([-t for t in points])

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glPushMatrix()
    rotate()

    glColor(200/255, 30/255, 40/255, 0)
    glMap2f(GL_MAP2_VERTEX_3, 0, 1, 0, 1, points)
    glEnable(GL_MAP2_VERTEX_3)
    glMapGrid2f(20, 0.0, 1.0, 20, 0.0, 1.0)
    glEvalMesh2(GL_FILL, 0, 20, 0, 20)

    glColor(30/255, 40/255, 200/255, 0)
    glMap2f(GL_MAP2_VERTEX_3, 0, 1, 0, 1, neg_points)
    glEnable(GL_MAP2_VERTEX_3)
    glMapGrid2f(20, 0.0, 1.0, 20, 0.0, 1.0)
    glEvalMesh2(GL_FILL, 0, 20, 0, 20)
    glPopMatrix()
    
    glFlush()
    glutSwapBuffers()

if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_STENCIL | GLUT_DEPTH)
    glutInitWindowSize(W, H)
    glutCreateWindow(b'lab6')

    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, W / H, 1.0, 30.0)
    gluLookAt(*LOOK_AT)
    glMatrixMode(GL_MODELVIEW)
        
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_AUTO_NORMAL)
    
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(mouse)
    glutMotionFunc(motion)
    glutMainLoop()
