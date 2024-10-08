def custom_write(file_name, strings):
    
    strings_positions = {}


    with open(file_name, 'w', encoding='utf-8') as file:
        for index, string in enumerate(strings, start=1):

            start_position = file.tell()


            file.write(string + '\n')


            strings_positions[(index, start_position)] = string


    return strings_positions



strings_to_write = ['Text for tell.', 'Используйте кодировку utf-8.']
result = custom_write('output.txt', strings_to_write)
print(result)