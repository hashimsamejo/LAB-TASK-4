shopping =[]
for i in range(5):
    item=input("Enter item")
    shopping.append(item)
    print ("\n your complete shopping list:")
    for item in shopping:
        print (f" {item}")