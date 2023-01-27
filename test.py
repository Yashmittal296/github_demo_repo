t = int(input())
list_dimensions = []
for i in range(0, t):
    dimensions = str(input()).split(' ')
    list_dimensions.append([int(element) for element in dimensions])
