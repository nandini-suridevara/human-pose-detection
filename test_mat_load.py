import scipy.io

mat_file = r'C:\Users\dlbha\Downloads\mpii_human_pose_v1_u12_2\mpii_human_pose_v1_u12_2\mpii_human_pose_v1_u12_1.mat'

try:
    data = scipy.io.loadmat(mat_file)
    print("✅ Successfully loaded .mat file!")
    print("Contents keys:", data.keys())
except Exception as e:
    print("❌ Error while opening:", e)
