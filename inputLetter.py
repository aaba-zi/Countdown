import random

inputWord=[]
vowels="aeiou"
consonants="bcdfghjklmnpqrstvwxyz"
l="abcdefghijklmnopqrstuvwxyz"
c=0
def isVowels(letter) :
    if letter in vowels :
        return "true"


def isConsonants(letter) :
    if letter in consonants :
        return "true"

def vowel() :
    index=random.randint(0,len(vowels)-1)
    inputWord.append(vowels[index])
    return (vowels[index])

def con() :
    index = random.randint(0,len(consonants)-1)
    inputWord.append(consonants[index])
    return (consonants[index])
            
#inputLetters(0)
              
