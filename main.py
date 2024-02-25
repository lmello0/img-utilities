import os
from PIL import Image
import multiprocessing


def are_images_equal(image_path1: str, image_path2: str) -> bool:
    img1 = Image.open(image_path1)
    img2 = Image.open(image_path2)

    if img1.size != img2.size:
        return False

    pixel_pairs = zip(img1.getdata(), img2.getdata())
    differences = [p1 != p2 for p1, p2 in pixel_pairs]

    if any(differences):
        return False

    return True


def compare_images(subset: list[str], images_to_compare: list[str], name: str) -> int:
    count = 0

    for idx, image1 in enumerate(subset, start=1):
        print(f'{name}: [{idx}/{len(subset)}]')

        for idx, image2 in enumerate(images_to_compare):
            if image1 == image2:
                continue

            try:
                if are_images_equal(image1, image2):
                    os.remove(image2)
                    # print(f"Deleted {os.path.basename(image2)}")
                    count += 1

            except FileNotFoundError:
                continue

    return count


def main():
    base_path = "/mnt/c/Users/mello/OneDrive/Área de Trabalho/WhatsApp Stickers/"
    images = [os.path.join(base_path, image)
              for image in os.listdir(base_path)]

    cpu_count = multiprocessing.cpu_count() - 3
    images_per_process = len(images) // cpu_count
    processes = []

    for i in range(cpu_count):
        start_index = i * images_per_process
        end_index = (i + 1) * images_per_process if i < cpu_count - \
            1 else len(images)

        images_subset = images[start_index:end_index]

        process = multiprocessing.Process(target=compare_images, args=(
            images_subset, images[:start_index] + images[end_index:], f'Process {i}'))

        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    remaining_images = [os.path.join(base_path, image)
                        for image in os.listdir(base_path)]

    with open('file.txt', 'w') as file:
        file.write(f'Total files before operation.: {len(images)}')
        file.write(f'Total files after operation.: {len(remaining_images)}')
        file.write(
            f'Total files deleted.: {len(images) - len(remaining_images)}')

if __name__ == '__main__':
    main()
