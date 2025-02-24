# Minimization Algorithm

## Contents
- [Team](#team)
- [Development environment](#development-environment)
- [Instructions for running](#instructions-for-running)
- [Explanation of the algorithm](#explanation-of-the-algorithm)

## Team
- Laura Andrea Castrillón Fajardo
- Samuel Martínez Arteaga
- Class code: 7308

## Development environment
- **Operative System:** Windows 11
- **Programming language:** Python 3.12
- **Tools:** Visual Studio Code

## Instructions for running
- 1. Download the file input.txt
- 2. Change the directory of input.txt to where you have it located (Not necessary if you have it in the same location as the main file).
```
    with open("input.txt", "r", encoding="utf-8") as file:
```
- 3. Run the main file

## Explanation of the algorithm

Algorithm for computing the collapsing relation ~ for a given DFA M with no inaccessible states. We center the explanation on the crucial points to achieve the right results.

```
 for j in range(states):
        for k in range(len(alphabet)):
            functions[(int(functionsGeneral[i][j][0]), alphabet[k])] = int(functionsGeneral[i][j][k+1])
```

Took the array of functions according to the case (i), took the array of each function (j) and makes a dictionary, where the key is the tuple of (state,string) and the value is the resultant state. As a little aclaration each function is stored as [state, resultantState1, resultantState2,...,resultantStateN]


```
    columns = 1
    for k in range(1, states):
        for j in range(columns):
```
Traverse half of the matrix, iterating through all the rows (the states), but the range of columns varies so that we only access and operate on the lower diagonal of the matrix.


```
                if (k in finalStates) ^ (j in finalStates):
                    matrix[k][j] = "x"
        columns += 1
```
Realize the step 1:  Mark {p, q} if p ∈ F and q ∉ F or vice versa. The variables k, j represent states, if k or j belong to a finalStates (array of final states). Then mark the corresponding box with the character "x". As a small clarification, the 'or' operator is used as an XOR, meaning it only applies when either k ∈ F or j ∈ F, but not both.

```
 iterator = 1
    while iterator != 0:
        iterator = 0
```

A loop is used that remains active while the iterator is not equal to 0, that is, when a new cell in the matrix is marked, meaning there are still distinguishable states.

```
        columns = 1
        for k in range(1, states):
            for j in range(columns):
                if matrix[k][j] == "0":
```
We traverse the lower diagonal looking for a cell with the value '0', as this represents a pair of states where it is still unknown whether they are distinguishable or equivalent.

```
for l in range(len(alphabet)):
                        x = functions[j, alphabet[l]]
                        y = functions[k, alphabet[l]]
                        if matrix[x][y] == "x" or matrix[y][x] == "x":
                            matrix[k][j] = "x"
                            iterator += 1
            columns += 1
```
For each character defined in the alphabet, we check if the resulting pair, defined by x and y (the values obtained from the transition function using dictionaries), leads to a marked pair. If so, it means that the pair (k, j) is distinguishable, so we mark it with an 'x' and increment the iterator.

```
columns = 1
    for k in range(1, states):
        for j in range(columns):
            if matrix[k][j] == "0":
                print(f"({j},{k})", end=" ")
        columns += 1
   print()
```
 Print the pairs of states that are not marked with "x" are the equivalent states



