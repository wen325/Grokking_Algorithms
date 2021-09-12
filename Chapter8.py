# example of set

fruits = set(["avocado","tomato","banana"])
vegetables = set(["beets","carrots","tomato"])

# set problem

states_needed = set(["mt","wa","or","id","nv","ut","ca","az"])
stations = {}
stations["kone"] = set(["id", "nv", "ut"]) 
stations["ktwo"] = set(["wa", "id", "mt"]) 
stations["kthree"] = set(["or", "nv", "ca"]) 
stations["kfour"] = set(["nv", "ut"]) 
stations["kfive"] = set(["ca", "az"]) 

final_stations = set()

best_station = None
states_covered = set()


while states_needed:    # there is still some states are needed
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items(): # test all stations
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):  # add station is useful; each for loop only adds one station
            best_station = station
            states_covered = covered                
            
    states_needed -= states_covered
    final_stations.add(best_station)