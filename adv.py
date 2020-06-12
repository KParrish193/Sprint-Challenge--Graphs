from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


# ! ------------------------------------------------ !

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
visited = {}

curr_room = player.current_room.id
visited_key = curr_room
visited_value = player.current_room.get_exits()

move_stack = []

# visited
# {
#   visited_key 0: visited_value{'n': '?', 's': '?', 'w': '?', 'e': '?'}
# }
visited[visited_key] = visited_value
print(visited)

# ? range to traverse = len(room_graph) -1, exit when visited = # of rooms - full scope while loop
while len(visited) < len(room_graph) -1:
    # ? if current room is not previously visited, add to visited, document room
    if curr_room not in visited:
        # add current room to visited, add exits as value?
        visited[curr_room] = curr_room.get_exits()
            
    # ? if dead end
    while len(visited[curr_room]) == 0:
        # pop previous direction from move stack
        prev_dir = ?
        # add backtrack directions to traversal
        traversal_path.append(prev_dir)
        # move player in backtracked direction
        player.travel(prev_dir)

    # ? move player to next room
    # add neighbors to move_stack
    move_stack.append()
    # determine next direction to move
    next_move = ?
    # append direction of next travel to traversal path
    traversal_path.append(next_move)
    # move player to next room
    player.travel(next_move)

# ! ------------------------------------------------ !

# TODO: fill in the traversal. 

#   set direction unable to visit as None?
#   set direction traveled to new room number
#   base case - when len(exits) == 1
#   how to move player back to previous room when dead end is reached
#   no `'?'` in the adjacency dictionaries
#   Start by writing an algorithm that picks a random unexplored direction from the player's current room, travels and logs that direction, then loops. This should cause your player to walk a depth-first traversal. When you reach a dead-end (i.e. a room with no unexplored paths), walk back to the nearest room that does contain an unexplored path.
# {
#   (current room id)0: exits?{'n': neighbor rooms'?', 's': '?', 'w': '?', 'e': '?'}
# }

# ! ------------------------------------------------ !




# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
