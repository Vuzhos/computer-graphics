from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np
from PIL import Image
W = 1600
H = 900

mat_emission = GLfloat_3(0.5, 0.5, 0.5)

LOOK_AT = np.array([0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 1, 0.0])
rot_x=0.0
rot_y=0.0
rot_z=0.0
mouseOldX = 0
mouseOldY = 0

def scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    image = Image.open('brick.bmp')
    image_data = np.array(list(image.getdata()), np.uint8)
    texture_id = glGenTextures(1)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 4)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.size[0], image.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, image_data)
    image.close()
    
    glEnable(GL_TEXTURE_2D)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-0.5, -0.5, 0.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-0.5, 0.5, 0.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(0.5, 0.5, 0.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(0.5, -0.5, 0.0)
    glEnd()
    glDisable(GL_TEXTURE_2D)
    glFlush()
    glutSwapBuffers()

if __name__ == '__main__':
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_DOUBLE |  GLUT_RGB)
    glutInitWindowSize(W, H)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"lab4")

    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glMaterialfv(GL_FRONT, GL_EMISSION, mat_emission)
    glMatrixMode(GL_MODELVIEW)
    
    glutDisplayFunc(scene)
    glutMainLoop()
