import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()


filenames = [f'./file {number}.txt' for number in range(1, 5)]

start = datetime.now()
for filename in filenames:
    read_info(filename)
end = datetime.now()
print(f'Время выполнения - {end - start} секунд')


if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.now()
        pool.map(read_info, filenames)
        end = datetime.now()
    print(f'Время выполнения - {end - start} секунд')
