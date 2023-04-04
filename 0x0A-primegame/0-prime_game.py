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


def filter_prime(nums):
    '''
    takes a list of integers as argument and
    removes all the non-prime numbers(excluding 1)
    and returns the new list.
    '''
    prime_nums = [2, 3, 5, 7]
    new_nums = []

    for num in nums:
        if num in prime_nums:
            new_nums.append(num)
        if num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
            new_nums.append(num)
    return new_nums


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


def isWinner(x, nums) -> str:
    '''
    check the README file for details on what
    problem this function solves.
    '''
    player_wins = {'Maria': 0, 'Ben': 0}

    for i in range(1, (x + 1)):
        players = {'Maria': False, 'Ben': False}
        j = 0
        numbers = filter_prime(num_gen(nums[i - 1]))
        numbers_length = len(numbers)
        while j < numbers_length:
            try:
                if numbers[j] == 1 and (j + 1) % 2 != 0:
                    players['Maria'] = True
                    players['Ben'] = False
                else:
                    players['Ben'] = True
                    players['Maria'] = False
                numbers = remove_multiples(numbers[j], numbers)
                if (j + 1) % 2 != 0:
                    players['Maria'] = True
                    players['Ben'] = False
                elif (j + 1) % 2 == 0:
                    players['Ben'] = True
                    players['Maria'] = False
            except IndexError:
                pass
            j += 1
        if players['Maria'] is True:
            player_wins['Maria'] += 1
        elif players['Ben'] is True:
            player_wins['Ben'] += 1
    if player_wins['Maria'] > player_wins['Ben']:
        return 'Maria'
    elif player_wins['Ben'] > player_wins['Maria']:
        return 'Ben'
    else:
        return None
