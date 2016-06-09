# def draw_stars(mylist):
#     for number in mylist:
#         print('*' * number)
#
# x = [4, 6, 1, 3, 5, 7, 25]
#
# draw_stars(x)


def draw_stars(mylist):
    for item in mylist:
        if (type(item) == int):
            print('*' * item)
        elif(type(item) == str):
            print(item[0].lower() * len(item))
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

draw_stars(x)
