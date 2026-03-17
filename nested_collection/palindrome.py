words=["mad","test","tan","dad","stats","racecar"]
# create a new list that contain palindrome words

palindrome_words=[w for w in words if w [::-1]==w]

print(palindrome_words)