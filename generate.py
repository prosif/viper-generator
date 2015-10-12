import random
import re

def main():
    words = {}
    with open("temp.txt") as f:
        for line in f:
            word_list = re.sub("[^\S]", " ", line[:line.index('[')]).split()
            i = 0
            while i < len(word_list):
                if word_list[i] not in words:
                    words[word_list[i]] = []
                if i not in words[word_list[i]]:
                    words[word_list[i]].append(i)
                i += 1

    to_return = ""
    for word in words:    
        index = random.randint(0, len(words[word])
        to_return += word[

if __name__ == '__main__':
    main()
