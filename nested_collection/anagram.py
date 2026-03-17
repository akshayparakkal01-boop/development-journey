# lst1=["listen","earth","moon","dad","madam","race"]
#lst2=["silent","angel","heart","test","dam","care"]
#anagram_words={"listen"}

words="racecarfast"

#print non recursive character
# print recursive character whose count >= 2

non_recursive=[ch for ch in words if words.count(ch)==1]
recursive={ch:words.count(ch) for ch in words if words.count (ch)>=2}

print("non recursive",non_recursive)
print("recursive",recursive)

