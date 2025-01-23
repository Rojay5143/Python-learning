# variable value exchange example in python 

glass1 ="milk"
glass2 = "water"

print(f"first glass contain {glass1}, second glass contain {glass2}")

#Now After swap value  (bring the concept of third glass)
third_glass = glass1 
glass1 = glass2
glass2 = third_glass

print(f"Now after swap first glass contain {glass1}, second glass contain {glass2}")

#the above method is done in others programming language but in python you can do the following 
# the value will be glass1 ma milk and 2 ma water bcz yo vanda mastera value change vai sakako xa
glass1, glass2 = glass2, glass1
print(f" In python Now after swap first glass contain {glass1}, second glass contain {glass2}")