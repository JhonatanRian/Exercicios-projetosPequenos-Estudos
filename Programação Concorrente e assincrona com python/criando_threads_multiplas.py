import threading
from random import randint
from time import sleep

def main():
    threads = [
        threading.Thread(target=contar, args=(f"Tubarão {randint(1, 100)}", 20)),
        threading.Thread(target=contar, args=(f"Buraco {randint(1, 100)}", 20)),
        threading.Thread(target=contar, args=(f"Dinheiro {randint(1, 100)}", 20)),
        threading.Thread(target=contar, args=(f"Pato {randint(1, 100)}", 20)),
    ]

    [x.start() for x in threads]

    print("fazendo outra coisa duranto o programa")
    sleep(5)
    for i in range(15):
        print(f"{i} = Mico leão Durado")

    print("fazendo outra coisa duranto o programa")
    sleep(3)

    [x.join() for x in threads]

    print("Finalizando")

def contar(obj, numero):
    for n in range(numero):
        print(obj)
        sleep(1)

if __name__ == "__main__":
    main()  