from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
W = 1600
H = 900

LOOK_AT = np.array([30, 20, 20, 0.0, 0.0, 0.0, 0.0, 1, 0.0])
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
        gluPerspective(60, W / H, 0.5, 50)
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

class ShadowObj:
    vertex = np.array([25, 25, 25, 25, 30, 30, 30, 30, 25])
    normal = np.array([1, -1, 1]) / np.sqrt(3)
    n = 0

shadow = ShadowObj()
light_pos = [50, 50, 50, 1]
sphere_mat = [1, 1, 1, 1]
obj_mat = [1, 1, 1, 1]

def extend(light, vertex, t):
    return light[:3] + (vertex - light[:3])*t

def make_shadow(obj, light, t, list_ind):
    glNewList(list_ind, GL_COMPILE)
    glDisable(GL_LIGHTING)
    glBegin(GL_QUADS)
    for i in range(obj.n):
        glVertex3fv(obj.vertex[i * 3:(i + 1) * 3])
        glVertex3fv(extend(light, obj.vertex[i * 3: (i + 1) * 3], t))
        glVertex3fv(extend(light, obj.vertex[((i + 1) % obj.n) * 3:((i + 1) % obj.n) * 3 + 3], t))
        glVertex3fv(obj.vertex[((i + 1) % obj.n) * 3: ((i + 1) % obj.n) * 3 + 3])
    glEnd()
    glEnable(GL_LIGHTING)
    glEndList()

def sphere():
    global sphere_mat
    glPushMatrix()
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, sphere_mat)
    glutSolidSphere(20.0, 200, 200)
    glPopMatrix()

def render(obj):
    global obj_mat
    sphere()
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, obj_mat)
    glBegin(GL_POLYGON)
    glNormal3fv(obj.normal)
    for i in range(obj.n):
        glVertex3fv(obj.vertex[3*i:3*(i+1)])
    glEnd()

def scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_STENCIL_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    rotate()
    
    glEnable(GL_STENCIL_TEST)
    glColorMask(GL_FALSE, GL_FALSE, GL_FALSE, GL_FALSE)
    glDepthMask(GL_FALSE)
    glStencilFunc(GL_ALWAYS, 1, 1)
    
    glStencilOp(GL_KEEP, GL_KEEP, GL_INCR)
    glCullFace(GL_FRONT)
    glCallList(1)
    glStencilOp(GL_KEEP, GL_KEEP, GL_DECR)
    glCullFace(GL_BACK)
    glCallList(1)

    glEnable(GL_LIGHT0)
    glColorMask(GL_TRUE, GL_TRUE, GL_TRUE, GL_TRUE)
    glDepthMask(GL_TRUE)
    glStencilFunc(GL_EQUAL, 0, 1)
    glStencilOp(GL_KEEP, GL_KEEP, GL_KEEP)
    glCullFace(GL_BACK)
    render(shadow)

    glDisable(GL_STENCIL_TEST)
    glutSwapBuffers()


if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH | GLUT_STENCIL | GLUT_DOUBLE)
    glutCreateWindow(b'lab5')
    glutMouseFunc(mouse)
    glutMotionFunc(motion)
    glutKeyboardFunc(keyboard)
    glutDisplayFunc(scene)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, W / H, 0.5, 50)
    gluLookAt(*LOOK_AT)
    glMatrixMode(GL_MODELVIEW)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_CULL_FACE)

    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
    shadow.n = len(shadow.vertex)//3
    make_shadow(shadow, light_pos, 100, 1)

    glutMainLoop()
