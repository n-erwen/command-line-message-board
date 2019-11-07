""" Message Board 2019: Object-oriented version
    Not GUI yet though. Also no security whatsoever."""
import csv,sys,os,time,traceback,glob
from datetime import datetime
sys.path.append("./modules")
from strManipulation import title

def linebr():
    print("---------\n".center(70))

class MessageBoard(object):
    dir_path = "./" 
    password = "aesthetics"
    List = []

    def header(self,filename):
        print()
        out = "MESSAGE BOARD: "+str(filename.rstrip(".csv"))
        title(out)
    # close header

    # INITIALISATION
    def __init__(self):
        MessageBoard.List = self.findBoards()  #note: message boards MUST be csv files
        self.current = MessageBoard.List[0]
        self.abs_path = MessageBoard.dir_path+self.current
        self.msg_list = []
        self.refresh()
    # close init


    # OBTAIN + OVERWRITE CONTENTS OF CSV
    def refresh(self):
        self.msg_list.clear()
        msgFile = open(self.abs_path,mode = "r",newline="")
        reader = csv.reader(msgFile)
        msgCount = 0
        for row in reader:
            self.msg_list.append(row)
            msgCount += 1
        msgFile.close()
        
    # close refresh

    def overwrite(self):
        msgFile = open(self.abs_path,mode = "w",newline="")
        writer = csv.writer(msgFile)
        writer.writerows(self.msg_list)
        msgFile.close()
    # close toFile

    # READ BOARD
    def read(self):
        if not self.msg_list:
            title("[EMPTY]")
            return
        else:
            linebr()
            for mesg in self.msg_list:
                print(str(mesg[0]),"\n- "+str(mesg[1])+", "+str(mesg[2])+"\n")
        linebr()
    # close read
    


    #WRITE MESSAGE TO BOARD    
    def writeMsg(self):
        try:
            name = input("(Press Ctrl+C to go back)\nEnter your name: ")
            message = ""
            print("Enter your message: ",end="\n")
            while True:
                m = input()
                if m == "":
                    break
                else:
                    m = m+"\n"
                    message += m
            message = message.rstrip("\n")
            date = str(datetime.now())[0:19]
            self.msg_list.append([message,name,date])
            self.overwrite()
            print("[MESSAGE SUBMITTED]".center(70))
            linebr()
        except KeyboardInterrupt:
            linebr()
            return
    # close writeMsg


    #REMOVE MESSAGE FROM BOARD
    def removeMsg(self):
        print("""Which message would you like to remove?
(Press Ctrl+C to go back)
""")
        maxi = self.listMsgDetails()
        while True:
            try:
                i = int(input(">>> "))
                assert i>=1 and i<=maxi
                self.removeFromFile(i)
                break
            except AssertionError:
                print("INVALID OPTION")
            except ValueError:
                print("INVALID OPTION")
            except KeyboardInterrupt:
                linebr()
                return
        print("[MESSAGE REMOVED]".center(50))
        linebr()
    
    def removeFromFile(self,i):
        i = i-1
        del self.msg_list[i]
        self.overwrite()
        
    def listMsgDetails(self):
        c = 0
        for row in self.msg_list:
            i = self.msg_list.index(row)
            print(str(i+1) + '. ' + str(self.msg_list[i][2]))
            c+=1
        print()
        return c


    # CLEAR BOARD
    def clear(self):
        print("Are you sure you want to clear the message board? [Y/N]")
        while True:
            d = input(">>> ")
            d = d.lower()
            if d == "y" or d == "yes":
                file = open(self.abs_path,mode = "w")
                file.close()
                print()
                print("[CLEARED MESSAGE BOARD].".center(50))
                linebr()
                break
            elif d == "n" or d == "no":
                return
            else:
                print("INVALID OPTION")

    
    # PASSWORD PROTECTION
    def verify(self):
        print()
        print("[PASSWORD REQUIRED]".center(50))
        pwd = input("\nEnter password >>> ")
        print()
        if pwd == MessageBoard.password:
            print("[ACCESS GRANTED]".center(50))
            print("-----------------".center(50))
            return True
        else:
            print("[INCORRECT PASSWORD, ACESS DENIED]".center(50))
            print("----------------------------------".center(50))
            return False

    def info(self):
        print("\nFile:",os.path.basename(self.abs_path))
        print("Directory:",os.getcwd())
        self.refresh()
        print("No. of messages:",len(self.msg_list))
        if self.msg_list:
            if len(self.msg_list) == 2:
                print("Last message written on:",self.msg_list[1][2])
            else:
                print("Last message written on:",self.msg_list[-1][2])
        else:
            print("Last message written on: null")
        
        print("----------------".center(50))
        
    #MAIN MENU OPTIONS
    def options(self):
        self.header(self.current)
        print("""\nWould you like to:
1. Read the message board
2. Write a message
3. Remove a message
4. Clear the message board
5. Get board info
6. Switch message boards
(Press Ctrl+C to quit)
""")
        while True:
            try:
                opt = int(input(">>> "))
                assert opt>=1 and opt<=6
                self.select(opt)
                break
            except KeyboardInterrupt:
                print("QUIT PROGRAM".center(50))
                sys.exit()
            except AssertionError:
                print("INVALID OPTION")
            except ValueError:
                print("INVALID OPTION")
            except Exception:
                print("\nAN UNKNOWN ERROR OCCURED:")
                traceback.print_exc()
                sys.exit()
    # close options

    def select(self,opt):
        if opt == 1:
            self.refresh()
            self.read()
        elif opt == 2:
            self.writeMsg()
        elif opt == 3:
            if self.verify():
                self.removeMsg()
        elif opt == 4:
            if self.verify():
                self.clear()
        elif opt == 5:
            self.info()
        elif opt == 6:
            self.switchBoards()
    # close select

    def findBoards(self):
        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)
        os.chdir(dname)
        csvList = glob.glob("*.csv")
        return csvList 
    # close findBoards

    # SWITCH MESSAGE BOARDS
    def switchBoards(self):
        linebr()
        MessageBoard.List = self.findBoards()
        print("\nChoose the message board:\n")
        for i in range(len(MessageBoard.List)):
            print(str(i+1)+". "+MessageBoard.List[i].rstrip(".csv"))
        print()
        while True:
            try:
                x = int(input(">>> "))
                x = x-1
                assert x >= 0 and x<len(MessageBoard.List)
                break
            except AssertionError:
                print("INVALID OPTION")
            except ValueError:
                print("INVALID OPTION")
            except Exception:
                print("\nAN UNKNOWN ERROR OCCURED:")
                traceback.print_exc()
                sys.exit()
            # close except
        # close while
        self.current = MessageBoard.List[x]
        self.abs_path = MessageBoard.dir_path+self.current
        self.refresh()
    # close switchBoards

# main #
MsgBoard = MessageBoard()
while True:
    MsgBoard.options()
