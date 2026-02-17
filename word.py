def match_words(words):
    ctr=0
    str=[]
    for word in words:
        if len(word)>1 and word[0] == word[-1]:
            str.append(word)
            ctr+=1

    print(str,ctr)
t=["abc","xyz","1221","rst","pop"]
match_words(t)