import scipy.io

# Correct path to the '.mat' file
mat_file_path = r'C:\Users\dlbha\Downloads\mpii_human_pose_v1_u12_2\mpii_human_pose_v1_u12_2\mpii_human_pose_v1_u12_1.mat'

# Load the .mat file
try:
    mat = scipy.io.loadmat(mat_file_path)
except FileNotFoundError:
    print(f"File {mat_file_path} not found. Please check the path.")
    exit()

# Inspect the structure of the 'RELEASE' key
release_data = mat.get('RELEASE', None)

if release_data is not None:
    print(f"Data inside 'RELEASE' key: {release_data}")
else:
    print("The 'RELEASE' key was not found or is empty. Please inspect the structure of the .mat file.")
