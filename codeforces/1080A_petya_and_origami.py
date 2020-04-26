n, k = map(int, input().split())

reds = n * 2
green = n * 5
blue = n * 8

red_notebooks = reds // k if reds % k == 0 else reds // k + 1
green_notebooks = green // k if green % k == 0 else green // k + 1
blue_notebooks = blue // k if blue % k == 0 else blue // k + 1

print(red_notebooks + green_notebooks + blue_notebooks)