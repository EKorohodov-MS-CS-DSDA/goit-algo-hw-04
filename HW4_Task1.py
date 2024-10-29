# Sorting. Homework 4. Task 1.
import timeit as tm
from HW4_utility import generate_array

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# === Tests ===
def asc_10000():
    return generate_array(10000, min_val=0, max_val=1000, noise=10, to_shuffle=False)

def desc_10000():
    return generate_array(10000, min_val=0, max_val=1000, noise=10, to_shuffle=False, order='desc')

def random_10000():
    return generate_array(10000, min_val=0, max_val=1000, noise=10, to_shuffle=True)

def asc_1000000():
    return generate_array(1000000, min_val=0, max_val=100000, noise=10, to_shuffle=False)

def desc_1000000():
    return generate_array(1000000, min_val=0, max_val=100000, noise=10, to_shuffle=False, order='desc')

def random_1000000():
    return generate_array(1000000, min_val=0, max_val=100000, noise=10, to_shuffle=True)

def main():

    # Run some tests
    tests = [random_10000, asc_10000, desc_10000]
    for test in tests:
        print(f"Running {test.__name__}...")
        print("Insertion sort:", tm.timeit(f"insertion_sort({test.__name__}())", globals=globals(), number=1))
        print("Merge sort:", tm.timeit(f"merge_sort({test.__name__}())", globals=globals(), number=1))
        print("Timsort:", tm.timeit(f"sorted({test.__name__}())", globals=globals(), number=1))

    # Run some bigger tests (only for Merged Sort and Timsort)
    tests = [random_1000000, asc_1000000, desc_1000000]
    for test in tests:
        print(f"Running {test.__name__}...")
        print("Merge sort:", tm.timeit(f"merge_sort({test.__name__}())", globals=globals(), number=1))
        print("Timsort:", tm.timeit(f"sorted({test.__name__}())", globals=globals(), number=1))

# === Results ===
# For 10000 shuffled elements:
# Insertion sort: 2.1915673999974388
# Merge sort: 0.03555860000051325
# Timsort: 0.01220150000153808

# For sorting 10000 ascending elements:
# Insertion sort: 0.05031079999753274
# Merge sort: 0.03068409999832511
# Timsort: 0.00819249999767635

# For sorting 10000 descending elements:
# Insertion sort: 4.123069000001124
# Merge sort: 0.029685000001336448
# Timsort: 0.009960200004570652

# Repeat tests for 1M elements (obviously, without Insertion sort):

# For 1000000 shuffled elements:
# Merge sort: 5.162219499994535
# Timsort: 1.6204223999957321

# For sorting 1000000 ascending elements:
# Merge sort: 3.6016471999973874
# Timsort: 0.8977780999994138

# For sorting 10000 descending elements:
# Merge sort: 3.6197477000023355
# Timsort: 0.9179946000003838

if __name__ == '__main__':
    main()