import time
import threading


def sing():
    for i in range(5):
        print("Sing national song ...")
        time.sleep(1)


def dance():
    for i in range(5):
        print("Dance friend step ...")
        time.sleep(1)


def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    print("======== main ==============")


if __name__ == "__main__":
    main()
