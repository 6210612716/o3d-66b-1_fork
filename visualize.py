import open3d as o3d

def visualize_pcd(path):
    pcd = o3d.io.read_point_cloud(path)
    o3d.visualization.draw_geometries([pcd])

def main():
    # path = input("Enter file path: ")
    visualize_pcd("data/kota-3.ply")

if __name__ == '__main__':
    main()
