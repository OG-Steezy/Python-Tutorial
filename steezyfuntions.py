#5! =  5 * 4 * 3 * 2 * 1 
#4! = 4 * 3 * 2 * 1

# def func1(var):
    
#     if var == 0:
#         return 1
#     else:
#         return var * func1(var-1)
    
# print(func1(5))


# thisdict = {

# "brand":"ford",
# "model":"mustang",
# "oldyear":1964,
# "year":2020
# }
# print(thisdict["year"])



# Create a function that can replace your backspace key as your keyboard came without one. The replacement key is ~.

# Example The following string "abcd~~~" should output "a"
# another example "aa~bb~cc~dd~" should output "abcd"

# testlist = [1,5,4,2,8]

def is_sorted(thelist):
    if len(thelist)  <= 1:
        return True
    else:
        if thelist[0] < thelist[1]:
            return is_sorted(thelist[1:])
        else:
            return False

def sort(thelist):

    while not is_sorted(thelist):
        for i in range(0, len(thelist) - 1):
            if thelist[i] > thelist[i+1]:
                temp = thelist[i]
                thelist[i] = thelist[i+1]
                thelist[i+1] = temp

    return thelist

# def backspace_replacement(thestring):
#     list = test.split("~")
#     if len(list) == 1:
#         return list[0]
#     else:
#         if list[i] == "":
#             return (list[0][:-1]).append(backspace_replacement(list[1:]))
#         else:
#             return list[0].append(backspace_replacement(list[1:]))

# def process_list(theList):
#     if len(theList) == 1:
#         return [theList[0]]
#     else:
#         if theList[1] == "":
#             processed_cell = [theList[0][:-1]]
#             return processed_cell.append(process_list(theList[1:]))
#         else:
#             return [theList[0]].append(process_list(theList[1:]))


# def backspace_replacement(theString):
#     ourlist = theString.split("~")

#     processed_list = process_list(ourlist)
  
#     return processed_list.join()

def apply_backspace(theString):
    return theString[:-1]

def backspace_replacement(theString):
    ourlist = theString.split("~")

    processed_list = []
    index = 0

    for i in range(0, len(ourlist)):
        if ourlist[i] == "":
            if len(processed_list) > 0:
                processed_list[index-1] = apply_backspace(processed_list[index-1])
        else:
            processed_list.append(ourlist[i])
            index = index + 1
    
    return ''.join(processed_list)