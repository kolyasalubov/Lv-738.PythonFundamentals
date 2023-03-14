def get_largest_number(a, b):
    """
    Ця функція приймає два числа на вхід та повертає найбільше з них.
    Якщо вони однакові, то функція повертає негативний перший параметр

    Args:
    a (int або float): перше число
    b (int або float): друге число

    Returns:
    int або float: найбільше число
    """
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return a * -1
    
print(get_largest_number(24,45))
print(get_largest_number(10,5))
    
