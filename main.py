# Michelle Golden and Shannon Mong
# Randomization + Local Search + Manhattan

# place attendees on a grid

import random as rand
from names_generator import generate_name  # name generator
import numpy as np
import Hotel as htl
import Attendee as attend
from scipy.spatial import distance
import matplotlib.pyplot as plt

blocks = 201  # holds limiter for plot
hotels = 20  # number of hotels
rooms = 15  # rooms per hotel
hotel_names = ["Prince's Keep Hotel", "Snowy Cave Hotel", "Ruby View Resort & Spa", "Rose Monarch Resort",
               "Private Citadel Hotel", "Crown Heritage Hotel", "Everland Motel", "Crescent Hotel",
               "Seaside Hotel & Spa",
               "Pinnacle Resort", "Grandiose Spa Resort", "Ruby Lodge Resort", "Sunrise Dawn Resort",
               "Southern View Hotel",
               "Obsidian Maple Resort", "Grand Veil Resort", "Shoreline Resort", "Leisure Hotel", "Vertex Resort",
               "Nimbus Hotel"]

attendees = 150  # number of attendees

attendee_loc = []  # location of attendees
hotel_loc = []  # locations of hotels
dist_list = []  # holds distances for each attendee

attendee_stay = {}  # dict to hold nested dicts of hotels and attendees in rooms

ht = hotels  # references hotels for loop without reducing hotels
ht_names = 19  # controls loop through hotel name assignment


# plot the hotels
def plot_loc_htl(x, y):
    x_coord = x
    y_coord = y
    colors = 'red'

    # Display Plot
    plt.scatter(x_coord, y_coord, c=colors)


# plot the attendees
def plot_loc_att(x, y):
    x_coord = x
    y_coord = y
    colors = 'green'

    # Display Plot
    plt.scatter(x_coord, y_coord, c=colors)


# create hotel object and control loop with ht
while ht > 0:
    temp_hotel = htl.Hotel(hotel_names[ht_names], rand.randrange(0, 200), rand.randrange(0, 200)) # generate hotel coord
    if (temp_hotel.get_hotel_x(), temp_hotel.get_hotel_y()) not in hotel_loc:  # if there is nothing at that coordinate
        hotel_loc.append((hotel_names[ht_names], int(temp_hotel.get_hotel_x()), int(temp_hotel.get_hotel_y())))  # add hotel
        ht -= 1
        ht_names -= 1

# print(hotel_loc[0])  # debug print
att = attendees  # references attendees for loop without reducing attendees
while att > 0:
    temp_attendee = attend.Attendee(rand.randrange(0, 200), rand.randrange(0, 200))
    attendee_loc.append(
        (generate_name(style='capital'), int(temp_attendee.get_attendee_x()), int(temp_attendee.get_attendee_y())))
    att -= 1

i = 0  # control for while loop
while attendees > i:
    j = 0  # control for nested while loop
    temp_list = []
    while hotels > j:
        coord_x = [hotel_loc[j][1], hotel_loc[j][2]]  # list with X coordinates
        plot_loc_htl(hotel_loc[j][1], hotel_loc[j][2])
        # print(coord_x)  # debug print
        coord_y = [attendee_loc[i][1], attendee_loc[i][2]]  # list with Y coordinates
        plot_loc_att(attendee_loc[i][1], attendee_loc[i][2])
        #  print(coord_y)  # debug print
        temp_list.append((attendee_loc[i][0], hotel_loc[j][0], distance.cityblock(coord_x, coord_y)))  # calculate
        # manhattan distance and match with name and hotel. Assign all distances for attendees to list

        j += 1  # increase counter
    temp_list = sorted(temp_list, key=lambda x: x[2])  # sort temp list by distance before inserting into dist_tuple
    # print("Current temp list: ", temp_list)  #debug print
    dist_list.append(temp_list)  # assign list of distances for each person to list
    i += 1  # increase counter

# create dictionary with key values for rooms. Each hotel starts out with 'no rooms' value
for k in hotel_names:
    attendee_stay.update({k: 'No Rooms'})
    l = 1
    room_dict_temp = {}
    # create a temporary dict and fill it with rooms using 1-15. Each are marked vacant. We will use
    while rooms >= l:
        room_dict_temp.update(
            {l: 'Vacant'})  # create a key for each room with vacant as value. This can be updated later
        l += 1
    attendee_stay[k] = room_dict_temp  # append temporary room dictionary to attendee_stay to create a sub dictionary
    # for each room that shows all rooms, vacant and occupied

# will be used to assign attendees to rooms
for attend in dist_list:  # for each attendee in the distribution list
    m = 0  # counter for hotels
    in_hotel = False  # set boolean param to tell if the attendee is in a hotel
    while hotels > m and in_hotel is False:  # go through each hotel option for each attendee IF the attendee is not
        # booked. It loops through list of hotels, starting with the closest one to the attendee
        n = 1  # room numbers, start at room 1
        while rooms >= n:  # while rooms is not yet at 15
            if attendee_stay[attend[m][1]][15] != 'Vacant':  # if the 15th room is occupied
                break  # break out of the loop
            elif attendee_stay[attend[m][1]][n] != 'Vacant':  # if the room the counter is on is occupied, go to next
                # room
                n += 1
            elif attendee_stay[attend[m][1]][n] == 'Vacant':  # if the room is vacant
                attendee_stay[attend[m][1]][n] = attend[m][0]
                in_hotel = True  # attendee is placed so break loops so attendee is not placed in another hotel
                break
        m += 1

x = 0
while hotels > x:  # print attendee list that shows attendees + rooms and vacant rooms
    print(hotel_names[x], ": ")
    print(attendee_stay[hotel_names[x]], " \n")
    x += 1

plt.show()
