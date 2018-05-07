import csv
import random
import math
import fit_eval
import puzzle_generate
import triangle_rotation as t_rot
#global variables

def cross(parent1_corner,parent1_sides,parent1_inner,\
        parent2_corner,parent2_sides,parent2_inner,color,layers):

    child1 = []
    child2 = []
    p1_corner_pos = []
    p1_sides_pos=[]
    p1_inner_pos=[]

    p2_corner_pos = []
    p2_sides_pos=[]
    p2_inner_pos=[]

    c1_corner_pos = []
    c1_sides_pos=[]
    c1_inner_pos=[]

    c2_corner_pos = []
    c2_sides_pos=[]
    c2_inner_pos=[]


    split1 = random.randint(0,2)
    split2 = random.randint(0,2)

    if split1 > split2:
        split1+=split2
        split2=split1-split2
        split1=split1-split2
    split2 = split2 + 1

    c1_corner = generate_children(parent1_corner[:],parent2_corner[:],split1,split2)
    c2_corner = generate_children(parent2_corner[:],parent1_corner[:],split1,split2)


    split1 = random.randint(0,len(parent1_sides)-1)
    split2 = random.randint(0,len(parent2_sides)-1)

    if split1 > split2:
        split1+=split2
        split2=split1-split2
        split1=split1-split2
    split2 = split2 + 1

    c1_sides = generate_children(parent1_sides[:],parent2_sides[:],split1,split2)
    c2_sides = generate_children(parent2_sides[:],parent1_sides[:],split1,split2)



    split1 = random.randint(0,len(parent1_inner)-1)
    split2 = random.randint(0,len(parent2_inner)-1)

    if split1 > split2:
        split1+=split2
        split2=split1-split2
        split1=split1-split2
    split2 = split2 + 1

    c1_inner = generate_children(parent1_inner[:],parent2_inner[:],split1,split2)
    c2_inner = generate_children(parent2_inner[:],parent1_inner[:],split1,split2)


    return c1_corner,c1_sides,c1_inner, \
    c2_corner,c2_sides,c2_inner


def generate_children(p1,p2,x,y):
    child = []
    region = p2[x:y]

    #print "parent 1",p1
    #print "parent 2",p2
    #print x,y,region
    p = 0
    for i in region:
        i1 = t_rot.rotate(i[:],1)
        i2 = t_rot.rotate(i[:],2)
        if i in p1:
            p1.remove(i)
        elif i1 in p1:
            p1.remove(i1)
        elif i2 in p1:
            p1.remove (i2)

    for i in range(0,x):
        child.append(p1[i])
        p+=1

    for i in range(0,len(region)):
        child.append(region[i])

    if len(child)<len(p2):
        for i in range(p,len(p1)):
            child.append(p1[i])

    #print "child",child

    return child
