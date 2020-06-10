def multiply_array(arr):
    multi = 1
    final_arr = []
    for number in arr:
        multi *= number
        
    for number in arr:
        final_arr.append(multi//number)

    return final_arr

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    multiplied_arr = multiply_array(arr)
    print(multiplied_arr)