from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
from PIL import Image
from numpy import sin, cos, pi

W = 1600
H = 900

LOOK_AT = np.array([0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 1, 0.0])
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
        gluPerspective(120, W / H, 0.5, 25)
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
    
def scene(n=30, m=30, r=2):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_TEXTURE_2D)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    
    glPushMatrix()
    rotate()
    
    image = Image.open('brick.bmp')
    image_data = np.array(list(image.getdata()), np.uint8)
    texture_id = glGenTextures(1)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 4)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.size[0], image.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, image_data)
    image.close()
    
    for j in range(n):
        phi1 = j * (2 * pi) / n
        phi2 = (j + 1) * (2 * pi) / n
        glBegin(GL_QUAD_STRIP)
        for i in range(m + 1):
            theta = i * pi / n
            ex = sin(theta) * cos(phi2)
            ey = sin(theta) * sin(phi2)
            ez = cos(theta)
            s = phi2 / (2 * pi)
            t = 1 - theta / pi
            glTexCoord2f(4 * s, 4 * t)
            glVertex3f(r * ex, r * ey, r * ez)
            ex = sin(theta) * cos(phi1)
            ey = sin(theta) * sin(phi1)
            ez = cos(theta)
            s = phi1 / (2 * pi)
            t = 1 - theta / pi
            glTexCoord2f(4 * s, 4 * t)
            glVertex3f(r * ex, r * ey, r * ez)
        glEnd()
    glDisable(GL_TEXTURE_2D)
    glPopMatrix()
    
    glFlush()
    glutSwapBuffers()


if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(W, H)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"lab4")

    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(120.0, W / H, 0.5, 25.0)
    glMatrixMode(GL_MODELVIEW)
    glutDisplayFunc(scene)

    glutKeyboardFunc(keyboard)
    glutMouseFunc(mouse)
    glutMotionFunc(motion)
    glutMainLoop()
