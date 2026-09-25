from pathlib import Path


def detect(files):
    fileinfo = {}
    for file in files:
        if file[0] != '.':
            if '.' in file:
                info = Path(file)
                if info.suffix in fileinfo.keys():
                    lst = fileinfo[info.suffix]
                    lst.append(info.stem)
                    fileinfo[info.suffix] = lst
                else:
                    fileinfo[info.suffix] = [info.stem]
            else:
                if '.dir' in fileinfo.keys():
                    lst = fileinfo['.dir']
                    lst.append(file)
                    fileinfo['.dir'] = lst
                else:
                    fileinfo['.dir'] = [file]
    return fileinfo