'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # If we were able to use loops it would be something like
    # count = 0
    # for i in word:
    #   if i == "th":
    #       count = count + 1

    # Base Case
    # If the length of the word is less than 2,
    # It can't possibly contain 'th' so return 0 to the count.
    if len(word) < 2:
        return 0

    # If word starts with 'th' return count recursively
    if word[:2] == 'th':
        return count_th(word[1:]) + 1

    # with [1:] we can look through the rest of the word for th
    return count_th(word[1:])
