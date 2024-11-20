# Step 1: Create an empty list called my_list
my_list = []
print(my_list)
# Step 2: Append the following elements: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("my_list after append" , my_list)

# Step 3: Insert the value 15 at the second position
my_list.insert(1, 15)
print("my_list after insert",my_list)
# Step 4: Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])
print("After extend",my_list)
# Step 5: Remove the last element from my_list
my_list.pop()
print("After pop()",my_list)
# Step 6: Sort my_list in ascending order
my_list.sort()
print("my_list after sort()",my_list)
# Step 7: Find and print the index of the value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)
