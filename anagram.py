import argparse

def anagramchk(word,chkword):
    for letter in word:
        if letter in chkword:
            chkword=chkword.replace(letter, '', 1)
        else:
            return 0
    return 1

def hasAllRequired(word,required):
    for letter in required:
        if letter not in word:
            return False
        word = word.replace(letter, '', 1)
    return True

def solve(opts):
    f=open('wordlist.txt', 'r')
    words = []

    for line in f:
        line=line.strip()

        if anagramchk(line,opts['letters']):
            words.append(line)

            if opts['min']:
                for word in words:
                    if not len(word)>=int(opts['min']):
                        words.remove(word)
                
            if opts['starts']:
                for word in words:
                    if word[0] != opts['starts']:
                        words.remove(word)
            
            if opts['ends']:
                for word in words:
                    if word[-1] != opts['ends']:
                        words.remove(word)

            if opts['required']:
                for word in words:
                    if not hasAllRequired(word, opts['required']):
                        words.remove(word)

            if not opts['unordered']:
                words.sort(key=len, reverse=True)

            if opts['limit']:
                words=words[:int(opts['limit'])]
        
    for word in words:
        print(word)

    f.close()

parser = argparse.ArgumentParser(description='Anagram generator with several options to control the generated words')
parser.add_argument('-l','--letters', help='Letters provided to generate an anagram', required=True)
parser.add_argument('-m','--min', help='Minimum amount of letters in anagram', required=False)
parser.add_argument('-s','--starts', help='Generates words starting with this letter', required=False)
parser.add_argument('-e','--ends', help='Generates words ending with this letter', required=False)
parser.add_argument('-r','--required', help='Generates words that must have this letter or letters', required=False)
parser.add_argument('-u', '--unordered', action='store_true', help='Leave the output in alphabetical order', required=False)
parser.add_argument('--limit', help='The maximum number of words you want to see', default=5, required=False)
args = vars(parser.parse_args())

solve(args)
