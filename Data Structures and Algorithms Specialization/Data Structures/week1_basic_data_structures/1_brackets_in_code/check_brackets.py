# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i + 1))

        if next in ")]}":
            if not opening_brackets_stack:
                return i + 1
            previous_bracket = opening_brackets_stack.pop().char
            if not are_matching(previous_bracket, next):
                return i + 1

    if opening_brackets_stack:
        return opening_brackets_stack[0].position

    return 'Success'


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
