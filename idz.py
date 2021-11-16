#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    sentence = input("Enter the sentence: ")
    splitted_sentence = sentence.rsplit()
    print(splitted_sentence)
    print(splitted_sentence[0][0])
    for word in splitted_sentence:
        if word.endswith(word[0]):
            print("This word starts with the same char which "
                  f"it ends: {word}")
        if word.count('e') == 3:
            print(f"This word  has exactly three 'e' characters in it: {word}")
        if word.count('o') > 0:
            print(f"This word  has at least one 'o' character in it: {word}")
