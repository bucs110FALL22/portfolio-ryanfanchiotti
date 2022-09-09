import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 3
print(classes_per_week, "int")
cost_per_class = (cost_per_week / classes_per_week)
print(cost_per_class, "float")
print("The cost per class is", cost_per_class)

#Part B
list1 = [1, 9.0, "hello", 9/2, "hi"]
choice = random.choice(list1)
print(choice)