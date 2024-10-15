#!/usr/bin/python3
''' Lockboxes interview question '''


def canUnlockAll(boxes):
    ''' determines if all the boxes can be opened. '''
    if (len(boxes) < 2):
        return True
    keys = {0}
    opened = set()
    while (len(keys) > len(opened)):
        for key in (keys - opened):
            opened.add(key)
            keys.update(boxes[key])

        toremove = set()
        for key in keys:
            if (key >= len(boxes)):
                toremove.add(key)
        keys -= toremove

        if (len(opened) == len(boxes)):
            return True

    return False
