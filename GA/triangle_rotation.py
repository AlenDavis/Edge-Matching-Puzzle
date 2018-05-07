def rotate(triangle,rotation):
    if (rotation == 1):
        return [triangle[2],triangle[0],triangle[1]]
    else:
        return [triangle[1],triangle[2],triangle[0]]
