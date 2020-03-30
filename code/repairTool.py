import os
import sys

class Repair(object):
    __oldFile= __newFile=__path=__tmpFile=__tmpFilePath= ""

    def __init__(self, *args, **kwargs):
        self.__oldFile = kwargs["oldFile"]
        self.__newFile = kwargs["newFile"]
        self.__path = os.path.dirname(os.path.realpath(__file__))
        self.__tmpFile = "tmp.sql"
        self.__tmpFilePath = self.__path+"\\"+self.__tmpFile

    def doRepair(self):
        print("INFO: Starting reparing, please wait for a while.")
        self.__dumpSql()
        print("INFO: DumpSql is successful.")
        self.__modLastLine()
        print("INFO: Modify last line is successful.")
        self.__readSql()
        print("INFO: ReadSql is successful.")
        self.__delTmp()
        print("INFO: Delete TempFile is successful.")
        print("INFO: Reparing is successful!")
    
    def __dumpSql(self):
        cmd = "cd "+self.__path+"&"+self.__path[0:2]+"&"+'''\
        sqlite3.exe {oldFile}<dump.sql'''.format(oldFile = self.__oldFile)
        os.system(cmd)

    def __readSql(self):
        cmd = "cd "+self.__path+"&"+self.__path[0:2]+"&"+'''\
        sqlite3.exe {newFile}<read.sql'''.format(newFile = self.__newFile)
        os.system(cmd)

    def __delTmp(self):
        cmd = "cd "+self.__path+"&"+self.__path[0:2]+"&"+'''\
        del {tmpFile}'''.format(tmpFile=self.__tmpFile)
        os.system(cmd)

    def __modLastLine(self):
        with open(self.__tmpFilePath,"rb+") as f:
            fsize = os.path.getsize(self.__tmpFilePath)
            offset = -8
        
            while -1*offset <fsize:
                f.seek(offset ,os.SEEK_END)
                lines = f.readlines()
                if len(lines) >=2:
                    last_line_len = len(lines[-1])
                    f.seek(-last_line_len,os.SEEK_END)
                    f.truncate()
                    f.write(b"Commit;")
                    return
                else:
                    offset*=2

if __name__ == "__main__":
    # 参数不为3，认为参数有误
    if len(sys.argv) !=3:
        print("Params are invalid, please enter the correct params.\ne.g.[repair.exe oldfilename newfilename]")
    else:
        repair = Repair(oldFile = sys.argv[1], newFile = sys.argv[2])
        repair.doRepair()