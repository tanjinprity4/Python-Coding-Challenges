
#given a 2D list, return the sum of the elemnts in the perimeter. list will be a rectangle.
def perimeter(arr):
    sum = 0
    for i in arr:
        for j in i:
            print(j, end = " ")
        print()
    print()
    for i in range(len(arr)):
        l = len(arr[i])
        for j in range(l):
            if i == 0 or i == (len(arr) - 1):
                sum += arr[i][j]
                print(arr[i][j], end = " ")
            elif j%l == 0 or j%l == (l-1):
                sum += arr[i][j]
                print(arr[i][j], end = " ")
    print()
    return sum

arr = [[1, 2, 3], [2, 3, 4], [1, 2, 4], [5, 4, 3]]
s = perimeter(arr)
print("The sum of the elemnts in the perimeter: " + str(s))
