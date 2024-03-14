import numpy as np

# Constants
VECTOR_1 = np.array([1, 2])
SAME_VECTOR = np.array([1, 2])
RECTANGULAR_ARRAY = np.arange(15).reshape(3, 5)
REPEATED_VALUES_ARRAY = np.array([[1, 2, 3, 4, 5],
                                  [1, 2, 3, 4, 5],
                                  [1, 2, 3, 4, 5]])


def print_vector_info(vector_name, vector):
    print(f"{vector_name} = {vector}")
    print(f"{vector_name}.shape = {vector.shape}")


def perform_operations_on_vectors(vector1, vector2):
    print(f"Dot product of vectors: {np.dot(vector1, vector2)}")
    print(f"Element-wise multiplication of vectors: {np.multiply(vector1, vector2)}")


def perform_operations_on_arrays(array1, array2):
    print(f"Dot product of arrays: {np.dot(array1, array2.T)}")
    print(f"Matrix multiplication of arrays: {np.matmul(array1, array2.T)}")


def main():
    print_vector_info("Vector 1", VECTOR_1)
    print_vector_info("Vector 2", SAME_VECTOR)
    perform_operations_on_vectors(VECTOR_1, SAME_VECTOR)

    print(f"Rectangular Shape Array = {RECTANGULAR_ARRAY}, ndim = {RECTANGULAR_ARRAY.ndim}")

    perform_operations_on_arrays(RECTANGULAR_ARRAY, REPEATED_VALUES_ARRAY)

    single_dimensional_vector = np.array([1, 2, 3, 4])
    reshaped_vector = single_dimensional_vector.reshape((-1, 1))
    print(f"reshaped_vector = {reshaped_vector}")


if __name__ == "__main__":
    main()