user_input = []
x_count = int(input('How many words you want to enter: '))
for i in range(x_count):
    user_give = str(input('Enter Your word: '))
    user_input.append(user_give)
word_value = []
value_given = {'e':1,'a':1,'i':1,'o':1,'n':1,'r':1,'t':1,'l':1,'s':1,'u':1,'d':1,'g':2,'b':3,'c':3,'m':3,'p':3,'f':4,'h':4,'v':4,'w':4,'y':4,'k':5,'j':8,'x':8,'q':10,'z':10}
add_value=0
for words in user_input:
    for w in words:
        add_value+=value_given[w]
    word_value.append(add_value)
biggest_word =None
#print(word_value)
index_find_k=max(word_value)
index_find=word_value.index(index_find_k)
biggest_word=user_input[index_find]
print('Your wordlist: ',user_input)
print('Biggest value word is: ',biggest_word)
        
        
        
        
        
        