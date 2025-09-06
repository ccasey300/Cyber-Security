# program to investigate list functions
# 23/01/23
lucky_numbers = [2, 8, 7, 9, 31, 12]
friends = ["Kevin", "Dave", "Phil", "Jonny", "Chris"]
print(friends)
print(lucky_numbers)
friends.append("Max")
print(friends)
friends.insert(1, "Oscar")
print(friends)
# friends.extend(lucky_numbers) combines lucky to end of friends
print(friends)
friends.remove("Oscar")
print(friends)
friends.pop()
# removes last item on list
print(friends.index("Chris"))
# finds and prints index of Chris
friends.append("Chris")
print(friends.count("Chris"))
friends.sort()
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
combined_list = friends.copy()
combined_list.extend(lucky_numbers)
# copies friends and adds numbers to make a new combined list
# friends.clear() clears items from list
print(combined_list)

