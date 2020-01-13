from subprocess import Popen, PIPE
import sys

def runGitCommand(command):
    git_process=Popen(command, stdout=PIPE, stderr=PIPE)
    (status,error)=git_process.communicate()
    git_process.wait()
    return

def addFiles():
    f=open("test.txt","w+")
    f.write("test")
    f.close

def createGitBranchAndPush():
    checkoutToMasterCommand=['git','checkout','master']
    runGitCommand(checkoutToMasterCommand)
    branchCommand=['git','branch','1']
    checkoutCommand=['git','checkout','1']
    addCommand=['git','add','.']
    commitCommand=['git','commit','-m','asdf']
    pushCommand=['git','push','origin','1']
    runGitCommand(branchCommand)
    runGitCommand(checkoutCommand)
    runGitCommand(addCommand)
    runGitCommand(commitCommand)
    runGitCommand(pushCommand)
    runGitCommand(checkoutToMasterCommand)

def changeFiles():
    checkoutToMasterCommand=['git','checkout','master']
    runGitCommand(checkoutToMasterCommand)
    f=open("test.txt","w+")
    f.write("test2")
    f.close
    branchCommand=['git','branch','2']
    checkoutCommand=['git','checkout','2']
    addCommand=['git','add','.']
    commitCommand=['git','commit','-m','asdf2']
    pushCommand=['git','push','origin','2']
    runGitCommand(branchCommand)
    runGitCommand(checkoutCommand)
    runGitCommand(addCommand)
    runGitCommand(commitCommand)
    runGitCommand(pushCommand)
    runGitCommand(checkoutToMasterCommand)

addFiles()
createGitBranchAndPush()
changeFiles()
sys.exit(0)
