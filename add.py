vecs = [(0,1), (2,3), (4,5)]

def add(vecs):
    x = 0
    y = 0
    for vec in vecs:
        x = x + vec[0]
        y = y + vec[1]
    print("sum: ",(x,y))
    return((x,y))
#add(vecs)

