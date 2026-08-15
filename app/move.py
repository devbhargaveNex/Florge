import shutil as s
import utls as u

ph = "./unsorted/"

def move(fileinfo):
    for ext , name in fileinfo.items():
        if ext in u.APPLICATION_EXTENSIONS:
            s.move(ph + name + ext,"./sorted/applications")
        elif ext in u.AUDIO_EXTENSIONS:
            s.move(ph + name + ext,"./sorted/audio")
        elif ext in u.DOCUMENT_EXTENSIONS:
            s.move(ph + name + ext,"./sorted/documents")
        elif ext in u.IMAGE_EXTENSIONS:
            s.move(ph + name + ext,"./sorted/images")
        elif ext in u.TEMP_EXTENSIONS:
            s.move(ph + name + ext,"./sorted/temp")
        elif ext in u.VIDEO_EXTENSIONS:
            s.move(ph + name + ext,"./sorted/videos")
        elif name == "":
            pass
        elif ext == ".dir":
            s.move(ph + name,"./sorted/Folders")
        else:
            s.move(ph + name + ext,"./sorted/others")
    return 'Operation Successful'