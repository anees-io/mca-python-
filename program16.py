color_list1 = input("enter colors in list 1:").split(",")
color_list2 = input("enter colors in list 2:").split(",")
for color in color_list1:
    if color not in color_list2:
        print(color)
