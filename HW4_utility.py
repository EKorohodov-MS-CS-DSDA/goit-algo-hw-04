import random

def generate_array(size, min_val=0, max_val=100, noise=0, to_shuffle=True, order='asc'):
    """
    Generates an array of a given size with random numbers in a given range.

    :param size: The size of the array to generate
    :param min_val: The minimum value of the range
    :param max_val: The maximum value of the range
    :param noise: The amount of random noise to add to each number
    :param to_shuffle: Whether to shuffle the array after generation
    :param order: The order in which to sort the array (asc or desc)
    :return: The generated array
    """
    data = []
    # Use order for the array data generation
    if order == 'asc':
        # min + i * step
        data = [min_val + i * (max_val - min_val) // (size - 1) for i in range(size)]
    elif order == 'desc':
        # max - i * step
        data = [max_val - i * (max_val - min_val) // (size - 1) for i in range(size)]
    else:
        raise ValueError("order must be 'asc' or 'desc'")
    
    # Clamp values between min_val and max_val
    for i in range(len(data)):
        data[i] = max(min_val, min(max_val, data[i] + random.randint(-noise, noise)))

    # Shuffle the array
    if to_shuffle:
        random.shuffle(data)
    return data