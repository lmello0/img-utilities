from datetime import datetime
import os
import shutil
from tqdm import tqdm
import sys

if len(sys.argv) <= 1:
    raise Exception('No filepath given')

base_path = sys.argv[1]

files = [os.path.join(base_path, file) for file in os.listdir(base_path)]

with tqdm(total=len(files), desc='Moving files') as pbar:
    for file in files:
        mod_date = datetime.fromtimestamp(os.path.getmtime(file))

        year = mod_date.strftime('%Y')
        month = mod_date.strftime('%b')
        day = mod_date.strftime('%d')

        new_location_dir = os.path.join(base_path, year, month)

        os.makedirs(new_location_dir, exist_ok=True)

        shutil.move(file, os.path.join(new_location_dir, os.path.basename(file)))

        pbar.update(1)