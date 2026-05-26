"""
Problem Statement:
You are given a set of intervals, These are specificied as minutes, no hour
If one meeting overlaps with another, they cannot be in the same room so we have to see how many rooms are required

16 30
1 15
16 45
31 60
45 60

key - room id, value will be list of tuples
room1 - <16, 30>, <1, 15>, <31, 60> - upper bound (n)
room2 - <16, 45> - upper bound (n)

n * k - upper bound < n * n

For each tuple in the input list:

if there are no rooms create 1
else traverse list of rooms, and insert in the first room where there is no overlap

after loop, return the size of the map



"""
def _is_slot_overlap(slot1, slot2):
    """
    Conditions of overlap:

    earlier starting Tuple  has its end equal or after later starting tuple?

    """

    if slot1[0] == slot2[0]:
        return True
    elif slot1[0] < slot2[0]:
        earlier = slot1
        later = slot2
    else:
        earlier = slot2
        later = slot1


    if earlier[1] >= later[0]:
        return True
    else:
        return False




def _is_time_overlap(slot, slot_list):
    # TBD: Check overlap here
    for existing_slot in slot_list:
        if _is_slot_overlap(slot, existing_slot):
            return True
    return False


def get_number_of_rooms(input):

    room_num = 1
    rooms = {}
    rooms[0] = []
    # print(rooms)

    for slot in input:
        # print(slot)

        if not rooms:
            # no rooms exist so create a new one
            rooms[room_num] = [slot]
            room_num = room_num + 1
            continue
        else:
            room_assigned = False
            for key, slot_list in rooms.items():
                # append the slot to the first room where there is no overlap
                if not _is_time_overlap(slot, slot_list):
                    slot_list.append(slot)
                    room_assigned = True
                    break
            ## all rooms have overlap so create a new one
            if not room_assigned:
                rooms[room_num] = [slot]
                room_num = room_num + 1

    print("rooms map", rooms)
    return len(rooms)




"""

slot1 = (1, 4)
slot2 = (5, 9)

print(_is_slot_overlap(slot1, slot2))

slot1 = (1, 6)
slot2 = (5, 9)

print(_is_slot_overlap(slot1, slot2)) 


slot1 = (3, 6)
slot2 = (1, 9)




print(_is_slot_overlap(slot1, slot2)) 

slots = [(1, 2), (3, 4), (5, 6)]    
single_slot = (7, 9)

print(_is_time_overlap(single_slot, slots))

"""

slot_list = []
slot_list.append((16, 30))
slot_list.append((1, 15))
slot_list.append((16, 45))
slot_list.append((31, 60))
slot_list.append((45, 60))
"""



45 60
 """

room_len = get_number_of_rooms(slot_list)
print("room_len", room_len)
