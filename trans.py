from add import add
vecs = [(1,2), (3,4), (5,-1), (1,1)]
trans = (1,3)

def translation(trans, vecs):
    #vecs_new = []
    #for vec in vecs:
    #    vecs_new.append((vec[0]+trans[0], vec[1] + trans[1]))
    #print("result: ", vecs_new)
    return[add([trans, v]) for v in vecs]
print("tr: ",translation(trans, vecs))
