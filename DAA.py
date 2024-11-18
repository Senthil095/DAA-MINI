def is_safe(board, row, col, N):
    
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def place_components_util(board, row, N, solutions):
    
    if row == N:
        solution = []
        for i in range(N):
            row_result = ['.'] * N
            row_result[board[i]] = 'C'  
            solution.append(' '.join(row_result))
        solutions.append(solution)
        return
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col  
            place_components_util(board, row + 1, N, solutions)
            board[row] = -1  

def circuit_design_verification(N):
    
    if N < 1:
        print("Please enter a positive integer for N.")
        return
    
    board = [-1] * N
    solutions = []
    
    place_components_util(board, 0, N, solutions)
    
    if solutions:
        print(f"Valid Circuit Placements for N = {N}:")
        print_solutions(solutions)
    else:
        print(f"No valid placement exists for {N} components.")

def print_solutions(solutions):
    """
    Prints all valid circuit placements.
    """
    solution_number = 1
    for solution in solutions:
        print(f"Placement {solution_number}:")
        for row in solution:
            print(row)
        print()
        solution_number += 1

try:
    N = int(input("Enter the number of components (N) to place in the circuit: "))
    circuit_design_verification(N)
except ValueError:
    print("Please enter a valid integer.")
