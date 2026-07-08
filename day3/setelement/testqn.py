texts = ["Hello world", "hello Python", "Python world"]


word_count = {}

for sentence in texts:
    
    words = sentence.lower().split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

print(word_count)




2.

day1 = ["alice", "bob", "carol", "dave"]
day2 = ["carol", "dave", "eve", "frank"]

set1 = set(day1)
set2 = set(day2)

both_days = set1 & set2          
only_one_day = set1 ^ set2       
new_on_day2 = set2 - set1       

print("Both days:", both_days)
print("Only one day:", only_one_day)
print("New on day2:", new_on_day2)