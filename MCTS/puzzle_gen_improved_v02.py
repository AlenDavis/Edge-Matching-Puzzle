import triangle_rotation as t_rot
import random
import math

def puzzle_generate(corners,sides,inner,layers,c_puzzle):
    puzzle =[0 for i in range(0,layers*layers)]
    l=0
    l1=len(c_puzzle)
    #print l1,c_puzzle
    #print "inside"
    for j in range(0,layers):
        for k in range(0,2*j+1):
            if l<l1:
                puzzle[l] = c_puzzle[l]
                l+=1
                continue
            if j == 0 :
                puzzle[l] = random.choice(corners)
                corners.remove(puzzle[l])
                l+=1

            elif (j==layers-1):
                if (k==0):
                    found = 0
                    c = 0
                    puzzle[l] = corners[c]

                    while (found < 1 and c < len(corners)):
                        temp = puzzle[l][:]
                        if puzzle[l][0]!='0':
                            temp=t_rot.rotate(puzzle[l],1)

                        elif puzzle[l][2]!='0':
                            temp=t_rot.rotate(puzzle[l],2)

                        for n in inner:
                            if n[1]!= temp[1] or n[2]!=puzzle[(j-1)*(j-1)][2]:
                                continue
                            for s in sides:
                                temp_s = s[:]

                                if temp_s[0]  == '0':
                                    temp_s = t_rot.rotate(temp_s,2)
                                elif temp_s[1]  == '0':
                                    temp_s = t_rot.rotate(temp_s,1)

                                if n[0] == temp_s[0]:
                                    found = 1
                                    break
                            if found == 1:
                                break

                        if found == 1:
                            break
                        c+=1

                    if found != 1:
                        puzzle[l] = random.choice(corners)

                    corners.remove(puzzle[l])
                    if puzzle[l][0]!='0':
                        puzzle[l]=t_rot.rotate(puzzle[l],1)
                    elif puzzle[l][2]!='0':
                        puzzle[l]=t_rot.rotate(puzzle[l],2)
                    l+=1

                elif (k==j*2):
                    puzzle[l] = random.choice(corners)
                    corners.remove(puzzle[l])
                    if puzzle[l][2]!='0':
                        puzzle[l]=t_rot.rotate(puzzle[l],1)
                    elif puzzle[l][1]!='0':
                        puzzle[l]=t_rot.rotate(puzzle[l],2)

                    l+=1

                else:
                    if (k % 2 != 0):
                        found = 0
                        #print "here"
                    #    print len(puzzle) , i
                        #print l,i
                        #print "inner",inner
                        for inr in inner:
                            if inr[1] == puzzle[l-1][1] and \
                                inr[2] == puzzle[l-int(math.sqrt(l))*2][2]:
                                found = 1
                                puzzle[l] = inr
                                break
                        #print "found",found
                        #print found,inr,puzzle[k-1][1],l-int(math.sqrt(l))*2,l
                        if found != 1:
                            puzzle[l] = random.choice(inner)

                        inner.remove(puzzle[l])
                        inner.remove(t_rot.rotate(puzzle[l],1))
                        inner.remove(t_rot.rotate(puzzle[l],2))
                        l+=1

                    else:
                        found = 0
                        for sds in sides:
                            if sds[0] == puzzle[l-1][0] or \
                            sds[0] == puzzle[l-1][1] or \
                            sds[0] == puzzle[l-1][2]:
                                found = 1
                                puzzle[l] = sds
                                break
                        #print "found sides",found
                        if found!=1:
                            puzzle[l] = random.choice(sides)

                        sides.remove(puzzle[l])
                        if puzzle[l][0]=='0':
                            puzzle[l]=t_rot.rotate(puzzle[l],2)
                        elif puzzle[l][1]=='0':
                            puzzle[l]=t_rot.rotate(puzzle[l],1)
                        l+=1
            else:
                if (k == 0):

                    found = 0
                    for s in sides:
                        temp_s = s[:]

                        if s[2] == '0':
                            temp_s = t_rot.rotate(s,1)

                        elif s[1] == '0':
                            temp_s = t_rot.rotate(s,2)


                            for inr in inner:
                                if inr[1] == temp_s[1] and inr[2] == puzzle[(j-1)*(j-1)][2]:
                                    found = 1
                                    break

                            if found == 1:
                                puzzle[l] = temp_s
                                sides.remove(s)
                                break


                    if found!=1:
                        puzzle[l] = random.choice(sides)
                        sides.remove(puzzle[l])

                    if puzzle[l][1]=='0':
                        puzzle[l]=t_rot.rotate(puzzle[l],2)
                    elif puzzle[l][2]=='0':
                        puzzle[l]=t_rot.rotate(puzzle[l],1)
                    l+=1

                elif(k == j*2):
                    found = 0
                    for sds in sides:
                        t_sds = sds
                        if sds[0] == '0':
                            sds = t_rot.rotate(sds,1)

                        elif sds[2] == '0':
                            sds = t_rot.rotate(sds,2)

                        if sds[0] == puzzle[l-1][0]:
                            found = 1
                            puzzle[l] = sds
                            sides.remove(t_sds)
                            break
                    #print "found sides",found
                    if found!=1:
                        puzzle[l] = random.choice(sides)
                        sides.remove(puzzle[l])

                    if puzzle[l][2]=='0':
                        puzzle[l]=t_rot.rotate(puzzle[l],2)
                    elif puzzle[l][0]=='0':
                        puzzle[l]=t_rot.rotate(puzzle[l],1)
                    l+=1
                else:
                    found = 0
                    pos_inr = -1

                    for inr in inner:
                        pos_inr+=1
                        if (inr[1] == puzzle[l-1][1] and \
                        inr[2] == puzzle[l-int(math.sqrt(l))*2][2] and \
                        k%2!=0):

                            pos_t_inr = -1
                            for t_inr in inner:
                                pos_t_inr += 1

                                if pos_t_inr == pos_inr:
                                    continue
                                else:
                                    if t_inr[0] == inr[0]:
                                        found = 1
                                        break

                            if found == 1:
                                puzzle[l] = inr
                                break

                        elif(inr[0] == puzzle[l-1][0] and k%2==0):

                            pos_t_inr = -1
                            for t_inr in inner:
                                pos_t_inr += 1

                                if pos_t_inr == pos_inr:
                                    continue
                                else:
                                    if t_inr[1] == inr[1]:
                                        found = 1
                                        break

                            if found == 1:
                                puzzle[l] = inr
                                break

                    if found != 1:
                        puzzle[l] = random.choice(inner)

                    inner.remove(puzzle[l])
                    inner.remove(t_rot.rotate(puzzle[l],1))
                    inner.remove(t_rot.rotate(puzzle[l],2))
                    l+=1
    return puzzle
