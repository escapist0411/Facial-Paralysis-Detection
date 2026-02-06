import os
import random
import shutil

# Paths (edit if needed)
celeba_path = r"dataset_raw/img_align_celeba"         # where you extracted CelebA
droop_path = r"dataset_raw/droopy"      # where you extracted droop dataset

output_normal = r"dataset/normal"
output_paralysis = r"dataset/paralysis"

# Create output folders
os.makedirs(output_normal, exist_ok=True)
os.makedirs(output_paralysis, exist_ok=True)

# Copy limited images
def copy_images(source, destination, limit):
    images = os.listdir(source)
    random.shuffle(images)

    for i, img in enumerate(images[:limit]):
        src = os.path.join(source, img)
        dst = os.path.join(destination, img)
        shutil.copy(src, dst)

    print(f"✅ Copied {limit} images to {destination}")


# Copy 300 Normal + 300 Paralysis
copy_images(celeba_path, output_normal, 300)
copy_images(droop_path, output_paralysis, 300)

print("\n✅ Dataset is readyyh! Now run training.")
