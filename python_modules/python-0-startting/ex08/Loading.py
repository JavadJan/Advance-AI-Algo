import os
from time import sleep
from tqdm import tqdm
import os

columns = os.get_terminal_size().columns


def ft_tqdm(lst: range) -> None:
    """ clone tqdm """

    GREEN = "\033[92m"
    RESET = "\033[0m"

    total = len(lst)
    done = 0

# Terminal width from os
    columns = os.get_terminal_size().columns

# Reserve space for "[100%] | "
    bar_width = columns - len("100%|| 10/10 [00:10<00:00,  1.03s/it]")

    for item in lst:
        done += 1
        percent = int((done / total) * 100)

    # Number of blocks to draw
        blocks = int((percent / 100) * bar_width)

        bar = GREEN + ("█" * blocks) + RESET

        print(f"\r{percent:3d}%|{bar}", end="", flush=True)

        yield item


def main():
    """ cone tqdm """
    for i in ft_tqdm(range(10)):
        sleep(1.03)
    print()

    for i in tqdm(range(10)):
        sleep(1.03)
    print()


if __name__ == "__main__":
    main()
