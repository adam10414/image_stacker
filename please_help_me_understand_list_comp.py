#This is the easiest way I know to update individual elements in an array.
#I know this is old school, please enlighten me.

test1 = [[[1, 2, 3], [1, 2, 3], [1, 2, 3]]]
test2 = [[[1, 2, 3], [1, 2, 3], [1, 2, 3]]]

result_array = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]]]

row = 0
while row < len(test1):
    pixel = 0
    while pixel < len(test1[row]):
        channel = 0
        while channel < len(test1[row][pixel]):
            result_array[row][pixel][channel] = test1[row][pixel][channel] * 2
            channel += 1
        pixel += 1
    row += 1

print(result_array)
