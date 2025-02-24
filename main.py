# Function that prints the matrix
def print_matrix(matrix):
    columns = 1
    for k in range(states):
        for j in range(columns):
            print(matrix[k][j], end=" ")
        print()
        columns += 1

with open('input.txt', 'r') as file:
    lines = file.readlines()
# Read the number of cases
cases = int(lines[0].strip())
statesGeneral=[]
alphabetGeneral=[]
finalStatesGeneral=[]
functionsGeneral=[]

line_index = 1
for i in range(cases):
    functionGroup = []
    # Read the number of states and append to the list of states
    statesGeneral.append(int(lines[line_index].strip()))
    line_index += 1
    # Read the alphabet and append to the list of alphabet
    alphabetGeneral.append(lines[line_index].strip().split())
    line_index += 1
    # Read the final states and append to the list of final states
    finalStatesGeneral.append(lines[line_index].strip().split())
    line_index += 1
    for j in range(len(finalStatesGeneral[i])):
        finalStatesGeneral[i][j] = int(finalStatesGeneral[i][j])
    for j in range(statesGeneral[i]):
        function = lines[line_index].strip().split()
        functionGroup.append(function)
        line_index += 1
    functionsGeneral.append(functionGroup)

# for i in range(cases):
#     functionGroup = []
#     # Read the number of states and appends to the list of states
#     statesGeneral.append(int(input()))
#     # Read the alphabet and appends to the list of alphabet
#     alphabetGeneral.append(input().split())
#     # Read the final states and appends to the list of final states
#     finalStatesGeneral.append(input().split())
#     for i in range(len(finalStatesGeneral)):
#         finalStatesGeneral[i] = [int(x) for x in finalStatesGeneral[i]]
#     for i in range(statesGeneral[i]):
#         function = input().split()
#         functionGroup.append(function)
#     functionsGeneral.append(functionGroup)

for i in range(cases):
    functions = {}
    states = statesGeneral[i]
    alphabet = alphabetGeneral[i]
    finalStates = finalStatesGeneral[i]
    # Read the transition functions and  organize them in the form: (initial_state, 'character'): arrive_state in a dictionary
    for j in range(states):
        for k in range(len(alphabet)):
            functions[(int(functionsGeneral[i][j][0]), alphabet[k])] = int(functionsGeneral[i][j][k+1])
    
    # Initialize the matrix with "0" Except on the diagonal, where the states are.
    matrix = [["0"] * states for _ in range(states)]
    for k in range(states):
        for j in range(states):
            if k == j:
                matrix[k][j] = str(k)
    
    # Mark the matrix with "x" for every pair composed of a initial state or (XOR) a final state
    columns = 1
    for k in range(1, states):
        for j in range(columns):
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
    print()