#!/usr/bin/python3
""" module contails canUnlockAll """


def canUnlockAll(boxes):
    """ func checks if boxes contain keys to unlocking all boxes """
    visited = set()
    to_explore = [0]  # Start from box 0

    while to_explore:
        current_box = to_explore.pop()
        visited.add(current_box)
        keys = boxes[current_box]
        for key in keys:
            if key not in visited:
                to_explore.append(key)

    return len(visited) == len(boxes)
