#!/usr/bin/env python3

num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']

num_list.append('x534')
word_list.append('x534')
num = input('Enter num: ')
print(num_list.index(num_list[-1]) - num_list[::-1].index(int(num)))
word = input('Enter word: ')
print(word_list.index(word_list[-1]) - word_list[::-1].index(word))

