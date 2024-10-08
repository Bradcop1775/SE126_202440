#WEEK 3 DAY 2: LIST DEMO

#LISTS can hold multiple points of data and store them to "memory" to be used later on in our program

#this demo utilizes the lab 2B solution file


#VARIABLE DICTIONARY----------------------------
#records            total records in file

#field0             col. 0, rec[0], type of machine, from file
#device               a LIST that holds the entire field0/rec[0] data from file
 
#field1             col. 1, rec[1], brand of machine, from file
#brand              a LIST that holds the entire field1/rec[1] data from file

#field2             col. 2, rec[2], cpu, from file
#cpu                a LIST that holds the entire field2/rec[2] data from file

#field3             col. 3, rec[3], ram, from file
#ram                a LIST that holds the entire field3/rec[3] data from file

#field4             col. 4, rec[4], 1st disk space, from file
#first_disk         a LIST that holds the entire field4/rec[4] data from file


#field5*             col. 5, rec[5], number of hard drives*, from file
#                           *this value determines where the remaining record values are stored
#num_disks          a LIST that holds the entire field5/rec[5] data from file

#field6             col. 6, 2nd disk space, from file where rec[5] == "2"
#secnd_disk         a LIST that holds the entire field6/rec[6] data from file

#field7             col. 7, operating system, from file 
#os                 a LIST that holds the entire field7/rec[7] data from file

#field8             col. 8, year, from file 
#yr                 a LIST that holds the entire field8/rec[8] data from file



#*this value determines where the remaining record values are stored

#BASE PROGRAM CODE-----------------------------------------------------------------------------------------

import csv 

#initialize variable that will count the total number of records -- NECESSARY FOR LIST PROCESSING LATER

records = 0

#LISTS -- first we need to prep some empty lists so the processor doesn't see one and think it's a var / allows us to store into the list 

#TIP --> create an empty list for EVERY potential field value in the file
device = []#we have created an empty list
brand = []
cpu = []
ram = []
first_disk = []
no_hdd = []
second_disk = []
os = []
yr = []


#pint header for file printing
#print("{0:10} \t {1:10} \t {2:3} \t {3:2} \t {4:7} \t {5:7} \t {6:7} \t {7:4} \t {8}".format("DEVICE", "MANU.", "CPU", "RAM", "1st Disk", "No. HDD", "2nd Disk", "OS", "YEAR"))
#print("-----------------------------------------------------------------------------------------------------------------")

#connect to the file location
#CONNECTED TO FILE---------------------
with open("Week2\lab2b.csv") as csvfile:

    #access the file's data
    file = csv.reader(csvfile)

    #process the file's data
    for rec in file:

        records += 1 #keeps count of the total number of records
                     #THIS IS NECESSARY for PROPER LIST PROCESSING LATER
                     #list processing uses FOR LOOPS using the range() and will need to know how many times to run the loop (1x for each value stored in the list, ie for each record in the file

        #change field0 from D/L --> Desktop/Laptop
        if rec[0] == "D":
            field0 = "Desktop"
        elif rec[0] == "L":
            field0 = "Laptop"
        else:
            field0 = "*ERROR*"

        #change field 1 to full manufacturer name
        if rec[1] == "DL":
            field1 = "Dell"
        elif rec[1] == "GW":
            field1 = "Gateway"
        elif rec[1] == "HP":
            field1 = "HP"
        else:
            field1 = "*ERROR*"


        #fields 2-5 stay the same, store into friendlier names
        field2 = rec[2]
        field3 = rec[3]
        field4 = rec[4]
        field5 = int(rec[5]) #this one determines fields 6 - 8


        #filter for remainig field values
        if field5 == 1: #1 HDD
            field6 = "---"
            field7 = rec[6]
            field8 = rec[7]


        elif field5 == 2:

            field6 = rec[6]
            field7 = rec[7]
            field8 = rec[8]

        else:

            field6 = "*ERROR*"
            field7 = "*ERROR*"
            field8 = "*ERROR*"


        #***LIST STORAGE***- you will essentially have a list for every FIELD in your file :]

        #ADD THE FIELD0-8 DATA TO THE APPROPRIATE LISTS
        device.append(field0) #<--appending (adding) field0 value into the type list
                            #IF WE HADN'T CREATED VARIABLES for each field:
                            # device.append(rec[0])
   
        
        brand.append(field1)
        cpu.append(field2)
        ram.append(field3)
        first_disk.append(field4)
        no_hdd.append(field5)
        second_disk.append(field6)
        os.append(field7)
        yr.append(field8)


        #print("{0:10} \t {1:10} \t {2:3} \t {3:2} \t {4:7} \t {5:7} \t {6:7} \t {7:4} \t {8}".format(field0, field1, field2, field3, field4, field5, field6, field7, field8))
        #print(rec)

#-------DISCONNECTED FROM FILE----------

print("RECORDS: ", records)

#print("{0:10} \t {1:10} \t {2:3} \t {3:2} \t {4:7} \t {5:7} \t {6:7} \t {7:4} \t {8}".format(field0, field1, field2, field3, field4, field5, field6, field7, field8))
#ABOVE LINE -- only prints data from the last record in the file

#AFTER "EXITING" the FILE HANDLING AREA
#we no longer need to be accessing the file because all of the file data is now stored into lists.  the data stored in the lists can be accessed and processed as many times as we would like now without connecting our program to the actual file with data

#process the list data
#list processing = FOR LOOP

print("\n\n\nPRINTING FROM LISTS----------------")

#the below for loop will start the 'index' value at 0 and run for as many times as the value held inside of 'records'
#the index value will grow by one through each new time through the loop
#INDEX: position inside of the list
for index in range(0, records):

    #print("INDEX: ", index, "\t MACHINE BRAND: ", brand[index])

     #print each record (from the file) by acessing the inidividual lists where its data is stored (each field should have its own list)

     print("INDEX: {9} \t {0:10} \t {1:10} \t {2:3} \t {3:2} \t {4:7} \t {5:7} \t {6:7} \t {7:4} \t {8}".format(device[index], brand[index], cpu[index], ram[index], first_disk[index], no_hdd[index], second_disk[index], os[index], yr[index], index))



#we can reprocess the list data as many times as we would like
for index in range(0, records):

    print(brand[index])

################################################################################################

