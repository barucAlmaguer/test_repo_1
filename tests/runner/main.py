#process type: Clock
import time

def main():
    for i in range(0, 10):
        with open("timed_grettings.log", 'a') as f:
            div = 10
            print("Hola mundo, tiempo: {}\n".format(time.time()/div))

if __name__ == '__main__':
    main()