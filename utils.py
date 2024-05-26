def append_number_to_file(number, file_path):
    with open(file_path, 'a') as file:
        file.write(f"{number}\n")

def read_next_three_ints(file_obg):
    line = file_obg.readline().strip()
    a, b, c = map(int, line.split())
    return [a, b, c]

def read_next_int(file_obj):
    return int(file_obj.readline().strip())