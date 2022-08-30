import numpy as np
from pyntcloud import PyntCloud as pcd
#import open3d as o3d

cloud = pcd.from_file("pcd/Tomato_1.pcd")
vertices = np.array(cloud.points)

for i in vertices:
    print(i)

#meshfile = open("tomato_1.obj", "w")
#meshfile.write("# Reconstrução Leonardo e Victor\n")
#meshfile.write("# IFPR - Campus Pinhais\n")
#for i in vertices:
#    meshfile.write(f"v {i[0]} {i[1]} {i[2]}\n")

#meshfile.close()