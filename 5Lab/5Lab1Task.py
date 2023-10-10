import numpy as np

def create_matrix(N):
    diag_values = np.arange(0, N-1) * 2 - 2
    A = np.diag(5 * np.ones(N)) + np.diag(diag_values, k=1)
    A[:, 0] = 6

    B = np.eye(N)

    C = np.zeros((N, N))

    D = np.exp(A)
    
    top_block = np.concatenate((A, B), axis=1)
    bottom_block = np.concatenate((C, D), axis=1)
    result_matrix = np.concatenate((top_block, bottom_block), axis=0)
    
    return result_matrix

while True:
    try:
        N = int(input("Enter an integer N: "))
        break
    except ValueError:
        print("Invalid input. Please try again with an integer.")

# Clear the file before writing new results
open("5Lab1Task_result.txt", "w", encoding="cp1251").close()

result_matrix = create_matrix(N)
# Find eigenvalues and eigenvectors of matrix A
eigenvalues, eigenvectors = np.linalg.eig(result_matrix)

# Find the smallest eigenvalue and its corresponding eigenvector
min_eigenvalue_index = np.argmin(np.abs(eigenvalues))
min_eigenvalue = eigenvalues[min_eigenvalue_index]
min_eigenvector = eigenvectors[:, min_eigenvalue_index]

# Check if Ax = λx holds for the smallest eigenvalue and its eigenvector
Ax = np.dot(result_matrix, min_eigenvector)
if np.allclose(Ax, min_eigenvalue * min_eigenvector):
    with open("5Lab1Task_result.txt", "a", encoding="cp1251") as f:
        f.write("Eigenvalues of matrix A:\n")
        eigenvalues_str = np.array2string(eigenvalues, precision=2, suppress_small=True, separator='\t')
        f.write(eigenvalues_str + "\n")
        f.write("\nEigenvectors of matrix A:\n")
        eigenvectors_str = np.array2string(eigenvectors, precision=2, suppress_small=True, separator='\t')
        f.write(eigenvectors_str + "\n")
        f.write("\nSmallest eigenvalue in magnitude:\n")
        f.write(f"{min_eigenvalue:.2f}\n")
        f.write("\nCorresponding eigenvector:\n")
        min_eigenvector_str = np.array2string(min_eigenvector, precision=2, suppress_small=True, separator='\t')
        f.write(min_eigenvector_str + "\n")
        f.write("\nThe equation Ax = lambda * x holds for the smallest eigenvalue and its eigenvector.\n")
else:
    with open("5Lab1Task_result.txt", "a", encoding="cp1251") as f:
        f.write("Eigenvalues of matrix A:\n")
        eigenvalues_str = np.array2string(eigenvalues, precision=2, suppress_small=True, separator='\t')
        f.write(eigenvalues_str + "\n")
        f.write("\nEigenvectors of matrix A:\n")
        eigenvectors_str = np.array2string(eigenvectors, precision=2, suppress_small=True, separator='\t')
        f.write(eigenvectors_str + "\n")
        f.write("\nSmallest eigenvalue in magnitude:\n")
        f.write(f"{min_eigenvalue:.2f}\n")
        f.write("\nCorresponding eigenvector:\n")
        min_eigenvector_str = np.array2string(min_eigenvector, precision=2, suppress_small=True, separator='\t')
        f.write(min_eigenvector_str + "\n")
        f.write("\nThe equation Ax = lambda * x does not hold for the smallest eigenvalue and its eigenvector.\n")


