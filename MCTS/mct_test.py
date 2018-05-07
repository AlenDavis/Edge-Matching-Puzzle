import csv
import triangle_rotation as t_rot      ## rotate a triange in clockwise direction
import math
import puzzle_gen_improved_v02 as sim  ## generate the final puzzle
import fit_eval_v01 as fit_eval        ## evaluates fitness assigns -1 to all miss matched edge
import draw_puzzle_v01 as pd           ## draws the puzzle
import random
import time

################################################################################
## The puzzle if populated in the following way:
#                                  0
#                                1,2,3
#                              4,5,6,7,8
#                         9,10,11,12,13,14,15
################################################################################
#########
start_time = time.time()

# Global variables
color  = []
layers = 0                          # number of layers

full_corner = []
full_sides  = []
full_inner  = []
flag = True
N=1
######
## Each Piece is represented as an object with the following attributes: Parent,chilren,score,n and the value which is the color of the pieces
######
class Node:
    def __init__(self):
        self.parent   = 'NaN'
        self.children = []
        self.score    = 0
        self.n        = 1

        self.value    = []

## This function reads the input csv file
def get_pieces():
    inp_file = open("Untitled 3.csv")   #files 5 - 7 has 7 layers,4 has 6 layers,3 with 5 layers, and so on
    reader = csv.reader(inp_file,delimiter=',')
    for row in reader:
        color.append(row)

## This fucntion separate the piecces into corner,sides and inner
def group_pieces():
    for i in color:
        if i.count('0') == 2:
            full_corner.append(i)
        elif i.count('0') == 1:
            full_sides.append(i)
        else:
            full_inner.append(i)
            full_inner.append(t_rot.rotate(i,1)) #considers all possible
            full_inner.append(t_rot.rotate(i,2)) #combination of inner pieces



## This fucntion is used to find the remaining available inner,corner and side pieces at each nodes
def back_prop(i,parent,current_layer):

    r_corner = full_corner[:]
    r_inner  = full_inner[:]
    r_sides  = full_sides[:]

    temp_parent = parent

## The process continuosly finds the parent of the current node and compare the
## position of the each node, based on which they are deleted from the corners
## sidies and inner  list at the end of which we get the remaining corner, sides and
## inner at each node

    if len(parent.value) == 0:
        return r_corner,r_inner,r_sides
    for j in range(i,-1,-1):

            t1 = temp_parent.value
            if len(t1) == 0:
                continue
            t2 = t_rot.rotate(t1,1)
            t3 = t_rot.rotate(t1,2)


            if t1.count('0')==2:
                if t1 in r_corner:
                    r_corner.remove(t1)
                elif t2 in r_corner:
                    r_corner.remove(t2)
                elif t3 in r_corner:
                    r_corner.remove(t3)

            elif t1.count('0')==1:
                if t1 in r_sides:
                    r_sides.remove(t1)
                elif t2 in r_sides:
                    r_sides.remove(t2)
                elif t3 in r_sides:
                    r_sides.remove(t3)

            else :
                r_inner.remove(t1)
                r_inner.remove(t2)
                r_inner.remove(t3)

            temp_parent = temp_parent.parent

    return r_corner,r_inner,r_sides


##This function is used to populate children nodes to a parent node:
## To do this the position of the parent node is checked, to know exactly which piece is
## to be placed and a selected piece is compared with the remaining pieces at that node
## to see if there is a atleast a piece that can be placed after this node. This is
## done to limit the score of pieces at each node inorder to reduce wasteful processing
def populate_children(parent,i,root):
## Each node is compared with the respective postion in the layer
    current_layer = int(math.sqrt(i))

    r_corner,r_inner,r_sides = back_prop(i,parent,current_layer)

## For the first corner
    if i == 0:
        while (len(r_corner)>0):
            j = r_corner[0]
            child = Node()
            child.parent     = parent

            if j[0] != '0':
                child.value = t_rot.rotate(j[:],2)
            elif j[1] != '0':
                child.value = t_rot.rotate(j[:],1)
            else:
                child.value  = j[:]

            r_corner.remove(j)
            parent.children+=(child,)

#For the leftmost corner
    elif i == (layers-1)*(layers-1):
        while(len(r_corner)>0):
            j = r_corner[0]


            pos_m = 0
            found = 0
#Ensuring that there is atleast one inner pieces that can be placed after this corner
            for m in r_inner:
                if m[1] == j[1]:
                    #found = 1
                    for n in r_sides:
                        if m[0] == n [0] or \
                            m[0] == n [1] or \
                            m[0] == n [2] :
                            found =1
                            break
                if found == 1:
                    break

            if found!=1:
                r_corner.remove(j)
                continue


            child = Node()
            child.parent     = parent

            if j[0] != '0':
                child.value = t_rot.rotate(j[:],1)
            elif j[2] != '0':
                child.value = t_rot.rotate(j[:],2)
            else:
                child.value  = j[:]

            r_corner.remove(j)
            parent.children+=(child,)

## The final piece
    elif i == (layers)*(layers)-1:   #laste piece

        while(len(r_corner)>0):
            j = r_corner[0]

            child = Node()
            child.parent     = parent

            if j[2] != '0':
                child.value = t_rot.rotate(j[:],1)
            elif j[0] != '0':
                child.value = t_rot.rotate(j[:],2)
            else:
                child.value  = j[:]

            r_corner.remove(j)
            parent.children+=(child,)
## left side pieces
    elif i == current_layer*current_layer:
        while (len(r_sides)>0):

            j = r_sides[0]
            child = Node()
            child.parent     = parent

            if j[2] == '0':
                child.value = t_rot.rotate(j[:],1)
            elif j[1] == '0':
                child.value = t_rot.rotate(j[:],2)
            else:
                child.value  = j[:]

            r_sides.remove(j)
            parent.children+=(child,)

## The final layer
    elif current_layer == layers-1:

        ## if the finat layer is evem the bottom pieces are at the even posistions and
        ## vice versa
        if (current_layer%2==0 and i%2==0) or \
            (current_layer%2!=0 and i%2!=0):

            while (len(r_sides))>0:
                j =r_sides[0]

                if j[1] == '0':
                    value = t_rot.rotate(j[:],1)
                elif j[0] == '0':
                    value = t_rot.rotate(j[:],2)
                else:
                    value  = j[:]

                if value[0]!=parent.value[0]:
                    r_sides.remove(j)
                    continue

                child = Node()
                child.parent     = parent

                child.value = value
                r_sides.remove(j)
                parent.children+=(child,)

        else:   # for inner in the final layer

            t_puzzle = []
            p_puzzle = []
            temp_parent = parent
            for _ in range(0,i):
                t_puzzle.append(temp_parent.value)
                temp_parent = temp_parent.parent

            p_puzzle = [t_puzzle[j] for j in range(len(t_puzzle)-1,-1,-1)]

            while (len(r_inner))>0:
                j = r_inner[0]

                if j[1]!=parent.value[1]:
                    r_inner.remove(j)
                    continue
                elif(j[2]!=p_puzzle[len(p_puzzle)-current_layer*2][2]):
                    r_inner.remove(j)
                    continue

                child = Node()
                child.value      = j[:]
                child.parent     = parent
                r_inner.remove(j)
                parent.children+=(child,)

## For right edges of the puzzle
    elif i == current_layer*current_layer+2*current_layer:
        while (len(r_sides))>0:
            j = r_sides[0]
            value = j
            if j[0] == '0':
                value = t_rot.rotate(j[:],1)
            elif j[2] == '0':
                value = t_rot.rotate(j[:],2)
            else:
                value  = j[:]

            if value[0]!=parent.value[0]:
                r_sides.remove(j)
                continue

            child = Node()
            child.parent     = parent
            child.value = value
            r_sides.remove(j)
            parent.children+=(child,)


## For other inner pieces
    else:
        t_puzzle = []
        p_puzzle = []
        temp_parent = parent
        for _ in range(0,i):
            t_puzzle.append(temp_parent.value)
            temp_parent = temp_parent.parent

        p_puzzle = [t_puzzle[j] for j in range(len(t_puzzle)-1,-1,-1)]
        pos_j = 0

## Here the each selected piece are compared with the remaining pieces to ensure that there is
## atleast one piece to place after the current piece
        while len(r_inner)>0:
            j = r_inner[0]

            if (current_layer%2==0):
                if i%2 != 0:    ### inverted layers at even postion when the current layer is odd and vice versa
                    if (j[1]!=parent.value[1]): ## comapring the first edge witht the piece on the left
                        r_inner.remove(j)
                        continue
                    elif(j[2]!=p_puzzle[len(p_puzzle)-current_layer*2][2]): ## comparing the bottom edge with the piece on the top
                        r_inner.remove(j)
                        continue


                        pos_n = 0
                        found = 0
                        for n in r_inner:
                            pos_n+=1
                            if pos_n==pos_j:
                                continue
                            else:
                                if n[0] == j [0]:
                                    found = 1
                                    break
                        if found != 1:
                            r_inner.remove(j)
                            continue

                        temp = []
                        if i == current_layer*current_layer+2*current_layer - 1:
                            found = 0

                            for s  in r_sides:
                                if s[0]=='0':
                                    temp = t_rot.rotate(s[:],1)
                                elif s[2]=='0':
                                    temp = t_rot.rotate(s[:],2)
                                else:
                                    temp = s[:]
                                if j[0] == temp[0]:
                                    found = 1
                                    break

                        if found != 1:
                            r_inner.remove(j)
                            continue
                else: ### other inner pieces
                    if (j[0]!=parent.value[0]):
                        r_inner.remove(j)
                        continue


                    found = 0
                    pos_m=0
                    for m in r_inner:
                        pos_m += 1
                        if pos_m==pos_j:
                            continue
                        else:
                            if (m[1]==j[1]):
                                pos_n = 0
                                for n in r_inner:
                                    pos_n+=1
                                    if pos_n==pos_m or pos_n==pos_j:
                                        continue
                                    else:
                                        if n[2] == j [2]:
                                            found = 1
                                            break
                        if found == 1:
                            break
                    if found != 1:
                        r_inner.remove(j)
                        continue


            elif (current_layer%2!=0):
                    if i%2 == 0:
                        if (j[1]!=parent.value[1]):
                            r_inner.remove(j)
                            continue
                        elif(j[2]!=p_puzzle[len(p_puzzle)-current_layer*2][2]):
                            r_inner.remove(j)
                            continue


                            pos_n = 0
                            found = 0
                            for n in r_inner:
                                pos_n+=1
                                if pos_n==pos_j:
                                    continue
                                else:
                                    if n[0] == j [0]:
                                        found = 1
                                        break
                            if found != 1:
                                r_inner.remove(j)
                                continue

                            temp = []
                            if i == current_layer*current_layer+2*current_layer - 1:
                                found = 0

                                for s  in r_sides:
                                    if s[0]=='0':
                                        temp = t_rot.rotate(s[:],1)
                                    elif s[2]=='0':
                                        temp = t_rot.rotate(s[:],2)
                                    else:
                                        temp = s[:]
                                    if j[0] == temp[0]:
                                        found = 1
                                        break

                            if found != 1:
                                r_inner.remove(j)
                                continue
                    else:
                        if (j[0]!=parent.value[0]):
                            r_inner.remove(j)
                            continue


                        found = 0
                        pos_m=0
                        for m in r_inner:
                            pos_m += 1
                            if pos_m==pos_j:
                                continue
                            else:
                                if (m[1]==j[1]):
                                    pos_n = 0
                                    for n in r_inner:
                                        pos_n+=1
                                        if pos_n==pos_m or pos_n==pos_j:
                                            continue
                                        else:
                                            if n[2] == j [2]:
                                                found = 1
                                                break
                            if found == 1:
                                break
                        if found != 1:
                            r_inner.remove(j)
                            continue


            child = Node()
            child.value      = j[:]
            child.parent     = parent
            r_inner.remove(j)
            parent.children+=(child,)

## Only doing the simulation when the parent has children
    if len(parent.children)>0:

        o = random.randint(0,len(parent.children)-1)
        t_puzzle = []
        p_puzzle = []
        temp_parent = parent.children[o]
        for _ in range(0,i+1):
            t_puzzle.append(temp_parent.value)
            temp_parent = temp_parent.parent


## Generating the puzzle at current postion
        p_puzzle = [t_puzzle[j] for j in range(len(t_puzzle)-1,-1,-1)]

## calculating the scores
        v_score = 0
        v_score,flag = simulation(parent.children[o],i,p_puzzle)
        parent.children[o].n+=1

        v_score /=parent.n
        parent.children[o].score   = v_score + \
                                    math.sqrt(2)*math.sqrt(2*math.log(root.n)/parent.n)
        c = parent.children[o]
        k = i + 1

    else:

## when there is no children return with high penalty and delete the parent
        parent.n+=1

        v_score = -9999
        parent.score   = v_score + \
                                    math.sqrt(2)*math.sqrt(2*math.log(root.n)/parent.n)
        c = parent
        k = i
        return parent

## update the scores and n till the root nodes
    for _ in range(0,k):
        c=c.parent
        c.n+=1

        if c.parent!='NaN':
            if len(parent.children)>0:
                c.score+=parent.children[0].score
            else:
                c.score+=parent.score

    return parent

## This fucntion generates the puzzle and calulates the fitness
def simulation(p,i,p_puzzle):

    r_corner,r_inner,r_sides = back_prop(i,p,math.sqrt(i))

    puzzle = []
    puzzle = sim.puzzle_generate(r_corner[:],r_sides[:],r_inner[:],layers,p_puzzle[:])

    fitness = fit_eval.fit_evaluate(puzzle[:],layers)

    #print i,fitness
    if fitness >= -1  or i == (layers * layers)-1:
        print("--- %s seconds ---" % (time.time() - start_time))
        flag == False
        print "final",fitness,i
        print puzzle
        pd.draw_puzzle(puzzle,layers)
        exit()
    else:
        flag==True
    return fitness,flag

##Begining with root node
def start_tree():
    root = Node()
    print root
    root.n = 1

    while (flag):
        parent = root
        parent.parent   = 'NaN'
        for i in range(0,len(color)):
            if len(parent.children) == 0:  #if no children create children
                parent = populate_children(parent,i,root)

#If no children remove the parent from the children list of its parent
                if len(parent.children) == 0:
                    parent.parent.children.remove(parent)


                    while (len(parent.children)==0):
                        sam =[]
                        for t in parent.parent.children:
                            if t != parent:
                                sam.append(t)
                        parent.parent.children = sam
                        parent=parent.parent

                        if parent.parent == 'NaN':
                            break


                break

## if there is children find the best child
            else:
                best_fit = parent.children[0].score
                best_child = parent.children[0]
                for j in parent.children:
                    if j.score > best_fit:
                        best_child = j
                        best_fit = j.score
                parent = best_child
        parent = root


def main():

    group_pieces()
    start_tree()


get_pieces()
layers = int(math.sqrt(len(color)))
main()
