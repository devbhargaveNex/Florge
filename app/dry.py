import utls as u

def dryrun(fileinfo):
    for ext , name in fileinfo.items():
        if ext in u.APPLICATION_EXTENSIONS:
            print(f'{name}{ext} will be in Applications')
        elif ext in u.AUDIO_EXTENSIONS:
            print(f'{name}{ext} will be in Audio')
        elif ext in u.DOCUMENT_EXTENSIONS:
            print(f'{name}{ext} will be in Documents')
        elif ext in u.IMAGE_EXTENSIONS:
            print(f'{name}{ext} will be in Images')
        elif ext in u.TEMP_EXTENSIONS:
            print(f'{name}{ext} will be in Temp')
        elif ext in u.VIDEO_EXTENSIONS:
            print(f'{name}{ext} will be in Videos')
        elif name == "":
            print(f'{name}{ext} will be ignored')
        elif ext == ".dir":
            print(f'{name}{ext} will be in Folders')
        else:
            print(f'{name}{ext} will be in Others')
    return "end"