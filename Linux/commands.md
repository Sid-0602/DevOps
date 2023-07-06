# LINUX COMMANDS AND OPERATIONS
 
1. Basics CLI Commands.
2. Understanding files in Linux.
3. Filters and Redirection
4. Users and Group.
5. Sudo 
6. Software management.
7. Services and Processes.
8. Advanced commands.
9. Server Managements.


## Linux Directories

![Alt text](image.png)

![Alt text](image-5.png)

The file Structure of linux with the extensions is:
![Alt text](image-1.png)


## Commands and File Systems

1. The following commands checks for the current directory, os release etc.
![Alt text](image-2.png)

2. sudo -i command will switch us to root directory.

![](image-3.png)

3. This is top level directory for UNIX OS

![Alt text](image-4.png)

Note: /bin is absolute path.

4. Linux Command Syntax
    -- [command] [options] [arguments]
    eg: cp -r filetobecopied destinationPath

    Note: [command] --help to get to more about an command.

5. Most Used Linux commands to be used: https://www.javatpoint.com linux-commandsJavaPoint

6. Note: Be very careful while using [rm -rf *] command, as it deletes all present directories in the current workig directories and it do not have any backup.


## VIM EDITOR

Vim is a Unix text editor that's included in Linux, BSD, and macOS. It's known for being fast and efficient, in part because it's a small application that can run in a terminal (although it also has a graphical interface), but mostly because it can be controlled entirely with the keyboard with no need for menus or a mouse.

VIM has 3 modes:
    -- Command Mode.
    -- Insert Mode. (edit mode).
    -- extended command Mode.

![Alt text](image-6.png)

![Alt text](image-7.png)
![Alt text](image-8.png)

## Types of Files in Linux 

In Linux, everything is considered as a file. In UNIX, seven standard file types are regular, directory, symbolic link, FIFO special, block special, character special, and socket. In Linux/UNIX, we have to deal with different file types to manage them efficiently.

In Linux/UNIX, Files are mainly categorized into 3 parts:
    -- Regular Files
    -- Directory Files
    -- Special Files

    Note: ls -l command gives long listing of existing files in current dict.

![Alt text](image-9.png)

-- Making entire Directorty Structure : [mkdir -p [directory absolute path]].
![Alt text](image-10.png)

### Soft Link in file systems

![Alt text](image-11.png)

If we change the path of file, the link becomes dead.

![Alt text](image-12.png)

To remove the link:

![Alt text](image-13.png)

