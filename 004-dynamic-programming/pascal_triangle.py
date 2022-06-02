def generate(numRows):
    #by shifting value inside array 
        
    #1 initiate 1 as value of rows=0
    rows =  [[1]]
        
    #2 loop rows
    for row in range(1, numRows):
            
        #3 append 1 till end of array
        rows.append([1]*(row+1))
            
        #4 update value of current row and col to sums of two elements from above row 
        for col in range(1, row):
            rows[row][col] = rows[row-1][col] + rows[row-1][col-1]
        
        #5 return updated rows
    return rows 

def main():
    numRows = 5
    res = generate(numRows)
    print(res)


if __name__ == '__main__':
    main()
