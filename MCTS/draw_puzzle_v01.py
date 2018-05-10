from graphics import *
from PIL import Image as NewImage
#puzzle = [['0', '0', '2'], ['0', '1', '5'], ['5', '1', '2'], ['3', '0', '5'], ['0', '2', '4'], ['3', '2', '5'], ['3', '2', '1'], ['3', '2', '5'], ['2', '0', '5'], ['0', '4', '5'], ['1', '4', '4'], ['4', '1', '1'], ['2', '4', '1'], ['1', '1', '1'], ['1', '1', '5'], ['1', '0', '1'], ['0', '1', '4'], ['3', '1', '5'], ['1', '3', '4'], ['2', '3', '1'], ['2', '2', '3'], ['4', '5', '1'], ['4', '5', '5'], ['2', '2', '5'], ['2', '0', '5'], ['0', '3', '3'], ['5', '3', '4'], ['5', '5', '3'], ['3', '1', '1'], ['2', '5', '1'], ['2', '5', '5'], ['3', '5', '3'], ['2', '2', '1'], ['2', '2', '4'], ['2', '4', '5'], ['2', '0', '1'], ['0', '4', '0'], ['3', '4', '3'], ['3', '4', '0'], ['3', '3', '5'], ['2', '2', '0'], ['2', '2', '1'], ['2', '2', '0'], ['4', '3', '3'], ['4', '4', '0'], ['3', '4', '5'], ['3', '5', '0'], ['3', '5', '1'], ['3', '0', '0']]
#layers = 7
def draw_puzzle(puzzle,layers):
    length = 1000
    width  = 10000
    win = GraphWin("My Canvas", length, width)

    x1 = length / 2 - 50
    y1 = 100

    x2 = x1 + 100
    y2 = y1
    x3 = x2 - 50
    y3= y2 - 40


    t_x1=0
    t_x2=0
    t_x3=0

    print(x1,y1,x2,y2,x3,y3)
    #puzzle = [['0', '0', '3'], ['0', '5', '2'], ['1', '5', '3'], ['1', '0', '1'], ['0', '2', '4'], ['3', '3', '4'], ['5', '2', '5'], ['5', '3', '4'], ['2', '0', '2'], ['0', '5', '2'], ['1', '3', '2'], ['5', '3', '2'], ['2', '3', '1'], ['1', '1', '1'], ['5', '3', '3'], ['4', '0', '1'], ['0', '4', '5'], ['5', '2', '2'], ['3', '4', '5'], ['1', '1', '4'], ['1', '1', '3'], ['5', '5', '4'], ['5', '1', '3'], ['5', '1', '4'], ['5', '0', '1'], ['0', '1', '2'], ['3', '5', '3'], ['3', '4', '1'], ['2', '5', '3'], ['1', '5', '1'], ['2', '4', '1'], ['1', '2', '5'], ['4', '4', '1'], ['2', '1', '2'], ['5', '3', '5'], ['4', '0', '4'], ['0', '4', '0'], ['2', '4', '2'], ['2', '2', '0'], ['4', '5', '2'], ['3', '4', '0'], ['1', '2', '2'], ['5', '3', '0'], ['2', '3', '2'], ['3', '3', '0'], ['3', '4', '3'], ['3', '5', '0'], ['1', '2', '5'], ['2', '0', '0']]




    color = {'0':'black','1':'blue','2':'red','3':'yellow','4':'orange','5':'pink','6':'violet'}
    #for i in range(0,2):
    poly_points2 = [Point(x1, y1), Point(x2, y2), Point(x3, y3)]
    poly_points3 = [Point(x1, y1), Point(x1+50, 5), Point(x3, y3)]
    poly_points4 = [Point(x2, y2), Point(x1+50, 5), Point(x3, y3)]

    puzzle_color = []
    print color
    print puzzle
    for i in puzzle:
        puzzle_color.append([color[j] for j in i])


    print puzzle_color
    p = Polygon(poly_points2)
    p.setFill(puzzle_color[0][2])
    p.draw(win)

    p = Polygon(poly_points3)
    p.setFill(puzzle_color[0][0])
    p.draw(win)

    p = Polygon(poly_points4)
    p.setFill(puzzle_color[0][1])
    p.draw(win)
    K=1
    for i in range (0,layers-1):
        x1 = x1-50
    #y1 = x1 * (-0.8) + 260
        y1  = y1 + 95
        x2 = x1 + 100
        y2 = y1
        x3 = x2 - 50
        y3=  y2 - 40

        poly_points2 = [Point(x1, y1), Point(x2, y2), Point(x3, y3)]
        poly_points3 = [Point(x1, y1), Point(x1+50, y1-95), Point(x3, y3)]
        poly_points4 = [Point(x2, y2), Point(x1+50, y1-95), Point(x3, y3)]

        p = Polygon(poly_points2)
        p.setFill(puzzle_color[K][2])
        p.draw(win)

        p = Polygon(poly_points3)
        p.setFill(puzzle_color[K][0])
        p.draw(win)

        p = Polygon(poly_points4)
        p.setFill(puzzle_color[K][1])
        p.draw(win)

        t_x1 = x1
        t_x2 = x2
        t_x3 = x3

        #if K < len(puzzle_color)-1:
        K+=2

        for j in range(0,i+1):


            x1 += 100
            #y1 += 100
            x2 += 100
            #y2 += 100
            x3 += 100
            #y3 += 100



            poly_points2 = [Point(x1, y1), Point(x2, y2), Point(x3, y3)]
            poly_points3 = [Point(x1, y1), Point(x1+50, y1-95), Point(x3, y3)]
            poly_points4 = [Point(x2, y2), Point(x1+50, y1-95), Point(x3, y3)]

            p = Polygon(poly_points2)
            p.setFill(puzzle_color[K][2])
            p.draw(win)

            p = Polygon(poly_points3)
            p.setFill(puzzle_color[K][0])
            p.draw(win)

            p = Polygon(poly_points4)
            p.setFill(puzzle_color[K][1])
            p.draw(win)

            #if K < len(puzzle_color)-1:
            K-=1

            poly_points2 = [Point(x3-100, y1-95), Point(x1+50, y1-95), Point(x3-50, y3-10)]
            poly_points3 = [Point(x3-100, y1-95), Point(x2-100, y2), Point(x3-50, y3-10)]
            poly_points4 = [Point(x1+50, y1-95), Point(x2-100, y2), Point(x3-50, y3-10)]

            p = Polygon(poly_points2)
            p.setFill(puzzle_color[K][2])
            p.draw(win)

            p = Polygon(poly_points3)
            p.setFill(puzzle_color[K][1])
            p.draw(win)

            p = Polygon(poly_points4)
            p.setFill(puzzle_color[K][0])
            p.draw(win)

            #if K < len(puzzle_color)-1:
            if (j==i):
                K+=2
            else:
                K+=3
            #if K >= len(puzzle_color):
            #    K-=3
            #print K
        x1 = t_x1
        x2 = t_x2
        x3 = t_x3



    win.getMouse() # Pause to view result
    win.close()    # Close window when done
#draw_puzzle(puzzle,layers)
