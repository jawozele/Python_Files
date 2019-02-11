list1 = ["Movies", "Music", "Pictures"]

list1.append("Files")



list1.append("Documents")

visitor = input("Hello! Please enter your name: ")
print("Oh Hi! {}. These are what we have on file {}".format(visitor, list1))

print("App done")



list1.remove("Pictures")

list2 = ["Music2", "Movies2"]

list1.extend(list2)

print(list1)