# python3
import sys


def build_suffix_array(text):
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value result[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    """

    suffixes = [(text[i:], i) for i in range(len(text))]

    result_util = sorted(suffixes, key=lambda x: x[0])
    result = [el[1] for el in result_util]
    return result


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))
