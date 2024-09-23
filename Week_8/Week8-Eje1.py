def order_songs(origin_path, destination_path):
    with open(origin_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    sorted_lines = sorted(lines)
    with open(destination_path, 'w', encoding='utf-8') as file:
        file.writelines(sorted_lines)

order_songs('test.txt', 'output.txt')
