def find_two_numbers_add_up(arr, total):
    known_numbers = set()
    for number in arr:
        if number in known_numbers:
            return True
        known_numbers.add(total - number)
    return False

if __name__ == "__main__":
    k = 17
    x = [10, 15, 3, 7]
    print(find_two_numbers_add_up(x, k))
    