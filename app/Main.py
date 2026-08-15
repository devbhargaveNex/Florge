import scan as s
import detect as d
import move as m
import operations as o
import dry


root = './unsorted'
files = s.scan(root)
fileinfo = d.detect(files)
finallist,operation = o.operate(fileinfo,files)
if operation == "move":
    fileinfo = d.detect(finallist)
    result = m.move(fileinfo)
    print(result)