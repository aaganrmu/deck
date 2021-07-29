import threading


def setup():
    watching_thread = threading.Thread(target=watcher, args=(), daemon=True)
    return watching_thread


def watcher():
    while True:
        print('poop')
