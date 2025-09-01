
#wap to give option to select choices as (display,append,delete) from list.
#[] --- user_input
#options
#display list,append item on list, delete item from list

my_list=["apple","banana","mango","orange"]
 
while True:
    print("options")
    print("1. current list")
    print("2. Append item to list")
    print("3. Delete item from list")
    print("4. Exit")

    choice = input("Enter your choice (1-4):")

    if choice == "1":
        print("current list", my_list)

    elif choice == "2":
        item = input("enter item to add")
        my_list.append(item)
        print(f"{item} add tp list")

    elif choice =="3":
        item = input("Enter item to delete")
        if item in my_list:
            my_list.remove(item)
            print(f"{item} removed from list")
        else:
            print("Item not found in list")

    elif choice =="4":
        print("Thank you")
        break
    else:
        print("not found")
