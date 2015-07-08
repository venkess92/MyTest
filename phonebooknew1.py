import shelve
DTB=shelve.open("addressbookdata.db")
def search_database (searchcriteria ):
    
    for line in DTB.itervalues():
        if searchcriteria in line:
            print ("\n")
            print line
            print ("\n")
            break
    else:
        print "zero results"
def db (info):
    
    DTB[str(hash(info))]=info
    print ("The record was added to the database address book ")
def collect ():
    
    firstname = raw_input("What is the persons first name? ")
    phone = raw_input("What id the persons phone number? ")
    info = (firstname + "," + phone)
    db (info)
def menu ():
    answer = raw_input("\n Type '1' to create new contact \n Or type '2' to search available contact ")
    if answer == "1":
        collect()
    if answer == "2":
        searchcriteria = raw_input("What do you want to search? ")
        search_database(searchcriteria)
    
    else:
        print str(answer) + " pls type again"
        menu()
menu ()