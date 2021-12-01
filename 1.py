import os

cookie =

if __name__ == '__main__':
    import time
    print('\nProcess starting...\n--------------------------------\n')
    t0 = time.time()
    # --------------------------------

    print(open(, 'r').read())

    # --------------------------------
    print(f'\n--------------------------------\nProcess finished in {time.time() - t0:.3f} seconds...\n')
