import inputLetter
import time
f = open(r'C:\Users\ThinkPad\Desktop\CountDown-Game-master\untitled1\words.txt')
wordlist=[]
dic={}
infor={}
#inputWord=inputLetter.inputWord
#inputWord="agreement"
def set_input_word(inputword) :
    start = time.time()
    checkWord(f,inputword)
    end = time.time()
    print (end-start)


def check(word,flag,inputword) :
    cc=list(inputword)
  #  print(cc)
    n=0
    flag=flag
    ww=list(word)
   # print(word)
    for i in word :
     #   print(ww)
      #  print(i)
      #  print(i in cc)
        if i in cc :
            
            ww.remove(i)
            cc.remove(i)
        #    print(ww)
      
        if len(ww)==0 :
            break 
     
    if len(ww)==flag :
        return 0;
        
def checkWord(f,inputword):
    infor.clear()
    f=open(r'C:\Users\ThinkPad\Desktop\CountDown-Game-master\untitled1\words.txt')
    for word in f:
        word = word.strip()

        if check(word,0,inputword)==0 :
          #  print(word)
            wordlist.append(word)
            infor[word]=len(word)
    print(sorted(infor.items(), key=lambda item: item[1]))


#set_input_word(inputWord)