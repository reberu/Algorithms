def minion_game(string):
    vowels = 'AEIOU'
    kevin = stuart = 0
    size = len(string)
    for i in range(size):
        if string[i] in vowels:
            kevin += size - i
        else:
            stuart += size - i
    if stuart > kevin:
        print('Stuart', stuart)
    elif kevin > stuart:
        print('Kevin', kevin)
    else:
        print('Draw')


if __name__ == '__main__':
    s = 'BANANA'
    minion_game(s)
