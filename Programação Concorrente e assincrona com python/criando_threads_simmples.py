import threading
from random import randint
from time import sleep

def main():
    th = threading.Thread(target=contar, args=(f"Tubarão {randint(1, 100)}", 20))

    th.start()

    print("fazendo outra coisa duranto o programa")
    sleep(5)
    for i in range(15):
        print(f"{i} = macaco louco")

    th.join()

    print("Finalizando")

def contar(obj, numero):
    for n in range(numero):
        print(obj)
        sleep(1)

if __name__ == "__main__":
    main()  