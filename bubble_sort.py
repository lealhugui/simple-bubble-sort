
def reorder(lst):
    #counter = 0
    print('\n')
    for i in range(len(lst)):
        if (i+1) == len(lst):
            print(lst)
            return
        if lst[i]>lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
        
    return

if __name__ == '__main__':
    l = [3,6,4,7,8,1,2,5]

    for i in range(10):
        reorder(l)