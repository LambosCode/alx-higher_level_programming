0.current_working_directory The script print absolute path of current path. unlike __pwd_ _it uses "readlink -f filename" to priint the full path. in collaboration with "dirname" __dirname" AND "XARGS" _Same thing can be accomplished readlink -f filename | xargs dirname"

1-listit the script implores "ls" to itemize contain of a particular dir

2-bring-me-home This script uses cd ~ the "~" specifies for home directory on linux. This has to be executed with "source" keyword. e.g source ./2-bring_me_home

3-list-files. The helps with the details of a file. such read, write and execute permission and the group/user/others they belong to time and date of when the foile or folder is created.

4
