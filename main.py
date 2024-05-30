from sparse_matrix import SparseMatrix

def main():
    print("Select the operation you want to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    choice = input("Enter your choice (1/2/3): ")

    file1 = input("Enter the path of the first matrix file: ")
    file2 = input("Enter the path of the second matrix file: ")

    matrix1 = SparseMatrix(file1)
    matrix2 = SparseMatrix(file2)

    if choice == '1':
        result = matrix1 + matrix2
    elif choice == '2':
        result = matrix1 - matrix2
    elif choice == '3':
        result = matrix1 * matrix2
    else:
        print("Invalid choice")
        return

    print("Resultant Matrix:")
    print(result)

if __name__ == "__main__":
    main()

