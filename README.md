# Minimization Algorithm

## Contents
- [Team](#team)
- [Development environment](#development-environment)
- [Instructions for running](#instructions-for-running)
- [Explanation of the algorithm](#explanation-of-the-algorithm)

## Team
- Laura Andrea Castrillón Fajardo
- Samuel Martínez Arteaga

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
   # Mark the matrix with "x" for every pair composed of a initial state or (XOR) a final state
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
Realize the step 1:  Mark {p, q} if p ∈ F and q ∉ F or vice versa. The variables k, j represent states, if k or j belong to a finalStates (array of final states) Las variables k, j representan los estados, si k o j, siendo este o excluyente (XOR), es decir, k ∈ F pero j ∉ F o viceversa, entonces marca esta casilla con un "x"