import assignment2

def sort_the_list():
    lst.sort()
    print(lst)

def sum_the_list():
    tot = 0
    for i in lst:
        tot = tot + i
        print(tot)

def product_of_the_list():
    result = 1
    for i in lst:
        result = result * i
        print(result)

def mean_in_list():
    tot = 0
    for i in lst:
        tot = tot + i
        total = tot / 5
        print(total)

def median_in_list():
    lst.sort()
    if len(lst) % 2 == 0:
        first_median= lst[len(lst) // 2]
        second_median = lst[len(lst) // 2-1]
        median = (first_median + second_median)/ 2
    else:
        median = lst[ len(lst) // 2]
    print(median)

def mode_in_list():
    n = len(lst)
    data = Counter(lst)
    get_mode = dict(data)
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
    if len(mode) == n:
        get_mode = "not mode found"
    else:
        get_mode = "mode is "+ ', '.join(map(str,mode))
    print(get_mode)

def largest_number():
    lst.sort()
    print(lst[-1])

def smallest_number():
    lst.sort()
    print(lst[0])

def remove_duplicates():
    x = []
    for i in lst:
        if i not in x:
            x.append(i)
            print(x)

def remove_even_numbers():
    for i in lst:
        if (i%2 == 0):
            lst.remove(i)
            print(lst)

def remove_odd_numbers():
    for i in lst:
        if (i%2 != 0) :
            lst.remove(i)
            print(lst)

def check_number ():
    x = int(input("Type a number to check if it is on the list "))
    if x not in lst:
        print("I not there")
    else: print("Yes it is")

sort_the_list()
