# word count

text="python programming programming is  simple"

words=text.split(" ")
print(words)
word_count={w:words.count(w) for w in words}

print(word_count)




orders=["tea","coffee","idaly","coffee","tea","dosa","tea","coffee"]

orders_count={o:orders.count(o) for o in orders}
print(orders_count)