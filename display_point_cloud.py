import open3d as o3d
import h5py
import numpy as np

# Open file containing calibration parameters
f = h5py.File('./data/006_mustard_bottle/calibration.h5', 'r')
print(list(f.keys()))

# Get homogeneous matrix from camera NP2 to NP5
H_NP2_from_NP5 = np.array(f['H_N2_from_NP5'])
#print(H_NP2_from_NP5)
#transform = np.linalg.inv(H_NP2_from_NP5)

# Read point cloud file
pcd = o3d.io.read_point_cloud("./data/006_mustard_bottle/clouds/nontextured.ply")
print(np.asarray(pcd.points).shape)

# Apply transform to PC
#pcd.transform(H_NP2_from_NP5)

# Visualize original point cloud and transformed point cloud
o3d.visualization.draw_geometries([pcd])