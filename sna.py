# I used os module becase I want to check whetever sn.txt exist or not.
import os


def addUser(command1,userList):
    if len(command1) != 2:
        print("Missing argument")
    
    elif command1[1] in userList:
        print("This user already exists!")
    
    elif command1[1] not in userList:
        
        sn = open("sn.txt","a")
        sn.write(f"{command1[1]}:\n")
        sn.close()
        print(f"User {command1[1]} added successfully")

def removeUser(command1,userList):
    if len(command1) != 2:
        print("Missing argument")
    
    elif command1[1] not in userList:
        print(f"There is no user named {command1[1]}")

    elif command1[1] in userList:                   

        print(f"User {command1[1]} and its all relations have been removed successfully.")
        with open("sn.txt","r+") as f:
            listOfLines = f.readlines()

            for i in listOfLines:
                seperatedUsers = i.split(":")
                if seperatedUsers[0] == command1[1]:
                    listOfLines.remove(i)

            for t in listOfLines:
                if command1[1] in t:
                    
                    s = listOfLines.index(t)  
                    # When we want to remove last user from friend list , we should delete space in the left side of last user.
                    if command1[1] == t[-2]:
                        listOfLines[s] = t.replace(f" {command1[1]}","")
                    
                    # When we want to remove user from friend list , we should delete space in the right side of user.
                    else:
                        listOfLines[s] = t.replace(f"{command1[1]} ","")
                else:
                    pass
            
            
            f.seek(0)
            f.truncate(0) # I use truncate method for deleting the file content and then I printed the updated version of file content.
            for i in listOfLines:
                f.write(i)

def addRelation(command1,userList):
    if len(command1) != 3:
        print("Missing argument")
    else:
        if command1[1] not in userList or command1[2] not in userList:
            print(f"No user named {command1[1]} or {command1[2]} found!")
        
        else:
            ar = open("sn.txt","r+")
            listOfLines = ar.readlines()

            for i in listOfLines:
                seperatedUsers = i.split(":")

                seperatedUsers2 = seperatedUsers[1].strip(" ").strip("\n").split(" ")
                
                if command1[1] == seperatedUsers[0] and command1[2] in seperatedUsers2 or command1[2] == seperatedUsers[0] and command1[1] in seperatedUsers2:
                    
                    # I used below code for print one time of their relationship exist otherwise print statement is going to executed twice. 
                    if command1[1] == seperatedUsers[0] and command1[2] in seperatedUsers:
                        print(f"{command1[1]} relation between {command1[1]} and {command1[2]} already exists!")
                    
                    else:
                        pass
                else:
                    if seperatedUsers[0] == command1[1]:
                        s = listOfLines.index(i)
                        listOfLines[s] = i.replace("\n",f" {command1[2]}\n")
                        ar.seek(0)
                        ar.truncate(0)
                        for j in listOfLines:
                            ar.write(j)
                                                        
                    elif seperatedUsers[0] == command1[2]:
                        s = listOfLines.index(i)
                        listOfLines[s] = i.replace("\n",f" {command1[1]}\n")
                    
                        print(f"{command1[1]} relation between {command1[1]} and {command1[2]} has been added successfully.")
                        ar.seek(0)
                        ar.truncate(0)
                        for j in listOfLines:
                            ar.write(j)
            ar.close()

def removeRelation(command1,userList):
    if len(command1) != 3:
        print("Missing argument")

    else:
        if command1[1] not in userList or command1[2] not in userList:
            print(f"No user named {command1[1]} or {command1[2]} found!")
        
        else:
            rr = open("sn.txt","r+")
            listOfLines = rr.readlines()

            for i in listOfLines:
                seperatedUsers = i.split(":")
                seperatedUsers2 = seperatedUsers[1].strip(" ").strip("\n").split(" ")
                if command1[1] == seperatedUsers[0] and command1[2] not in seperatedUsers2 or command1[2] == seperatedUsers[0] and command1[1] not  in seperatedUsers2:
                    
                    # I used below code for print one time of their relationship that not exist otherwise print statement is going to executed twice. 
                    if command1[1] == seperatedUsers[0] and command1[2] not in seperatedUsers2:
                        print(f"No relation between {command1[1]} and {command1[2]} found!")
                    
                    else:
                        pass                           
                else:
                    if seperatedUsers[0] == command1[1]:
                        s = listOfLines.index(i)
                        
                        if command1[2] == seperatedUsers2[-1]:
                            listOfLines[s] = i.replace(f" {command1[2]}","")
                        else:
                            listOfLines[s] = i.replace(f"{command1[2]} ","")
                        
                        rr.seek(0)
                        rr.truncate(0)
                        for j in listOfLines:
                            rr.write(j)
                                                        
                    elif seperatedUsers[0] == command1[2]:
                        s = listOfLines.index(i)

                        if command1[1] == seperatedUsers2[-1]:
                            listOfLines[s] = i.replace(f" {command1[1]}","")
                        else:
                            listOfLines[s] = i.replace(f"{command1[1]} ","")

                        print(f"{command1[1]} relation between {command1[1]} and {command1[2]} has been removed successfully.")
                        rr.seek(0)
                        rr.truncate(0)
                        for j in listOfLines:
                            rr.write(j)
            rr.close()

def rankUsers(command1,userList):
    if len(command1) != 2:
        print("Missing argument")
    
    elif int(command1[1]) > len(userList):
        print(f"Invalid input since {command1[1]} is greater than {len(userList)}")

    else:                   
        with open("sn.txt","r+") as file5:                        
            listOfLines = file5.readlines()
            listOfLines = sorted(listOfLines)
            list1 = []

            for i in listOfLines:
                seperatedUsers = i.strip("\n").split(":")
                seperatedUsers2 = len(seperatedUsers[1].replace(" ",""))
                print(f"User '{seperatedUsers[0]}' has {seperatedUsers2} friends")
                list1.append([seperatedUsers[0],seperatedUsers2])
            
            # I used this code for according to sort who has more friends.
            sortedList = sorted(list1, key = lambda i: i[1],reverse=True)                      
            for i in range(0,int(command1[1])):
                print(f"{i+1}. '{sortedList[i][0]}': {sortedList[i][1]}")

def suggestFriendship(command1,userList):
    if len(command1) != 3:
        print("Missing argument")

    elif command1[1] not in userList:
        print(f"No user named {command1[1]} found!")
    
    else:
        with open("sn.txt","r") as fl:                        
            listOfLines = fl.readlines()
            check = 0
            
            for i in listOfLines:
                relations2 = i.strip("\n").split(":")

                if relations2[0] == command1[1]:
                    check += len(relations2[1].replace(" ",""))
            
            if int(command1[2]) > check:
                print(f"User {command1[1]} has friends less than {command1[2]}")
                
            else:
                list1 = []                           
                for i in listOfLines:
                    relations = i.strip("\n").split(" ")
                    if relations[0] == command1[1]+":":
                        for k in relations:                                      
                            for l in listOfLines:                                
                                if l.split(" ")[0].strip(":") == k.strip(":"):
                                    relations2 = l.strip("\n").split(" ")
                                    for z in relations2:
                                        if z != command1[1]:
                                            list1.append(z)
                                        else:
                                            pass
                list2 = []
                list3 = []
                for i in list1:                                   
                    if i not in list3:
                        list2.append(list1.count(i))
                        list3.append(i)
                    else:
                        pass
                
                print(f"Suggestion List for '{command1[1]}' (when MD is {command1[2]}):")
                h = 0
                for i in list2:                                
                    if i >= int(command1[2]):
                        print(f"'{command1[1]}' has {i} mutual friends with {list3[h]}")                              
                    h += 1

def main():
    with open("commandsP1.txt","r+",encoding="utf-8") as file:   
        x = len(file.readlines())
        n = 0
        file.seek(0)

        while n < x:
            commands1 = file.readline().strip("\n")
            command1 = commands1.split(" ")

            if os.path.exists("sn.txt") == False:
                with open("sn.txt","w"):
                    pass
            
            # I created to userList with below codes.
            file2 = open("sn.txt","r+",encoding="utf-8")
            users = file2.readlines()
            userList = []
            for user in users:
                user = user.split(":")
                if user[0] not in userList:
                    userList.append(user[0])
            file2.close()

            if command1[0] == "AU":
                addUser(command1,userList)
                
            elif command1[0] == "RU":
                removeUser(command1,userList)

            elif command1[0] == "AR":
                addRelation(command1,userList)
                            
            elif command1[0] == "RR":
                removeRelation(command1,userList)

            elif command1[0] == "PA":
                rankUsers(command1,userList)

            elif command1[0] == "SA":     
                suggestFriendship(command1,userList)
                
            n +=1
main()