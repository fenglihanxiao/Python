import time
import threading


def sing():
    for i in range(5):
        print("Sing national song ...\n")
        # time.sleep(1)


def dance():
    for i in range(5):
        print("Dance friend step ...\n")
        # time.sleep(1)


def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)

    # t1.join()
    # t2.join()
    print(threading.enumerate())
    print("======== main ==============\n")


if __name__ == "__main__":
    main()
