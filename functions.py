FILEPATH= "todos.txt" #IT IS A GOOD HABIT TO WRITE YOUR DEFAULT ARGUMENTS INTO VARIABLES SO THAT WHEN YOU CHANGE THEM, YOU DON'T HAVE TO GO INTO ALL THE FUNCTIONS YOU'VE USED IT
def file_open(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items as the output. """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def file_write(listname_arg, filepath_arg=FILEPATH):
    """ Open the text file as the write mode and write the specified list into it"""
    with open(filepath_arg, 'w') as file_local:
        file_local.writelines(listname_arg)


#WE WANT TO GET A PRINT CODE EXECUTED ONLY WHEN THIS STRING IS RUN FROM INSIDE THE ORIGINAL FILE - NOT WHEN IMPORTED
if __name__ == "__main__": #here we are using a hiddenly defined variable in Python
    print("You are using the original script.")
