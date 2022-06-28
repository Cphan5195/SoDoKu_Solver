# import tkinter
# tk = tkinter.Tk()
# tk.title("my first app")

# button = tkinter.Button(tk,text="click here")


# button.pack()

# tk.mainloop()
matrix = [
    [1,4,2,6,3,0],
    [3,0,6,0,0,2],
    [0,0,3,5,0,4],
    [0,0,0,2,6,3],
    [0,2,0,0,5,0],
    [5,3,0,4,0,0],
]


def findEmpty(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j] == 0):
                return  (i,j)
    return None

def valid(matrix,inputValue,pos):
    for i in range(len(matrix[0])): # ivalid Row
        if(matrix[pos[0]][i] == inputValue):
            return False
    for i in range(len(matrix)): # ivalid Col
         if(matrix[i][pos[1]] == inputValue):
            return False
        
        # 9*9
    # x = pos[0]//3
    # y = pos[1]//3
    # for i in range(x*3,x*3+3):
    #     for j in range(y*3,y*3+3):
    #         if(inputValue == matrix[i][j]):
    #             return False
    return True

def print_result(matrix):
    for row in matrix:
        for col in row:
            print (col,end=" ")     
        print()     
        
def solve(matrix):
    empty_position = findEmpty(matrix)

    if(empty_position == None):
        return  True
    x,y = empty_position
    for i in range(1,7):
        if(valid(matrix,i,empty_position)):
            matrix[x][y] = i
            if(solve(matrix)):
                return True
            matrix[x][y] = 0  # backtracking  quay lui
    return False




solve(matrix)
print_result(matrix)