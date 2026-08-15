import detect as d
import dry
def operate(fileinfo,files):
    print(f"No. of files found {len(fileinfo)}")
    choice = 0
    finallist = files
    state="Inital"
    while choice != '4':
        print("1.Show files\n2.Remove files\n3.DRY Run\n4.Move files")
        choice = input("_")
        if choice == '1':
            if state == "Inital":
                for ext , name in fileinfo.items():
                    print(f"Name of file is {name} and it is a {ext}")
                    print(f"No. of files found {len(fileinfo)}")
            elif state == "edited":
                fileinfo = d.detect(finallist)
                for ext , name in fileinfo.items():
                    print(f"Name of file is {name} and it is a {ext}")
                    print(f"No. of files found {len(fileinfo)}")
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
    return finallist , operation