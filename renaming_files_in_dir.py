import os 
from datetime import datetime


def main():
    dir_path = '/mnt/d/test'
    os.chdir(dir_path)
    current_time = datetime.now()
    strdate = current_time.strftime("%Y%m%d%H%M%S")

    for count,file in enumerate(os.listdir(dir_path)):
        name, ext = os.path.splitext(file)
        name = f"test - {strdate}{count}{ext}"
        os.rename(file,name)



if __name__ == '__main__':
    main()
