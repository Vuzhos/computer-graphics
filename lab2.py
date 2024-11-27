from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from itertools import product

W = 800
H = 400

LOOK_AT = np.array([2, 3, 2, 0, 0, 0, 0, 0, 1])
rot_x=0
rot_y=0
rot_z=0
mouseOldX = 0
mouseOldY = 0

light_position = (5, 0, 5, 0)
example_color = (0, 0, 1, 1)

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
    rot_y += ((mouseOldY - y) * 180) / 500
    rot_z += ((mouseOldX - x) * 180) / 500    
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
    glRotatef(rot_x, 1, 0, 0)
    glRotatef(rot_y, 0, 1, 0)
    glRotatef(rot_z, 0, 0, 1)

def set_default_material():
    mat_dif = (0, 0, 0)
    mat_amb = (0.2, 0.2, 0.2)
    mat_spec = (0.6, 0.6, 0.6)
    mat_shininess = 0.1 * 128

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_amb)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_dif)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_spec)
    glMaterialf(GL_FRONT, GL_SHININESS, mat_shininess)
    
    

def set_specular_material():
    mat_dif= (0, 0, 0)
    mat_amb= (0, 0, 0)
    mat_spec= (1, 1, 1)
    mat_shininess = 0.1 * 128
    
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_amb)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_dif)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_spec)
    glMaterialf(GL_FRONT, GL_SHININESS, 1)
    
    #mat_emission = (01, 01, 0, 001 )
    #glMaterialfv(GL_FRONT, GL_EMISSION, mat_emission)


def set_diffuse_material():
    mat_dif= (1, 1, 1)
    mat_amb= (0, 0, 0)
    mat_spec= (0, 0, 0)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_amb)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_dif)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_spec)
    glMaterialf(GL_FRONT, GL_SHININESS, 1)


def set_specular_light():
    light_ambient= (0, 0, 0, 1)
    light_diffuse= (0, 0, 0, 1)
    light_specular= (1, 1, 1, 1)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

def set_diffuse_light():
    light_ambient= (0, 0, 0, 1)
    light_diffuse= (1, 1, 1, 1)
    light_specular= (0, 0, 0, 1)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

def draw_cube():
    glPushMatrix()
    glBegin(GL_QUADS)
    glNormal3d(0, 1, 0)
    glVertex3d(0, 1, 0)
    glVertex3d(1, 1, 0)
    glVertex3d(1, 1, 1)
    glVertex3d(0, 1, 1)
    glEnd()

    glBegin(GL_QUADS)
    glNormal3d(0, -1, 0)
    glVertex3d(0, 0, 0)
    glVertex3d(1, 0, 0)
    glVertex3d(1, 0, 1)
    glVertex3d(0, 0, 1)
    glEnd()

    glBegin(GL_QUADS)
    glNormal3d(-1, 0, 0)
    glVertex3d(0, 0, 0)
    glVertex3d(0, 1, 0)
    glVertex3d(0, 1, 1)
    glVertex3d(0, 0, 1)
    glEnd()

    glBegin(GL_QUADS)
    glNormal3d(1, 0, 0)
    glVertex3d(1, 0, 0)
    glVertex3d(1, 1, 0)
    glVertex3d(1, 1, 1)
    glVertex3d(1, 0, 1)
    glEnd()

    glBegin(GL_QUADS)
    glNormal3d(0, 0, -1)
    glVertex3d(0, 0, 0)
    glVertex3d(1, 0, 0)
    glVertex3d(1, 1, 0)
    glVertex3d(0, 1, 0)
    glEnd()

    glBegin(GL_QUADS)
    glNormal3d(0, 0, 1)
    glVertex3d(0, 0, 1)
    glVertex3d(1, 0, 1)
    glVertex3d(1, 1, 1)
    glVertex3d(0, 1, 1)
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
    v = np.array([0, 0, 1]) + diff
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
    v = np.array([0, 1, 1]) + diff
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
    v = np.array([0, 0, 1]) + diff
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
    v = np.array([1, 0, 1]) + diff
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
    v = np.array([1, 0, 0]) + diff
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
    v = np.array([1, 0, 1]) + diff
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
    
    light_ambient = GLfloat_4(1, 1, 1, 1) 
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient) 
    light_diff = GLfloat_4(1, 1, 1, 1) 
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diff) 
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)   
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHT0) 
    glEnable(GL_LIGHTING)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(120, W / H, 0.5, 25)
    gluLookAt(*LOOK_AT)
    glMatrixMode(GL_MODELVIEW)
    
    #glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_TRUE)
    #set_default_material()
    

    #glLightModelfv(GL_LIGHT_MODEL_AMBIENT, example_color)
    #glShadeModel(GL_FLAT) 
    
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(mouse)
    glutMotionFunc(motion)
    glutMainLoop()
