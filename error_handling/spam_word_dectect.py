def spam_word_count(message):
    count=0
    fr=open("error_handling/spam_words.txt")
    spam_word=[line.strip() for line in fr]
    for w in message.split(" "):
        if w in spam_word:
            count=count+1
    return count
print(spam_word_count("bonus cash "))