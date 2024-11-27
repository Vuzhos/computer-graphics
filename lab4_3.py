from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
from PIL import Image
W = 1600
H = 900

rot_x=0.0
rot_y=0.0
rot_z=0.0
mouseOldX = 0
mouseOldY = 0
LOOK_AT = np.array([0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 1, 0.0])

def motion(x, y):
    global rot_x, rot_y, rot_z, mouseOldY, mouseOldX
    rot_x -= 0
    rot_y += ((mouseOldX - x) * 180.0) / 500.0 
    rot_z += ((mouseOldY - y) * 180.0) / 500.0
    if (rot_x > 360): rot_x -= 360
    if (rot_x < -360): rot_x += 360
    if (rot_y > 360): rot_y -= 360
    if (rot_y < -360): rot_y += 360
    if (rot_z > 360): rot_z -= 360
    if (rot_z < -360): rot_z += 360
    mouseOldX = x
    mouseOldY = y
    glutPostRedisplay ()

def mouse(button, state, x, y):
    if state == GLUT_DOWN:
        mouseOldX = x
        mouseOldY = y

def rotate():
    glRotatef(rot_x, 1.0, 0.0, 0.0)
    glRotatef(rot_y, 0.0, 1.0, 0.0)
    glRotatef(rot_z, 0.0, 0.0, 1.0)

def draw_scene():
    glDisable(GL_LIGHTING)
    glPushMatrix()
    glTranslatef(3, 0.5, 0.5)
    glRotatef(45, 1, 1, 1)

    image = Image.open('brick.bmp')
    image_data = np.array(list(image.getdata()), np.uint8)

    glGenTextures(2)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 4)
    glBindTexture(GL_TEXTURE_2D, 2)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.size[0], image.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, image_data)
    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR)
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)
    image.close()

    glutSolidCube(0.4)
    glPopMatrix()

    glBindTexture(GL_TEXTURE_2D, 1)
    
    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)
    
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glEnable(GL_LIGHTING)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, 0, 0, 5, 0, 0, 0, 0, 1)
    glScalef(1, -1, 1)
    rotate()
    draw_scene()
    glCopyTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, 0, 0, W, H, 0)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(5, 0, 0, 0, 0, 0, 0, 0, 1)
    rotate()
    draw_scene()
    glutSolidSphere(2.0, 20, 20)
    glFlush()
    glutSwapBuffers()


def reshape(w, h):
    global W, H
    W = w
    H = h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, float(w / h), 1.0, 30.0)
    glMatrixMode(GL_MODELVIEW)



if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(W, H)
    glutCreateWindow(b'lab4')
    
    glClearColor(1, 1, 1, 0.0)
    glEnable(GL_DEPTH_TEST)
    light_ambient = [0.1, 0.1, 0.1, 1.0]
    light_diffuse = [0.95, 0.95, 0.95, 1.0]
    light_position = [2.0, 2.0, 2.0, 0.0]

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_LIGHT0)
    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glEnable(GL_TEXTURE_2D)
    
    glutDisplayFunc(display)
    glutMouseFunc(mouse)
    glutMotionFunc(motion)
    glutReshapeFunc(reshape)
    glutMainLoop()
