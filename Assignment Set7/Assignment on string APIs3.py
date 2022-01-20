

#Sample ticket list - ticket format: "flight_no:source:destination:ticket_no"
#Note: flight_no has the following format - "airline_name followed by three digit number

#Global variable
ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056", "BA896:MUM:LON:067", "SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148","AI567:CHE:SIN:015","AI077:MUM:SIN:050","AI077:MUM:LON:051","SI267:MUM:SIN:146"]

def find_passengers_flight(airline_name="AI"):
    #This function finds and returns the number of passengers travelling in the specified airline.
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        if(string_list[0].startswith(airline_name)):
            count+=1
    return count

def find_passengers_destination(destination):
#   This function find and return the number of passengers traveling to the specified destination
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        if(string_list[2].startswith(destination)):
            count+=1
    return count

def find_passengers_per_flight():
      '''Write the logic to find and return a list having number of passengers traveling per flight based on the details in the ticket_list
    In the list, details should be provided in the format:
    [flight_no:no_of_passengers, flight_no:no_of_passengers, etc.].'''
    l = []
    flight_list = []
     
    for i in ticket_list: 
        string_list=i.split(":")
        flight_list.append(string_list[0])
    for i in flight_list:
        j = str(flight_list.count(i))
        l.append(i+':'+j)
    nl = list(set(l))
    return nl

def sort_passenger_list():
#   Sorts the list returned from find_passengers_per_flight() function in the descending order of number of passengers
    x = find_passengers_per_flight()
    dic = {}
    nl = []
    for i in x:
        s = i.split(':')
        dic[(s[1])]=(s[0])
    for key,value in sorted(dic.items()):
        nl.append(value+':'+key)


    return (nl[::-1])

print(find_passengers_flight("AI"))
print(find_passengers_destination("LON"))
print(sort_passenger_list())

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# Simplified code

# Sample ticket list - ticket format: "flight_no:source:destination:ticket_no"
# Note: flight_no has the following format - "airline_name followed by three digit number

# Global variable
ticket_list = ["AI567:MUM:LON:014", "AI077:MUM:LON:056", "BA896:MUM:LON:067", "SI267:MUM:SIN:145", "AI077:MUM:CAN:060",
               "SI267:BLR:MUM:148", "AI567:CHE:SIN:015", "AI077:MUM:SIN:050", "AI077:MUM:LON:051", "SI267:MUM:SIN:146"]


def find_passengers_flight(airline_name="AI"):
    # This function finds and returns the number of passengers travelling in the specified airline.
    count = 0
    for i in ticket_list:
        string_list = i.split(":")
        if (string_list[0].startswith(airline_name)) :
            count += 1
    return count

def find_passengers_destination(destination):
  #   This function find and return the number of passengers traveling to the specified destination
    count = 0
    for i in ticket_list:
        string_list = i.split(":")
        if (string_list[2]==destination):
            count += 1
    return count

def find_passengers_per_flight():
        '''Write the logic to find and return a list having number of passengers traveling per flight based on the details in the ticket_list
    In the list, details should be provided in the format:
    [flight_no:no_of_passengers, flight_no:no_of_passengers, etc.].'''
    l = []
    for i in ticket_list:
        str_list= i.split(":")
        count = find_passengers_flight(str_list[0])
        l.append(str_list[0] + ':' + str(count))
    return list(set(l))

def sort_passenger_list():
  #   Sorts the list returned from find_passengers_per_flight() function in the descending order of number of passengers
    x = find_passengers_per_flight()
    return (sorted(x , key=lambda val : val.split(":")[-1], reverse=True))
  
print(find_passengers_flight("AI"))
print(find_passengers_destination("LON"))
print(sort_passenger_list())
