import numpy as np
def get_matrix_input(name):
    print(f"Enter the dimensions of {name} (rows, columns):")
    rows, cols = map(int, input().split())
    print(f"Enter the elements of {name} row by row, separated by spaces:")
    elements = []
    for _ in range(rows):
        elements.append(list(map(float, input().split())))
    return np.array(elements)
def display_menu():
    print("\nMatrix Operations Tool")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("6. Exit")
    return int(input("Choose an operation (1-6): "))
def main():
    while True:
        choice = display_menu()

        if choice in [1, 2, 3]:
            matrix_a = get_matrix_input("Matrix A")
            matrix_b = get_matrix_input("Matrix B")

            if matrix_a.shape != matrix_b.shape and choice in [1, 2]:
                print("Error: Matrices must have the same dimensions for addition or subtraction.")
                continue

            if choice == 1:
                print("\nResult of Addition:")
                print(matrix_a + matrix_b)
            elif choice == 2:
                print("\nResult of Subtraction:")
                print(matrix_a - matrix_b)
            elif choice == 3:
                if matrix_a.shape[1] != matrix_b.shape[0]:
                    print("Error: Number of columns in Matrix A must equal the number of rows in Matrix B for multiplication.")
                    continue
                print("\nResult of Multiplication:")
                print(np.dot(matrix_a, matrix_b))

        elif choice == 4:
            matrix = get_matrix_input("Matrix")
            print("\nTranspose of the Matrix:")
            print(matrix.T)

        elif choice == 5:
            matrix = get_matrix_input("Matrix")
            if matrix.shape[0] != matrix.shape[1]:
                print("Error: Determinant can only be calculated for square matrices.")
                continue
            print("\nDeterminant of the Matrix:")
            print(np.linalg.det(matrix))

        elif choice == 6:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid operation.")
if __name__ == "__main__":
    main()
