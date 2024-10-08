from time import sleep
import threading
import time

start_time_1 = time.time()


def write_words(word_count, file_name):
    with open(file_name, "w") as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)

    print(f"Завершилась запись в файл {file_name}")


write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
end_time_1 = time.time()
print(f"Работа потоков {end_time_1 - start_time_1} секунд")

start_time_2 = time.time()
threads = []
for word_count, file_name in [(10, "example5.txt"), (30, "example6.txt"), (200, "example7.txt"), (100, "example8.txt")]:
    thread = threading.Thread(target=write_words, args=(word_count, file_name))
    threads.append(thread)
    thread.start()

# Ожидание завершения всех потоков:
for thread in threads:
    thread.join()

end_time_2 = time.time()
print(f"Работа потоков {end_time_2 - start_time_2} секунд")