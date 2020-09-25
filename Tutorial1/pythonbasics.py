"""
Intro to python exercises shell code
"""
def is_odd(x):
    return x % 2 == 1



def is_palindrome(word):
    return word[::-1] == word



def only_odds(numlist):
    for num in numlist:
        if num % 2 != 0:
            print(num, end=" ")


print(only_odds([5, 3, 4, 3]))


def count_words(text):


    dict = {}
    text = text.lower()
    text_list = list(text.split(" "))

    for i in text_list:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    return dict


print(count_words("How much wood would a woodchuck chuck if a woodchuck could chuck wood?"))


