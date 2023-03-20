""" Akshat Kumar 10/1/2022
This program implements a the search function seen in file systems using a tree and traversing via Depth First Search and Breadth First Search
This program uses a test tree made with dummy variables as practice for DFS and BFS
The DFS implementation uses recursion and the BFS implementation uses a queue
"""

#declaring the standard node for the tree which can either be a folder or a file
class treeNode:
    
    def __init__(self, initFileType, initFileName, initChildren, initParent):
        self.fileType = initFileType
        self.fileName = initFileName
        self.children = initChildren
        self.parent = initParent

#tree class
class tree:
    
    def __init__(self, initRoot):
        self.root = initRoot
        
#function that gets all the parents of a file and adds them into a list using recursion
def findParents(node, parents):
    #if the highest parent is found, add parent to list and return list
    if(node.parent == None):
        parents.append(node.fileName)
        return parents
    #if the file has a parent, add the parent to list and recursively call function
    else:
        parents.append(node.fileName)
        return findParents(node.parent, parents)
    
#function that returns the path of a file in the correct path format
def generatePath(node):
    parents = []
    pathString = ""
    #get a list of all the parents of a file 
    path = findParents(node, parents)
    
    #flip the path list and add / between every file or folder
    for i in range(len(path)):
        pathString = pathString + "/" + str(path[len(path)-1-i])
    return pathString
    
      
#global variable to store values in the recursive DFS function
dfsList = []

#depth first search using recursion
def DFS(c):
    #check for children, if there are none then add node to list
    if(c.children == None):
        dfsList.append(c)
    
    #if the node has a child then add node and recursively call function for each child
    else:
        dfsList.append(c)
        for i in range(len(c.children)):
            DFS(c.children[i])           
        
#breadth first search using a queue approach
def BFS(c):
    #add root to list
    allNodes = [c]
    
    #iterate through the list untill the end is reached
    for i in allNodes:
        #if the node has a child add every child to the end of the list (enqueue into a queue)
        if(i.children != None):   
            for j in range(len(i.children)):
                allNodes.append(i.children[j])
                
    #return the final list
    return allNodes
       
        
#Creating test tree nodes
#parents/folders are initialized first with empty children
#children are initialized later with their parent as an attribute
#children are then added to the parent's children attribute 
homeDirectory = treeNode("Folder", "homeDirectory", None, None)            

imagesFolder = treeNode("Folder", "imageFolder", None, homeDirectory)

workFolder = treeNode("Folder", "workFolder", None, homeDirectory)
            
homeworkFolder = treeNode("Folder", "homeworkFolder", None, imagesFolder)

homework1 = treeNode("jpg", "jpeg1.jpg", None, homeworkFolder)
homework2 = treeNode("pdf", "homework2.pdf", None, homeworkFolder)
homework3 = treeNode("jpg", "jpeg3.jpg", None, homeworkFolder)
homework4 = treeNode("pdf", "homework4.pdf", None, homeworkFolder)
homework5 = treeNode("jpg", "jpeg5.jpg", None, homeworkFolder)

compsciIA = treeNode("Folder", "compsciIA", None, homeworkFolder)

critA = treeNode("pdf", "critA.pdf", None, compsciIA)
critB = treeNode("pdf", "critB.pdf", None, compsciIA)
critC = treeNode("pdf", "critC.pdf", None, compsciIA)
critD = treeNode("mov", "critD.mov", None, compsciIA)
critE = treeNode("pdf", "critE.pdf", None, compsciIA)
recordOfTasks = treeNode("pdf", "recordOfTasks.pdf", None, compsciIA)

compsciIA.children = [critA, critB, critC, critD, critE, recordOfTasks]

homeworkFolder.children = [compsciIA, homework1, homework2, homework3, homework4, homework5]

schoolWorkFolder = treeNode("Folder", "schoolWorkFolder", None, imagesFolder)

school1 = treeNode("png", "png1.png", None, schoolWorkFolder)
school2 = treeNode("png", "png2.png", None, schoolWorkFolder)
school3 = treeNode("pdf", "school3.pdf", None, schoolWorkFolder)
school4 = treeNode("png", "png4.png", None, schoolWorkFolder)
school5 = treeNode("png", "png5.png", None, schoolWorkFolder)
school6 = treeNode("pdf", "school6.pdf", None, schoolWorkFolder)

schoolWorkFolder.children = [school1, school2, school3, school4, school5, school6]

imagesFolder.children = [homeworkFolder, schoolWorkFolder]

pdfFolder = treeNode("Folder", "pdfFolder", None, workFolder)

pdf1 = treeNode("pdf", "pdf1.pdf", None, pdfFolder)
pdf2 = treeNode("pdf", "pdf2.pdf", None, pdfFolder)
pdf3 = treeNode("pdf", "pdf3.pdf", None, pdfFolder)
pdf4 = treeNode("pdf", "pdf4.pdf", None, pdfFolder)
pdf5 = treeNode("pdf", "pdf5.pdf", None, pdfFolder)

pdfFolder.children = [pdf1, pdf2, pdf3, pdf4, pdf5]

text1 = treeNode("txt", "text1.txt", None, workFolder)
text2 = treeNode("pdf", "text2.pdf", None, workFolder)
text3 = treeNode("txt", "text3.txt", None, workFolder)
text4 = treeNode("pdf", "text4.pdf", None, workFolder)

workFolder.children = [pdfFolder, text1, text2, text3, text4]

homeDirectory.children = [workFolder, imagesFolder]

#constructing test tree
fileTree = tree(homeDirectory)

#main class were dfs and bfs are called
class main():
    #construct the tree
    rootNode = fileTree.root
    
    #search through the tree with dfs
    DFS(rootNode)
    #print the all the pdfs of the tree with their path
    for i in range(len(dfsList)):
        if(dfsList[i].fileType == "pdf"):
            print(str(dfsList[i].fileName) + " " +  str(generatePath(dfsList[i])))
    
    print("–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")
        
    #search through the tree with bfs
    bfsList = BFS(rootNode)
    #print the all the pdfs of the tree with their path
    for i in range(len(bfsList)):
        if(bfsList[i].fileType == "pdf"):
            print(str(bfsList[i].fileName) + " " +  str(generatePath(dfsList[i])))
    


        
        

    
        
