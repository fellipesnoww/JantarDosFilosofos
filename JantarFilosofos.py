import threading as thr
import time
from Filosofos import Filosofo


def jantarFilosofos():
    nomeFilosofos = ('Rodolfo', 'Bugatti', 'Mauricio', 'Meira', 'Seu parça')

    garfo = [thr.Semaphore() for i in range(5)]     #informa a quantidade de itens

    filosofos = [Filosofo(nomeFilosofos[i], garfo[i], garfo[(i + 1) % 5], 2, i)     # % - modulus
                    for i in range(5)]

    for f in filosofos:
        f.start()

    time.sleep(30)

    return Filosofo.acoes


def main():
    acoes = jantarFilosofos()
    return acoes


if __name__ == '__main__':

    main()
