from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from itertools import product
W = 1600
H = 900

LOOK_AT = np.array([2.0, 3.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0])
rot_x=0.0
rot_y=0.0
rot_z=0.0
mouseOldX = 0
mouseOldY = 0

light_position = GLdouble_4(-1.0, 3.0, 5.0, 0.0)
example_color = GLdouble_4(0.0, 0.0, 1.0, 1.0)

def keyboard(key, _, __):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    if key == b'1':
        set_specular_light()
        set_specular_material()
    elif key == b'2':
        set_diffuse_light()
        set_specular_material()
    elif key == b'3':
        set_specular_light()
        set_diffuse_material()
    elif key == b'4':
        set_diffuse_light()
        set_diffuse_material()
    elif key == b'5':
        set_default_material()
    glutPostRedisplay()

def motion(x, y):
    global rot_x, rot_y, rot_z, mouseOldY, mouseOldX
    rot_x -= 0
    rot_y += ((mouseOldY - y) * 180.0) / 500.0
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

def set_default_material():
    mat_dif = GLdouble_3(0.0, 0.2, 0.0)
    mat_amb = GLdouble_3(0.2, 0.2, 0.2)
    mat_spec = GLdouble_3(0.6, 0.6, 0.6)
    mat_shininess = 0.1 * 128

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_amb)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_dif)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_spec)
    glMaterialf(GL_FRONT, GL_SHININESS, mat_shininess)
    
    #mat_emission = GLdouble_4(0.1, 200.0, 0.0, 1.0 )
    #glMaterialfv(GL_FRONT, GL_EMISSION, mat_emission)

def set_specular_material():
    mat_dif= GLdouble_3(0.0, 0.0, 0.0)
    mat_amb= GLdouble_3(0.2, 0.2, 0.2)
    mat_spec= GLdouble_3(1.0, 1.0, 1.0)
    mat_shininess = 0.1 * 128
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_amb)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_dif)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_spec)
    glMaterialf(GL_FRONT, GL_SHININESS, mat_shininess)


def set_diffuse_material():
    mat_dif= GLdouble_3(1.0, 1.0, 1.0)
    mat_amb= GLdouble_3(0.2, 0.2, 0.2)
    mat_spec= GLdouble_3(0.0, 0.0, 0.0)
    mat_shininess = 0.1 * 128

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_amb)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_dif)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_spec)
    glMaterialf(GL_FRONT, GL_SHININESS, mat_shininess)


def set_specular_light():
    light_ambient= GLdouble_4(0.0, 0.0, 0.0, 1.0)
    light_diffuse= GLdouble_4(0.0, 0.0, 0.0, 1.0)
    light_specular= GLdouble_4(1.0, 1.0, 1.0, 1.0)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

def set_diffuse_light():
    light_ambient= GLdouble_4(0.0, 0.0, 0.0, 1.0)
    light_diffuse= GLdouble_4(1.0, 1.0, 1.0, 1.0)
    light_specular= GLdouble_4(0.0, 0.0, 0.0, 1.0)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

def draw_cube():
    glPushMatrix()
    glBegin(GL_QUADS)
    glNormal3d(0, 1, 0)
    glVertex3d(0, 1, 0)
    glVertex3d(1.0, 1.0, 0.0)
    glVertex3d(1.0, 1.0, 1.0)
    glVertex3d(0.0, 1.0, 1.0)
    glEnd()

    glBegin(GL_QUADS)
    glNormal3d(0, -1, 0)
    glVertex3d(0, 0, 0)
    glVertex3d(1.0, 0.0, 0.0)
    glVertex3d(1.0, 0.0, 1.0)
    glVertex3d(0.0, 0.0, 1.0)
    glEnd()

    glBegin(GL_QUADS)
    glNormal3d(-1, 0, 0)
    glVertex3d(0, 0, 0)
    glVertex3d(0.0, 1.0, 0.0)
    glVertex3d(0.0, 1.0, 1.0)
    glVertex3d(0.0, 0.0, 1.0)
    glEnd()

    glBegin(GL_QUADS)
    glNormal3d(1, 0, 0)
    glVertex3d(1, 0, 0)
    glVertex3d(1.0, 1.0, 0.0)
    glVertex3d(1.0, 1.0, 1.0)
    glVertex3d(1.0, 0.0, 1.0)
    glEnd()

    glBegin(GL_QUADS)
    glNormal3d(0, 0, -1)
    glVertex3d(0, 0, 0)
    glVertex3d(1.0, 0.0, 0.0)
    glVertex3d(1.0, 1.0, 0.0)
    glVertex3d(0.0, 1.0, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glNormal3d(0, 0, 1)
    glVertex3d(0, 0, 1)
    glVertex3d(1.0, 0.0, 1.0)
    glVertex3d(1.0, 1.0, 1.0)
    glVertex3d(0.0, 1.0, 1.0)
    glEnd()
    glPopMatrix()
    
    # cube2
    diff = np.array([0, 2, 0])
    center = np.array([0.5, 0.5, 0.5]) + diff
    
    glPushMatrix()
    glBegin(GL_QUADS)
    v = np.array([0, 0, 0]) + diff
    glNormal3d(*((v - center)/sum(abs(v - center))))
    glVertex3d(*v)
    v = np.array([1, 0, 0]) + diff
    glNormal3d(*((v - center)/sum(abs(v - center))))
    glVertex3d(*v)
    v = np.array([1, 0, 1]) + diff
    glNormal3d(*((v - center)/sum(abs(v - center))))
    glVertex3d(*v)
    v = np.array([0.0, 0.0, 1.0]) + diff
    glNormal3d(*((v - center)/sum(abs(v - center))))
    glVertex3d(*v)
    glEnd()

    glBegin(GL_QUADS)
    v = np.array([0, 1, 0]) + diff
    glNormal3d(*((v - center)/sum(abs(v - center))))
    glVertex3d(*v)
    v = np.array([1, 1, 0]) + diff
    glNormal3d(*((v - center)/sum(abs(v - center))))
    glVertex3d(*v)
    v = np.array([1, 1, 1]) + diff
    glNormal3d(*((v - center)/sum(abs(v - center))))
    glVertex3d(*v)
    v = np.array([0.0, 1.0, 1.0]) + diff
    glNormal3d(*((v - center)/sum(abs(v - center))))
    glVertex3d(*v)
    glEnd()

    glBegin(GL_QUADS)
    v = np.array([0, 0, 0]) + diff
    glNormal3d(*((v - center)/sum(abs(v - center))))
    glVertex3d(*v)
    v = np.array([0, 1, 0]) + diff
    glNormal3d(*((v - center)/sum(abs(v - center))))
    glVertex3d(*v)
    v = np.array([0, 1, 1]) + diff
    glNormal3d(*((v - center)/sum(abs(v - center))))
    glVertex3d(*v)
    v = np.array([0.0, 0.0, 1.0]) + diff
    glNormal3d(*((v - center)/sum(abs(v - center))))
    glVertex3d(*v)
    glEnd()

    glBegin(GL_QUADS)
    v = np.array([1, 0, 0]) + diff
    glNormal3d(*((v - center)/sum(abs(v - center))))
    glVertex3d(*v)
    v = np.array([1, 1, 0]) + diff
    glNormal3d(*((v - center)/sum(abs(v - center))))
    glVertex3d(*v)
    v = np.array([1, 1, 1]) + diff
    glNormal3d(*((v - center)/sum(abs(v - center))))
    glVertex3d(*v)
    v = np.array([1.0, 0.0, 1.0]) + diff
    glNormal3d(*((v - center)/sum(abs(v - center))))
    glVertex3d(*v)
    glEnd()

    glBegin(GL_QUADS)
    v = np.array([0, 0, 0]) + diff
    glNormal3d(*((v - center)/sum(abs(v - center))))
    glVertex3d(*v)
    v = np.array([0, 1, 0]) + diff
    glNormal3d(*((v - center)/sum(abs(v - center))))
    glVertex3d(*v)
    v = np.array([1, 1, 0]) + diff
    glNormal3d(*((v - center)/sum(abs(v - center))))
    glVertex3d(*v)
    v = np.array([1.0, 0.0, 0.0]) + diff
    glNormal3d(*((v - center)/sum(abs(v - center))))
    glVertex3d(*v)
    glEnd()

    glBegin(GL_QUADS)
    v = np.array([0, 0, 1]) + diff
    glNormal3d(*((v - center)/sum(abs(v - center))))
    glVertex3d(*v)
    v = np.array([0, 1, 1]) + diff
    glNormal3d(*((v - center)/sum(abs(v - center))))
    glVertex3d(*v)
    v = np.array([1, 1, 1]) + diff
    glNormal3d(*((v - center)/sum(abs(v - center))))
    glVertex3d(*v)
    v = np.array([1.0, 0.0, 1.0]) + diff
    glNormal3d(*((v - center)/sum(abs(v - center))))
    glVertex3d(*v)
    glEnd()
    glPopMatrix()

def display ():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glColor(1, 200/255, 0)
    rotate()
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    draw_cube()
    glPopMatrix()
    glutSwapBuffers()



if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(W, H)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"lab2")
    
    light_ambient = GLfloat_4(0.0, 0.0, 0.0, 1.0) 
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient) 
    light_diffuse = GLfloat_4(1.0, 1.0, 1.0, 1.0) 
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse) 
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)   
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHT0) 
    glEnable(GL_LIGHTING)

    gluPerspective(120.0, W / H, 0.5, 25.0)
    gluLookAt(*LOOK_AT)
    
    glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_TRUE)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glutPostRedisplay()
    #glLightModelfv(GL_LIGHT_MODEL_AMBIENT, example_color)
    #glShadeModel(GL_FLAT) 
    
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(mouse)
    glutMotionFunc(motion)
    glutMainLoop()
