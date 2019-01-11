

n = int(raw_input("List numbers to sort: "))
a = map(int, raw_input().rstrip().split())

def countSwaps(a):
    swaps = 0
    sorted = False;
    while not sorted:
        sorted = True;
        for i in range (0, len(a)-1):
            if a[i] > a[i+1]:
                temp = a[i + 1]
                a[i+1] = a[i]
                a[i] = temp
                swaps += 1;
                sorted = False;
    print("Array is sorted in " + str(swaps) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[-1]))

countSwaps(a)
