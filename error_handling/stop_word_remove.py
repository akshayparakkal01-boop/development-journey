

def remove_stop_words(sentence):
    result=""
    fr=open("error_handling/stop_words.txt")
    stop_words=[line.rstrip("\n") for line in fr]
    cleaned_word=[w for w in sentence.split(" ")if w not in stop_words]
    result=" ".join(cleaned_word)
    return result
  

sentence2="machine learning is a subset of AI"
sentence3="django is a one of python framework"
print(remove_stop_words(sentence2))
print(remove_stop_words(sentence3))

assert remove_stop_words(sentence2)=="machine learning subset AI","test case 1 failed"
assert remove_stop_words(sentence3)=="django one python framework","test case2 failed"

print("code accepted")

