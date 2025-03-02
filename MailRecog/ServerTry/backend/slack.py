import slack_sdk

def writeToNamesFile(name, fname = "../../names.txt"): # Will need changing
    f = open(fname, "a")
    # Do preprocessing?
    f.write(name.upper().strip(" "))
    f.close()

# def removeName(name, fname = "/Users/anandtekkey/macGitRepo/MailBoxCompVis/MailRecog/names.txt"): # Will need changing
#     return

# def fullActionGetName():
#     return
# writeToNamesFile("Me 32")