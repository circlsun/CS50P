name = input('File name: ').strip().lower()

match name[-4:]:
    case '.jpg' | 'jpeg':
        print('image/jpeg')
    case '.gif':
        print('image/gif')
    case '.png':
        print('image/png')
    case '.pdf':
        print('application/pdf')
    case '.zip':
        print('application/zip')
    case '.txt':
        print('text/plain')
    case _:
        print('application/octet-stream')
