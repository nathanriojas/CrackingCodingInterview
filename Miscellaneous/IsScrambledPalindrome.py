"""
Is Scrambled Palindrome
Write a function that, given a string of letters, returns true or false for whether the letters in the string
could be arranged to form a palindrome.
E.g. For “torro”, the answer is True, because the letters can be rearranged to spell “rotor”.
"""


# check if a string is a scrambled palindrome by comparing sets against string lengths divided by 2
def IsScrambledPalindrom(st) -> bool:
    # quick cases to check
    if st is None or len(st) == 0:
        return False
    # assume that case doesn't matter i.e. Nan would be a palindrome
    s = st.lower()
    l = len(s)
    ls = len(set(s))
    # two cases to check
    # first, the length of the string is odd
    if l % 2 != 0 and (l // 2) + 1 == ls:
        return True
    # second, the length of the string is even
    if l % 2 == 0 and l // 2 == ls:
        return True
    return False


def main():

    # simple test cases
    cases = ["torro", "aa", "b", "wow", "hello", ",!,.."]
    for strings in cases:
        print("Is " + strings + " a scrambled palindrome? " + str(IsScrambledPalindrom(strings)))


main()
