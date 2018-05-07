import random

def selection(fit):
    parents = []
    window = 7
    number_of_parents = int(0.2*len(fit))

    a = fit

    while len(parents) < (number_of_parents):
        j=[]
        for _ in xrange(window):
            i = random.randint(0,len(a)-1)
            while (i in parents or i in j):
                i = random.randint(0,len(a)-1)


            j.append(i)

        m = min(j)
        parents.append(m)
        parents = list(set(parents))

    return parents
