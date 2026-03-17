word="aman##aplan**pananvanwith2car1bike"
# W.A.P to display alphabet_count,digit_count,special_character_count
alpha_count=0
digit_count=0
special_char_count=0

for ch in word:
   if ch.isalpha():
      alpha_count+=1
   elif ch.isdigit():
      digit_count+=1
   elif not ch.isalnum():
      special_char_count+=1
print(f"alphabet count : {alpha_count}")
print(f"digit count : {digit_count}")
print(f"special character count : {special_char_count}")


    