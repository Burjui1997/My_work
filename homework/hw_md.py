def read_my_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return None
    except IOError:
        return 'Ошибка чтения файла'


def split_md_file(md_str):
    lines = md_str.split('\n')
    headers = []
    for line in lines:
        if line.startswith('#'):
            headers.append(line.strip())
    return headers


def write_md_file(string,filename):
    with open(filename, 'w') as file:
        file.write(string)
        