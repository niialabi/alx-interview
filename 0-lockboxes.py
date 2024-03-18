#!/usr/bin/python3
def canUnlockAll(boxes):
    """ func checks if boxes contain keys to unlocking all boxes """
    # Initialize a set to keep track of visited boxes
    visited = set()
    # Initialize a list to keep track of boxes that need to be explored
    to_explore = [0]  # Start from box 0

    # While there are boxes to explore
    while to_explore:
        # Get the next box to explore
        current_box = to_explore.pop()
        # Mark the current box as visited
        visited.add(current_box)
        # Get keys in the current box
        keys = boxes[current_box]
        # + unvisited boxes reachable from current box to to_explore list
        for key in keys:
            if key not in visited:
                to_explore.append(key)

    # Check if all boxes have been visited
    return len(visited) == len(boxes)
