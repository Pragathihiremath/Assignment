#create friends dict of lists
def add_friends(all_friends, friend1, friend2):
    if friend1 not in all_friends:
        all_friends[friend1] = []
    if friend2 not in all_friends:
        all_friends[friend2] = []
    all_friends[friend1].append(friend2)
    all_friends[friend2].append(friend1)

def get_friends(all_friends, friend):
    return all_friends.get(friend, [])

#Using intersection of sets will find common friends
def find_common_friends(all_friends, friend1, friend2):
    friends1 = set(get_friends(all_friends, friend1))
    friends2 = set(get_friends(all_friends, friend2))
    return friends1.intersection(friends2)

#with recurrsion withh find connection counts
def find_connection_count(all_friends, start_friend, target_friend, visited=None, count=0):
    if visited is None:
        visited = set()
    if start_friend == target_friend:
        return count
    visited.add(start_friend)
    for friend in get_friends(all_friends, start_friend):
        if friend not in visited:
            connection_count = find_connection_count(all_friends, friend, target_friend, visited, count + 1)
            if connection_count != -1:
                return connection_count
    return -1  # No connection found

all_friends = {}

# Adding friends
add_friends(all_friends, 'Alice', 'Bob')
add_friends(all_friends, 'Bob', 'Janice')

connection_count = find_connection_count(all_friends, 'Alice', 'Janice')
print("Connection count between Alice and Janice:", connection_count)

connection_count = find_connection_count(all_friends, 'Alice', 'Bob')
print("Connection count between Alice and Bob:", connection_count)
