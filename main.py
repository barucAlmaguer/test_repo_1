import time
with open("my_file.txt", 'a') as f:
    f.write("Hola mundo, tiempo: {}\n".format(time.time()))