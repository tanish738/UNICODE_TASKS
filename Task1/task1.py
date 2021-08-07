hello=input("Number of lines:")
all_words=[]
main_words=[]
final_words=[]
rep_words_count=[]
max_rep_word=[]
min_rep_word=[]

#TO TAKE INPUT FROM USER
for num in range(int(hello)):
    z=input("Enter the word:")
    all_words.append(z)
    main_words.append(z)

# TO REATE A FUNCTION THAT RETURNS REPEATED WORDS
def repeat(x):
    size=len(x)
    repeated=[]
    for i in range(size):
        k=i+1
        for j in range(k,size):
            if x[i]==x[j] and x[i] not in repeated:
                repeated.append(x[i])

    return(repeated)
#print(all_words)
#TO STORE ALL REPEATED WORDS
repeated_word=repeat(all_words)

#TO REMOVE ALL THE REPEATED WORDS AND GET NON-REPEATED WORDS
for rep_words in repeated_word:
    for nums in range(int(hello)):
        try:
            all_words.remove(rep_words)
        except:
            pass
non_repeated_words=all_words

#THIS IS TO SHOW ALL DIFFERENT TYPES OF WORDS
print(len(repeated_word)+len(non_repeated_words))
#print(non_repeated_words)
#print(main_words)

# THIS IS TO SHOW THE DESIRED OUTPUT
for wordss in main_words:
    if wordss in repeated_word:
        if wordss not in final_words:
            final_words.append(wordss)
            print(main_words.count(wordss),end="")
    else:
        print(main_words.count(wordss),end="")



# BONUS TASK

#THIS IS TO COUNT THE TIMES REPEATED WORDS IS REPEATED
for reps_words in repeated_word:
    rep_words_count.append(main_words.count(reps_words))

#IF THE COUNT IS MAX IT IS THE MOST TIME REPEATED WORD
for repps_words in repeated_word:
    if main_words.count(repps_words)==max(rep_words_count):
        max_rep_word.append(repps_words)
    elif main_words.count(repps_words)==min(rep_words_count):
        min_rep_word.append(repps_words)

print("\n")
print("the max repeated word is",max_rep_word)

#IF THERE IS NO REPEATED WORD THEN THE MIN REPEATED WORD WILL BE THE LEAST REPEATED WORD
if non_repeated_words==[]:
    print("Least repeated word is",min_rep_word)
else:
    print("Least repeated word is",non_repeated_words)

# THIS IS TO PRINT ALL THE WORDS IN DESCSENDING ORDER
print(non_repeated_words)
try:
    for final_rep_word in max_rep_word:
        repeated_word.remove(final_rep_word)
    print(repeated_word)
except:
    pass
print(max_rep_word)
    