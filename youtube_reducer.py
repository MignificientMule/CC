#!/usr/bin/python3

import sys


def read_map_output(file):
    """ Return an iterator for key, value pair extracted from file (sys.stdin).
    Input format:  key \t value
    Output format: (key, value)
    """
    for line in file:
        yield line.strip().split("\t")


def tag_reducer():
    dict = {}

    for category,video_id,country in read_map_output(sys.stdin):
        if category not in dict:
            dict[category] = [[video_id],[(video_id,country)]]

        else:
            if video_id not in dict[category][0]:
                dict[category][0].append(video_id)
                dict[category][1].append((video_id,country))
            else:
                if (video_id,country) not in dict[category][1]:
                    dict[category][1].append((video_id,country))
    for key in dict:

        print(key + ":" + str(float(len(dict[key][1]))/float(len(dict[key][0]))))

if __name__ == "__main__":
    tag_reducer()
