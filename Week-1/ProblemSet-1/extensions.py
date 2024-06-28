get_input = input('File Name: ').strip().casefold()
get_ext = get_input.split('.')[-1]

match get_ext:
    case 'gif' | 'png':
        print(f'image/{get_ext}')
    case 'jpg' | 'jpeg':
        print('image/jpeg')
    case 'pdf' | 'zip':
        print(f'application/{get_ext}')
    case 'txt':
        print('text/plain')
    case _:
        print('application/octet-stream')

    
"""
split_name = get_input.split('.')[-1]

match split_name:
    case 'gif' | 'jpg' | 'jpeg' | 'png':
        print(f'image/{split_name}')
    case 'pdf' | 'txt' | 'zip':
        print(f'application/{split_name}')
    case _:
        print('application/octet-stream')
"""