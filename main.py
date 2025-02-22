# Function that prints the matrix
def print_matrix(matrix):
    columns = 1
    for k in range(states):
        for j in range(columns):
            print(matrix[k][j], end=" ")
        print()
        columns += 1
cases = int(input())
for i in range(cases):
    functions = {}
    states = int(input())
    alphabet = input().split()
    finalStates = input().split()
    finalStates = [int(x) for x in finalStates]
    # Read the transition functions and  organize them in the form: (initial_state, 'character'): arrive_state in a dictionary
    for j in range(states):
        function = input().split()
        for k in range(len(alphabet)):
            functions[(int(function[0]), alphabet[k])] = int(function[k+1])
    
    # Initialize the matrix with "0"
    matrix = [["0"] * states for _ in range(states)]
    for i in range(states):
        for j in range(states):
            if i == j:
                matrix[i][j] = str(i)
    
    # Mark the matrix with "x" for every pair composed of a initial state or (XOR) a final state
    columns = 1
    for k in range(1, states):
        for j in range(columns):
            if matrix[k][j] == "0":
                if (k in finalStates) ^ (j in finalStates):
                    matrix[k][j] = "x"
        columns += 1
    
    # Iterate to mark the matrix based on transition functions
    iterator = 1
    while iterator != 0:
        columns = 1
        iterator = 0
        for k in range(1, states):
            for j in range(columns):
                if matrix[k][j] == "0":
                    for l in range(len(alphabet)):
                        x = functions[j, alphabet[l]]
                        y = functions[k, alphabet[l]]
                        if matrix[x][y] == "x" or matrix[y][x] == "x":
                            matrix[k][j] = "x"
                            iterator += 1
            columns += 1
    
    # Print the pairs of states that are not marked with "x" are the equivalent states
    columns = 1
    for k in range(1, states):
        for j in range(columns):
            if matrix[k][j] == "0":
                print(f"({j},{k})", end=" ")
        columns += 1