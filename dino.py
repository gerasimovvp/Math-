from vector_drawing import *
from add import add
from trans import translation


dino_vectors = [(6,4),(3,1),(1,2),(-1,5),(-2,5),(-3,4),(-4,4),(-5,3),(-5,2),(-2,2),(-5,1),(-4,0),(-2,1),(-1,0),(0,-3),(-1,-4),(1,-4),(2,-3),(1,-2),(3,-1),(5,1)]

dinosaurs = []
polygons = []
#draw(Points(*[(x,x**2) for x in range(-10,11)]), 
#        grid=(1,10), nice_aspect_ratio = False
#        )
for i in range(10):
    for j in range(10):
        
        #dinosaurs.append(Points(*translation((i*10,j*10), dino_vectors)))
        polygons.append(Polygon(*translation((i*12,j*12), dino_vectors)))
        

draw(*polygons)

#new_vecs = translation((10,10),dino_vectors)
#draw(Points(*new_vecs), Polygon(*new_vecs))
