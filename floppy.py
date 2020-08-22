# 0-8 is top
# 9-11 is front
# 12-14 is left
# 15-17 is back
# 18-20 is right
# 21-29 is back

#    17 16 15
# 12  0  1  2  20   21 22 23
# 13  3  4  5  19   24 25 26
# 14  6  7  8  18   27 28 29
#     9 10 11

cube = ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'O', 'O', 'O', 'G', 'G', 'G', 'R', 'R', 'R', 'B', 'B', 'B', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']
def getMove():
    move = input('move please: ').lower()
    if move == 'f':
        cube[9], cube[11] = cube[11], cube[9]
        cube[14], cube[18] = cube[18], cube[14]
        cube[6], cube[27] = cube[27], cube[6]
        cube[7], cube[28] = cube[28], cube[7]
        cube[8], cube[29] = cube[29], cube[8]
    elif move == 'l':
        cube[12], cube[14] = cube[14], cube[12]
        cube[9], cube[17] = cube[17], cube[9]
        cube[0], cube[29] = cube[29], cube[0]
        cube[3], cube[26] = cube[26], cube[3]
        cube[6], cube[23] = cube[23], cube[6]
    elif move == 'b':
        cube[15], cube[17] = cube[17], cube[15]
        cube[12], cube[20] = cube[20], cube[12]
        cube[0], cube[21] = cube[21], cube[0]
        cube[1], cube[22] = cube[22], cube[1]
        cube[2], cube[23] = cube[23], cube[2]
    elif move == 'r':
        cube[18], cube[20] = cube[20], cube[18]
        cube[11], cube[15] = cube[15], cube[11]
        cube[8], cube[21] = cube[21], cube[8]
        cube[5], cube[24] = cube[24], cube[5]
        cube[2], cube[27] = cube[27], cube[2]
    else:
        print('Not valid move.')

def printCube():
    print('  ' + cube[17] + ' ' + cube[16] + ' ' + cube[15])
    print(cube[12] + ' ' + cube[0] + ' ' + cube[1] + ' ' + cube[2] + ' ' + cube[20] + ' ' + cube[21] + ' ' + cube[22] + ' ' + cube[23])
    print(cube[13] + ' ' + cube[3] + ' ' + cube[4] + ' ' + cube[5] + ' ' + cube[19] + ' ' + cube[24] + ' ' + cube[25] + ' ' + cube[26])
    print(cube[14] + ' ' + cube[6] + ' ' + cube[7] + ' ' + cube[8] + ' ' + cube[18] + ' ' + cube[27] + ' ' + cube[28] + ' ' + cube[29])
    print('  ' + cube[9] + ' ' + cube[10] + ' ' + cube[11])

while True:
    printCube()
    getMove()
