import random
import triangle_rotation as t_rot

def swap_mutation(corner,sides,inner,color,layers):
    n_corner = []
    n_sides  = []
    n_inner  = []

    for i in range(0,len(corner)):

        if (random.uniform(0,1)>0.8):
            x=i
            y = random.randint(0,len(corner)-1)
            while(x==y):
                y = random.randint(0,len(corner)-1)

            t         = corner[x]
            corner[x] = corner[y]
            corner[y] = t


        if (random.uniform(0,1)>0.8):
            if(random.uniform(0,1)>0.5):
                corner[i] = t_rot.rotate(corner[i],(1))
            else:
                corner[i] = t_rot.rotate(corner[i],(2))


    for i in range(0,len(corner)):
        place = corner[i]

        if i == 0:
            if place[0] != '0':
                place = t_rot.rotate(place,2)
            elif place[1] != '0':
                place = t_rot.rotate(place,1)

        elif i == 1:
            if place[2] != '0':
                place = t_rot.rotate(place,2)
            elif place[0] != '0':
                place = t_rot.rotate(place,1)

        else:
            if place[1] != '0':
                place = t_rot.rotate(place,2)
            elif place[2] != '0':
                place = t_rot.rotate(place,1)

        n_corner.append(place)



    for i in range(0,len(sides)):

        if (random.uniform(0,1)>0.6):

            x = i
            y = random.randint(0,len(sides)-1)
            while(x==y):
                y = random.randint(0,len(sides)-1)

            t        = sides[x]
            sides[x] = sides[y]
            sides[y] = t

        if (random.uniform(0,1)>0.6):
            if(random.uniform(0,1)>0.5):
                sides[i] = t_rot.rotate(sides[i],(1))
            else:
                sides[i] = t_rot.rotate(sides[i],(2))

    for i in range(0,len(sides)):

        place = sides[i]

        s1=(layers-2)
        s2=s1*2
        s3=s2*2

        if i<(s1):
            if place[1] == '0':
                place = t_rot.rotate(place,2)
            elif place[2] == '0':
                place = t_rot.rotate(place,1)

        elif i<s2:
            if place[0] == '0':
                place = t_rot.rotate(place,2)
            elif place[1] == '0':
                place = t_rot.rotate(place,1)

        else:
            if place[2] == '0':
                place = t_rot.rotate(place,2)
            elif place[0] == '0':
                place = t_rot.rotate(place,1)

        n_sides.append(place)


    for i in range(0,len(inner)):

        if (random.uniform(0,1)>0.4):

            x = i
            y = random.randint(0,len(inner)-1)
            while(x==y):
                y = random.randint(0,len(inner)-1)

            t        = inner[x]
            inner[x] = inner[y]
            inner[y] = t

        if (random.uniform(0,1)>0.4):
            if(random.uniform(0,1)>0.5):
                inner[i] = t_rot.rotate(inner[i],(1))
            else:
                inner[i] = t_rot.rotate(inner[i],(2))


    for i in range(0,len(inner)):
        place = inner[i]

        n_inner.append(place)


    return n_corner,n_sides,n_inner
