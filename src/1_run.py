from modules.runner import Runner
import glob
import os
import datetime

if __name__ == '__main__':
    
    DATASET_PATH = '../data/dataset/'

    all_files_paths = [
        x for x in glob.iglob(DATASET_PATH + '**', recursive=True)
        if os.path.isfile(x)
    ]

    WORK_DIR = f'../data/result_{datetime.datetime.now().strftime("%d%m%Y_%H%m%s")}'
    os.mkdir(WORK_DIR)

    runner = Runner()
    
    all_ = 0
    processed_ = 0
    for file_path in all_files_paths:
        try:
            output_dir = os.path.join(WORK_DIR, file_path.rsplit('/', 1)[1].rsplit('.', 1)[0])
            os.mkdir(output_dir)
            runner.process(file_path, output_dir)
            processed_ += 1
        except:
            print(f'Can\'t process file {file_path}')
        all_ += 1
        
    print(f'Processed {processed_}/{all_}')

    