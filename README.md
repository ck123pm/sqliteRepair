# sqliteRepair
A tool for repairing sqlite database

# Repair Tool For Sqlite3
A tool for repairing sqlite database
## Environment
Windows 7

## Step1
### Directory Structure
```
├─RepairTool
│      dump.sql
│      read.sql
│      repair.exe
│      sqlite3.exe
```

## Step2
Copy the corrupt sqlite database file to this directory.

**Needed Files**
```
├─RepairTool
│      dump.sql
│      read.sql
│      repair.exe
│      sqlite3.exe
│      CorruptDB
```

## Step3
Open the command line in the current directory or use the `cd` command to this directory.

Then
```
D:\Tools\RepairTool>repair.exe CorruptDB NewDB
```
`Param1`: filename of the corrupt database file

`Param2`: filename of the new database file you want to export to

## Step4
Example
```
D:\Tools\RepairTool>repair.exe CorruptDB NewDB
INFO: Starting reparing, please wait for a while.
INFO: DumpSql is successful.
INFO: Modify last line is successful.
INFO: ReadSql is successful.
INFO: Delete TempFile is successful.
INFO: Reparing is successful!
```

Now the files should be like this:
```
├─RepairTool
│      dump.sql
│      read.sql
│      repair.exe
│      sqlite3.exe
│      CorruptDB
|      NewDB
```