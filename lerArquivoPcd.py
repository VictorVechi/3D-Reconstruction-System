#HEAD
#import numpy as np
#from pyntcloud import PyntCloud as pcd
#import open3d as o3d

#cloud = pcd.from_file("arquivos pcd/DellValleMaca_1")
#vertices = np.array(cloud.points)

#for i in vertices:
    #print(i)

#meshfile = open("tomato_1.obj", "w")
#meshfile.write("# Reconstrução Leonardo e Victor\n")
#meshfile.write("# IFPR - Campus Pinhais\n")
#for i in vertices:
#    meshfile.write(f"v {i[0]} {i[1]} {i[2]}\n")

#
import numpy as np
from pyntcloud import PyntCloud as pcd
#import open3d as o3d

cloud = pcd.from_file("arquivos pcd/DellValleMaca_1.pcd")
vertices = np.array(cloud.points)
for i in vertices:
    print(i)

#meshfile = open("tomato_1.obj", "w")
#meshfile.write("# Reconstrução Leonardo e Victor\n")
#meshfile.write("# IFPR - Campus Pinhais\n")
#for i in vertices:
#    meshfile.write(f"v {i[0]} {i[1]} {i[2]}\n")

#3df5456d33ab9e0e6fd73c6714ec9c4354ec97f0
#meshfile.close()