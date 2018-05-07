def puzzle_gen(corners,sides,inner,layers):
    puzzle =[0 for i in range(0,layers*layers)]
    c=0
    s=(layers-2)*3
    s1=0
    s2=s1+s/3
    s3=s-1
    i=0
    l=0
    for j in range(0,layers):
        for k in range(0,2*j+1):
            if j == 0 :
                puzzle[l] = corners[c]
                c+=1
                l+=1

            elif (j==layers-1):
                if (k==0):
                    puzzle[l] = corners[c]
                    c+=1
                    l+=1

                elif (k==2*j):
                    puzzle[l] = corners[c]
                    c+=1
                    l+=1

                else:
                    if (k % 2 != 0):
                        puzzle[l] = inner[i]
                        i+=1
                        l+=1

                    else:
                        puzzle[l] = sides[s2]
                        s2+=1
                        l+=1
            else:
                if (k == 0):
                    puzzle[l] = sides[s1]
                    s1+=1
                    l+=1
                elif(k == j*2):
                    puzzle[l] = sides[s3]
                    s3-=1
                    l+=1
                else:
                    puzzle[l] = inner[i]
                    i+=1
                    l+=1
    return puzzle
