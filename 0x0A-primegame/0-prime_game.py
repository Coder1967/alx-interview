#!/usr/bin/python3
'''
solution for Alx interview question.
'''


def num_gen(num):
    '''
    generates a list of integers
    >= 1 and <= num(passed arg).
    '''
    nums = []
    i = 1

    while i <= num:
        nums.append(i)
        i += 1
    nums.reverse()
    return nums


def remove_multiples(num, nums):
    '''
    removes an int(num) and all its multiples
    from a list(nums).
    '''
    i = 0
    nums_length = len(nums)
    new_list = []

    while i < len(nums):
        if nums[i] == 1:
            new_list.append(nums[i])
        if num % nums[i] != 0 and nums[i] % num != 0:
            new_list.append(nums[i])
        i += 1
    return new_list


def prime_filter(nums):
    new_nums = []

    for num in nums:
        if num == 1:
            continue
        if num == 2 or num == 3 or num == 5 or num == 7:
            new_nums.append(num)
        elif num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
            new_nums.append(num)
    return new_nums

def isWinner(x, nums) -> str:
    '''
    check the README file for details on what
    problem this function solves.
    '''
    if x <= 0:
        return None
    player_wins = {'Maria': 0, 'Ben': 0}

    for num in nums:
        numbers = num_gen(num)
        numbers = prime_filter(numbers)

        if len(numbers) % 2 == 0:
            player_wins['Ben'] += 1
        elif len(numbers) % 2 != 0:
            player_wins['Maria'] += 1

    if player_wins['Maria'] > player_wins['Ben']:
        return 'Maria'
    elif player_wins['Ben'] > player_wins['Maria']:
        return 'Ben'
    else:
        return None
