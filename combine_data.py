import os
import shutil
import hashlib

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def compute_image_hash(image_path):
    hash_func = hashlib.md5()
    with open(image_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def copy_images(source_dirs, dest_dirs, label_mapping, seen_hashes):
    for source_dir, subdir in source_dirs:
        for original_label, generalized_label in label_mapping.items():
            label_dir = os.path.join(source_dir, original_label)
            if os.path.exists(label_dir):
                dest_dir = os.path.join(dest_dirs[subdir], generalized_label)
                create_directory(dest_dir)
                for image_name in os.listdir(label_dir):
                    src_image_path = os.path.join(label_dir, image_name)
                    image_hash = compute_image_hash(src_image_path)
                    if image_hash in seen_hashes:
                        print(f"Duplicate found: {src_image_path}")
                        continue
                    seen_hashes.add(image_hash)
                    dest_image_path = os.path.join(dest_dir, image_name)
                    shutil.copy(src_image_path, dest_image_path)

# Define the directories
base_dir = os.getcwd()
dataset1 = os.path.join(base_dir, 'Dataset 1')
dataset2 = os.path.join(base_dir, 'Dataset 2')
dataset3 = os.path.join(base_dir, 'Dataset 3')

# Define the label mappings
label_mapping = {
    'glioma_tumor': 'tumor',
    'meningioma_tumor': 'tumor',
    'pituitary_tumor': 'tumor',
    'yes': 'tumor',
    'no_tumor': 'no_tumor',
    'no': 'no_tumor'
}

# Define the source directories
source_dirs = [
    (os.path.join(dataset1, 'Testing'), 'test'),
    (os.path.join(dataset1, 'Training'), 'train'),
    (os.path.join(dataset2, 'Testing'), 'test'),
    (os.path.join(dataset2, 'Training'), 'train'),
    (os.path.join(dataset2, 'Validation'), 'test'),
    (dataset3, 'train')
]

# Define the destination directories
dest_dirs = {
    'train': os.path.join(base_dir, 'combined/train'),
    'test': os.path.join(base_dir, 'combined/test')
}

# Create destination directories if they don't exist
for subdir in ['train', 'test']:
    create_directory(os.path.join(dest_dirs[subdir], 'tumor'))
    create_directory(os.path.join(dest_dirs[subdir], 'no_tumor'))

# Set to keep track of seen hashes
seen_hashes = set()

# Copy images to the respective directories and check for duplicates
copy_images(source_dirs, dest_dirs, label_mapping, seen_hashes)

print("Images have been combined into 'train/tumor', 'train/no_tumor', 'test/tumor', and 'test/no_tumor' directories.")
