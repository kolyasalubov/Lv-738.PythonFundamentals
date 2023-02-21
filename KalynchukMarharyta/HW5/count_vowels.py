def count_vowels(word):
   count = 0
   for item in word:
       if item in "aeiouAEIOU":
           count += 1
   return count 
