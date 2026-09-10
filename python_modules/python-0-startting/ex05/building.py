import sys
import string as string_module


def counts_char(text):
    """
            displays the sums of its upper-case characters, lower-case
            characters, punctuation characters, digits, and spaces.
    """
    for char in text:
        print(char)
    counts = {"upper": 0, "lower": 0,
              "punctuation": 0, "space": 0, "digit": 0}
    for char in text:
        if char.isupper():
            counts["upper"] += 1
        elif char.islower():
            counts["lower"] += 1
        elif char.isdigit():
            counts["digit"] += 1
        elif char.isspace():
            counts["space"] += 1
        elif char in string_module.punctuation:
            counts["punctuation"] += 1
    return counts


def report_char(text):
    """
                        reports how many char exist in the text
    """
    counts = counts_char(text)

    print(f"The text contains {len(text)} characters:")
    print(f"{counts['upper']} letters")
    print(f"{counts['lower']} letters")
    print(f"{counts['punctuation']} marks")
    print(f"{counts['space']} spaces")
    print(f"{counts['digit']} digits")


def main():
    """Convert a string to an int, raising a clean error if it fails."""
    try:
        text = sys.argv[1]
    except IndexError:
        print("Error: exactly one string argument is required")
        return
    report_char(text)


if __name__ == "__main__":
    main()
