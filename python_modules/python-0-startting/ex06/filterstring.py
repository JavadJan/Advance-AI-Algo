import sys
import ft_filter


def main():
    """Clone of the built-in filter() — entry point."""
    try:
        text = sys.argv[1]
        num = int(sys.argv[2])
    except IndexError:
        print("Error: two arguments are required")
        return
    except ValueError:
        print("Error: second argument must be an integer")
        return
    arr = text.split()
    print(list(ft_filter.ft_filter(lambda x: len(x) > num, arr)))


if __name__ == "__main__":
    main()
