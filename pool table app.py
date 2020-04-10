import json

class Table:
    def __init__(self, table_number, start_time = 0, end_time = 0, occupied = False, cost = 0):
        self.table_number = table_number
        self.start_time = start_time
        self.end_time = end_time
        self.occupied = occupied
        self.time_played = ""
        self.cost = cost

    def __repr__(self):
        return "\n------------------------\nTable: {0} \nStart Time: {1}\nEnd Time: {2}\nOccupied: {3}\nTime Played: {4}\nCost: {5}\n------------------------".format(self.table_number, self.start_time, self.end_time, self.occupied, self.time_played, self.cost)

#create objects for each table
table1 = Table("1")
table2 = Table("2")
table3 = Table("3")
table4 = Table("4")
table5 = Table("5")
table6 = Table("6")
table7 = Table("7")
table8 = Table("8")
table9 = Table("9")
table10 = Table("10")
table11 = Table("11")
table12 = Table("12")

#list to hold the objects
tables = [table1,table2,table3,table4,table5,table6,table7,table8,table9,table10,table11,table12]

tables_for_json = [table1.__dict__,table2.__dict__,table3.__dict__,table4.__dict__,table5.__dict__,table6.__dict__,table7.__dict__,table8.__dict__,table9.__dict__,table10.__dict__,table11.__dict__,table12.__dict__]

while True:
    try:
        prompt = input("Please select from the menu below:\n1 - Start a new game of Pool\n2 - End a game of Pool\n3 - View all Pool Tables\n4 - Quit the Program\n")
    # start new game of Pool
        if (prompt == "1"):
            open_table = int(input("Which table would you like to choose? "))
            current_object = tables[open_table - 1]
            if(current_object.occupied == True):
                print("***** This table is already being used *****")
            else:
                start_time = int(input("Please enter the start time: "))
                current_object.start_time = start_time
                current_object.end_time = 0
                current_object.occupied = True
                with open("9-8-18.json","w") as file_object:
                    json.dump(tables_for_json,file_object, indent = 2)

        # end a game of Pool
        elif (prompt == "2"):
            close_table = int(input("Which table would you like to choose? "))
            current_object = tables[close_table - 1]
            end_time = int(input("Please enter the end time: "))
            current_object.occupied = False
            current_object.end_time = end_time

            string_start_time = str(current_object.start_time)
            if (len(string_start_time) == 3 and len(string_start_time) != 4):
                hours = int(string_start_time[0])
                if(hours > 23):
                    print("***** Hours cannot be greater than 23 *****")
                minutes = int(string_start_time[1:3])
                if(minutes > 59):
                    print("***** Minutes cannot be greater than 59 *****")
                start_total = hours * 60 + minutes
            elif (len(string_start_time) == 4):
                hours = int(string_start_time[:2])
                if(hours > 23):
                    print("***** Hours cannot be greater than 23 *****")
                minutes = int(string_start_time[2:4])
                if(minutes > 59):
                    print("***** Minutes cannot be greater than 59 *****")
            start_total = hours * 60 + minutes

            string_end_time = str(current_object.end_time)
            if (len(string_end_time) == 3 and len(string_end_time) != 4):
                    hours = int(string_end_time[0])
                    if(hours > 23):
                        print("***** Hours cannot be greater than 23 *****")
                    minutes = int(string_end_time[1:3])
                    if(minutes > 59):
                        print("***** Minutes cannot be greater than 59 *****")
                    end_total = hours * 60 + minutes
            elif (len(string_end_time) == 4):
                    hours = int(string_end_time[:2])
                    if(hours > 23):
                        print("***** Hours cannot be greater than 23 *****")
                    minutes = int(string_end_time[2:4])
                    if(minutes > 59):
                        print("***** Minutes cannot be greater than 59 *****")
            end_total = hours * 60 + minutes

            difference = end_total - start_total
            hours = difference // 60
            minutes = difference % 60
            cost = (hours * 30) + (minutes * .0166667) * 30
            current_object.cost = "${:,.2f}".format(cost)
            current_object.time_played = "%s Hours %s Minutes" % (hours,minutes)
            with open("9-8-18.json","w") as file_object:
                json.dump(tables_for_json,file_object, indent = 2)
        # view all tables
        elif (prompt == "3"):
            print(tables)
        # quit the program
        elif (prompt == "4"):
            break
        else:
            print("***** Please enter a valid option *****")
    except NameError:
        print("***** There is no start time for this table *****")
    except ValueError:
        print("***** Please enter a valid time *****")
    except IndexError:
        print("***** Please enter a table number 1-12 *****")
    except:
        print("***** Something went wrong *****")