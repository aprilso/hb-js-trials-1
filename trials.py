"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print (item)


def get_all_evens(nums):
    evenNums = []

    for num in nums:
        if num % 2 == 0:
            evenNums.append(num)
    
    return evenNums




def get_odd_indices(items):
    result = []

    for i, item in enumerate(items):
        if i %2 != 0:
            result.append(item)
    
    return result


def print_as_numbered_list(items):
    i = 1

    for item in items:
        print(f"{i}. {item}")
        i+=1


def get_range(start, stop):
    nums = []
    i = start
    while i < stop:
        nums.append(i)
        i+=1
    
    return nums

def censor_vowels(word):
    pass  # TODO: replace this line with your code


def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
