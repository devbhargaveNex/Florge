import detect as d
import dry
def operate(fileinfo,files):
    size = 0
    for keys in fileinfo.keys():
        size += len(fileinfo[keys])
    print(f"No. of files found {size}")
    choice = 0
    finallist = files
    state="Inital"
    while choice != '4' and choice != '5':
        print("1.Show files\n2.Remove files\n3.DRY Run\n4.Move files\n5.Exit")
        choice = input("_")
        if choice == '1':
            if state == "Inital":
                for ext , name in fileinfo.items():
                    print(f"Name of file is {name} and it is a {ext}")
            elif state == "edited":
                fileinfo = d.detect(finallist)
                for ext , name in fileinfo.items():
                    print(f"Name of file is {name} and it is a {ext}")
        elif choice == '2':
            rmfiles = input("enter files to remove with name and ext: ")
            rmfiles = rmfiles.split(",")
            for files in rmfiles:
                finallist.remove(files)
            state = "edited"
        elif choice == '3':
            fileinfo = d.detect(finallist)
            dry.dryrun(fileinfo)
        elif choice == '4':
            operation = "move"
        elif choice == '5':
            operation = None
    return finallist , operation