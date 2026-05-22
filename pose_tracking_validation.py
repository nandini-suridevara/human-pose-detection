import numpy as np
from scipy.spatial.distance import euclidean

# Step 1: Extract Image and Keypoint Data
def extract_keypoints(data):
    release_data = data['RELEASE']
    
    image_data = []
    keypoints_data = []

    for item in release_data:
        image_name = item[0][0][0][0]
        keypoints = []

        # Extract the keypoints data for each annotation
        for annotation in item[1][0][0]:
            print(f"Annotation: {annotation}")  # Check structure
            x = annotation[0]  # Access directly, assuming annotation is now [x, y]
            y = annotation[1]  # Same here for y
            keypoints.append((x, y))

        image_data.append(image_name)
        keypoints_data.append(keypoints)

    return image_data, keypoints_data

   

# Step 2: Preprocess the Data
def preprocess_keypoints(keypoints):
    processed_keypoints = []
    
    for point in keypoints:
        x, y = point
        # You can add any necessary preprocessing here
        processed_keypoints.append((x, y))

    return processed_keypoints

# Step 3: Compute Pose Tracking Accuracy
def compute_pose_accuracy(ground_truth, predicted):
    distances = []
    for gt, pred in zip(ground_truth, predicted):
        dist = euclidean(gt, pred)
        distances.append(dist)

    avg_distance = np.mean(distances)
    return avg_distance

# Example: Running the validation process
def run_pose_tracking_validation(data, predicted_keypoints):
    # Step 1: Extract keypoints data
    image_data, keypoints_data = extract_keypoints(data)

    # Step 2: Preprocess keypoints data
    processed_keypoints_data = [preprocess_keypoints(keypoints) for keypoints in keypoints_data]

    # Step 3: Validate pose tracking for the first image (as an example)
    ground_truth = processed_keypoints_data[0]  # Ground truth for first image
    predicted = predicted_keypoints  # Predicted keypoints for the first image (replace with actual predictions)

    # Compute the accuracy (Euclidean distance)
    accuracy = compute_pose_accuracy(ground_truth, predicted)
    print(f"Pose tracking accuracy (average Euclidean distance): {accuracy}")

if __name__ == "__main__":
    # Sample data (replace with actual data structure)
    data = { 
        'RELEASE': [
            # Example data structure, replace with your actual dataset structure
            [ [["image_1.png"]], [[[[0, 0], [100, 100]], [[150, 150], [200, 200]]]] ],
            # Add more entries as needed...
        ]
    }

    # Example predicted keypoints (replace with actual predicted values)
    predicted_keypoints = [(300, 200), (320, 210), (340, 220)]  # Example predicted keypoints

    # Run the pose tracking validation
    run_pose_tracking_validation(data, predicted_keypoints)
