from pathlib import Path


def detect(files):
    fileinfo = {}
    for file in files:
        if file[0] != '.':
            if '.' in file:
                info = Path(file)
                fileinfo[info.suffix] = info.stem
            else:
                fileinfo['.dir'] = file
    return fileinfo