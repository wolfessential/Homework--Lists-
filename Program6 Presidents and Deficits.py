#!/usr/bin/env python3
#Names: James Wolf
#Date:  10/30/2017
#Program6 Presidents and Deficits

#diplay menu

def displayMenu():
    flag = True
    while flag:

        print()
        print("Deficit List")
        print("\tList - List the Presidents.")
        print("\tShow - List the Deficits.")
        print("\tAdd - Add a President.")
        print("\tDraw - Draw a Histogram.")
        print("\tQuit - End Application.")

        item = input("Enter command first letter: ").lower()
        if item == "l" or item == "s" or item == "a" or item == "d" or item == "q":
            flag = False
        else:
            print("Error: Invalid input " + ("(")+ item + (")"))
            

    return item.lower()

#---------------------------function--------------------------------
#Name: ListPresidents(presidents)
#Purpose: Will print the list of presidents names list found in main

def ListPresidents(presidents):
    print("List of Presidents")
    print("-------------------------")
    if len(presidents) == 0:
        print("There are no presidents in the list.\n")
        return
    else:
        i = 1
        
    
    for row in presidents:
        print ("{:4}{:25}".format((str(i)) + ". " , (row)))
        i += 1
        print()
        
              
              
        
    
#---------------------------function--------------------------------
#Name: showDeficits(presidents, deficits)
#Purpose: Will print the list of presidents names along with deficits list found in main


def showDeficits(presidents, deficits):
    print("List of Presidents and Deficits")
    print("------------------------------------")
    
    if len(presidents) == 0:
        print("There are no presidents in the list.\n")


    if len(deficits) == 1:
        print("There are no presidents in the list.\n")
        return
        
    else:
        i = 0
          
    
    for row in deficits:
        #print ("{:4}{:25}".format((str(i)) + ". " , (row)))
        #defc = str(deficits[i])
        print ("{:4}{:25}{:8}".format((str(i + 1)) + ". " , presidents[i], (row)))
        i += 1
        print()      
        
#---------------------------function--------------------------------
#Name: showDeficits(presidents, deficits)
#Purpose: Will let you add a new presidents name to add to the presidents list and deficits for that president in billions
        
def addPresident(presidents, deficits):
    while True:
        uName = input("Enter presidents name: ")
        if uName ==(""):
            print("Please enter something")
        else:
            break
       elif presidents.append(uName):
            
            uDeficit = input("Enter the deficit in billions: ")
            if uDeficit ==(""):
            print("Please enter something")
            else:
                break
        elif deficits.append(uDeficit):
            break
    print(uName + " was added.\n")
           
    



def main():

    #list of presidents
    presidents = ["Barack H. Obama",
                 "George W. Bush",
                 "William Clinton",
                 "George H. Bush",
                 "Ronald Reagan",
                 "Jimmy Carter",
                 "Gerald Ford",
                 "Richard Nixon",
                 "Lyndon Johnson",
                 "John Kennedy",
                 "Dwight Eisenhower"]

    #list of deficits
    deficits = [-6695.00,
               -3295.00,
               63.00,
               -1035.00,
               -1412.00,
               -253.00,
               -181.00,
               -70.00,
               -36.00,
               -18.00,
               -22.00]
#loop main tasks
    while True:
        command = displayMenu()

        if command == "l":
            ListPresidents(presidents)
        elif command == "s":
            showDeficits(presidents, deficits)
        elif command == "a":
            addPresident(presidents, deficits)
        elif command == "d":
            drawHistogram(Histogram)
        elif command == "q":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")


    



if __name__ == "__main__":
    main()
