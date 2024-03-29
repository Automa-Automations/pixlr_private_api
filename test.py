import threading
from pixlr_private_api.main import PixlrApi


def gen_imgase():
    pixlr = PixlrApi()
    pixlr.register()
    pixlr.verify_email()

    def gen():
        print(pixlr.generate_image(1024, 1024, 1, "A happy cat"))

    threads = []
    for _ in range(20):
        thread = threading.Thread(target=gen)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    pixlr.delete_account()


thhreads = []
for i in range(1):
    thread = threading.Thread(target=gen_imgase)
    thread.start()
    thhreads.append(thread)

for thread in thhreads:
    thread.join()
