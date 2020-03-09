import open3d as o3d

print(o3d.__dict__.keys())
pcd = o3d.io.read_point_cloud("./data/006_mustard_bottle/clouds/pc_NP2_NP5_15.ply")
o3d.visualization.draw_geometries([pcd])