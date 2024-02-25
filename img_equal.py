import os
import hashlib
import sys
from tqdm import tqdm


def compute_hash(filepath: str) -> str:
    """Compute hash value of a file"""
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


def is_image_file(filename: str) -> bool:
    """Check if a file is an image."""
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']

    return any(filename.endswith(ext) for ext in image_extensions)


def find_duplicate_images(folder_path: str, threshold=0) -> list:
    """Find duplicate images in a folder."""
    images = [os.path.join(folder_path, f)
              for f in os.listdir(folder_path) if is_image_file(f)]
    hash_dict = {}

    with tqdm(total=len(images), desc="Computing hashes") as pbar:
        for idx, filepath in enumerate(images, start=1):
            # if idx % 100 == 0:
            #     print(f'[{idx}/{len(images)}]')

            image_hash = compute_hash(filepath)
            hash_dict.setdefault(image_hash, []).append(filepath)

            pbar.update(1)

    duplicate_groups = [
        group for group in hash_dict.values() if len(group) > 1]

    return duplicate_groups


def get_extension(filename: str) -> str:
    _, ext = os.path.splitext(filename)

    return ext


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        raise Exception('No filepath given')

    folder_path = sys.argv[1]

    duplicates = find_duplicate_images(folder_path)

    if duplicates:
        with tqdm(total=len(duplicates), desc="Deleting files") as pbar:
            for group in duplicates:
                for image in group[1:]:
                    os.remove(image)

                pbar.update(1)
    else:
        print('No duplicate images found.')
