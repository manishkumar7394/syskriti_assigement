'''taskPY200_T5: Chessboard with Numbers Input: N Print an N x N grid: 
• If (row+col) is even → print 1 • else → print 0 But if row == col → print X instead.'''

# Chessboard Pattern with Numbers

N = int(input("Enter the value of N: "))        # User enters the size of the grid (N × N).

for row in range(N):                            # This loop runs from 0 to N-1.It represents each row.
    for col in range(N):                        #   It represents each column.
        
        if row == col:                          # if both are = That means it’s a diagonal position → print X
            print("X", end=" ")
        
        elif (row + col) % 2 == 0:              # If sum of row and column is even → print 1
            print(1, end=" ")
        
        else:
            print(0, end=" ")               #If sum is odd → print 0
    
    print()  # move to next line after each row

                # After finishing one row, this moves the cursor to the next line.
''' Example Output
If N = 4

X 0 1 0
0 X 0 1
1 0 X 0
0 1 0 X             '''