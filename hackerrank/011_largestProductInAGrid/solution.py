#!/bin/python3

import sys

grid = []
for grid_i in range(20):
	grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
	grid.append(grid_t)

def rightProduct(startX, startY, factors):
    # check if startY is valid
    if startY > len(grid) - factors:
        return 0

    rightProduct = 1
    for y in range(0, factors):
        rightProduct *= grid[startX][startY + y]

    return rightProduct


def downProduct(startX, startY, factors):
    if startX > len(grid) - factors:
        return 0

    downProduct = 1

    for x in range(0, factors):
        downProduct *= grid[startX + x][startY]

    return downProduct

def topLeftBottomRightDiagonalProduct(startX, startY, factors):
    if startY > len(grid) - factors or startX > len(grid) - factors:
        return 0

    tlbrProduct = 1

    for xy in range(0, factors):
        tlbrProduct *= grid[startX + xy][startY + xy]

    return tlbrProduct

def topRightBottomLeftDiagonalProduct(startX, startY, factors):
    if startY < factors - 1 or startX > len(grid) - factors:
        return 0

    trblProduct = 1

    for xy in range(0, factors):
        trblProduct *= grid[startX + xy][startY - xy]

    return trblProduct

def calculateLargestCellProduct(startX, startY, factors):
    products = [
        rightProduct(startX, startY, factors),
        downProduct(startX, startY, factors),
        topLeftBottomRightDiagonalProduct(startX, startY, factors),
        topRightBottomLeftDiagonalProduct(startX, startY, factors)
    ]

    return max(products)


def largestProductInAGrid(factors):
    if len(grid) < factors:
        return 0

    largestProduct = 0

    # rows
    for x in range(0, len(grid)):
        # columns
        for y in range (0, len(grid)):
            largestCellProduct = calculateLargestCellProduct(x, y, factors)
            if largestCellProduct > largestProduct:
                largestProduct = largestCellProduct
    
    return largestProduct

print(largestProductInAGrid(4))
