#!/usr/bin/python3
'''
solution for Alx interview question.
'''


def prime_counter(num):
    count = 0

    for num in range(1, num + 1):
        if num == 1:
            continue
        if num == 2 or num == 3 or num == 5 or num == 7:
            count += 1
        elif num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
            count + 1
    return count


def isWinner(x, nums) -> str:
    '''
    check the README file for details on what
    problem this function solves.
    '''
    if x <= 0:
        return None
    player_wins = {'Maria': 0, 'Ben': 0}

    for num in nums:
        count = prime_counter(num)

        if count % 2 == 0:
            player_wins['Ben'] += 1
        elif count % 2 != 0:
            player_wins['Maria'] += 1

    if player_wins['Maria'] > player_wins['Ben']:
        return 'Maria'
    elif player_wins['Ben'] > player_wins['Maria']:
        return 'Ben'
    else:
        return None
