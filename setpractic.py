# If you want to store multiple unique values in same veriable  without worring about the order and type and dublication 
# and represented by {} ( once you add item in set it cannot be change but it can be remove and add again)

# crate a set of fruits 
fruits = {"apple", "banana", "cherry"}
mix_data_set ={1, "apple", 3.14, True}
is_in_set = "banana" in fruits #checks if banana is in the set or not 
print(is_in_set)
#add item in set 
fruits.add("papaya")
fruits.remove("apple") #remove item from set
print(fruits)

#unique Email addresss
email = ["ram@gmail", "shyam@gmail", "ram@gmail", "hari2gmail.com"] #list of emails
#converting list to set
uniques_emails = set(email)
print("uniques emails", uniques_emails)

#finding commom elements of 2 sets
fruits = {"apple", "banana", "tomato"}
vegetables = {"tomato", "potato", "carrot"}
common_items = fruits.intersection(vegetables) #intersection method find the common between two set 
print(common_items)
all_items = fruits.union(vegetables) #union method find all items in both set
print(all_items)
diff_item_for_fruit = fruits.difference(vegetables) # diffrent between set 
print(f"diffrest items for fruit ",diff_item_for_fruit)
diff_item_for_veg = vegetables.difference(fruits) # diffrent between set 
print(f"diffrest items for veg ",diff_item_for_veg)
symmetric_diff = fruits.symmetric_difference(vegetables) #symmetric diffrent between two set
print(symmetric_diff)