from time import gmtime, strftime

def WriteLogging(action):

    # open file
    f = open("LogFile.txt", "a+")

    # write line in logfile
    date_str = strftime("%a, %d %b %Y %H:%M:%S", gmtime())

    f.write(" \n")
    f.write("--------------------------------------------------------------------\n")
    f.write(date_str + " " + action + "\n")
    f.write("--------------------------------------------------------------------\n")
    f.write("test a\n")
    f.write("test b\n")
    f.write("test c\n")

    # close file
    f.close()

