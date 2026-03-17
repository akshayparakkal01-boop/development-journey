word=input("enter number:")
word_length=len(word)-1
result=""
for i in range(word_length,-1,-1):
    result=result+word[i]
    
if result==word:
    print("is palindrome")
else:
    print("is not palindrome")