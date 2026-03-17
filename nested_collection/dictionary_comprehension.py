lst=[10,11,12,11,10,13,13]
#o/p{10:2,11:2,12:1,13:2}
num_count={n:lst.count(n)for n in lst}
print(num_count)


word="racecar"
#display character count
word_count={ch:word.count(ch) for ch in word }
print(word_count)