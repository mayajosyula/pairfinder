import pandas as pd 
import networkx as nx 
import random

def get_matching(df):

    # Assuming that the leftmost column of the file is a list of names,
    # and the top row of the file is a list of preferences.
    fields = list(df.columns)
    names = df[fields[0]]
    names_list = list(names)

    # Find all the valid pairs.
    edge_list = []
    for f in fields[1:]:
        rowset = df[df[f].notnull()]
        rownames = rowset[fields[0]]
        for n in rownames:
            for m in rownames:
                if n < m:
                    edge_list.append((str(n), str(m)))


    # Attempt to randomize. Seems to work okay.
    random.shuffle(edge_list)
    random.shuffle(names_list)

    # Convert to graph, run matching algorithm. Edge weights are 1 by default
    G = nx.Graph()
    G.add_nodes_from(names_list)
    G.add_edges_from(edge_list)
    matching = nx.algorithms.max_weight_matching(G, maxcardinality=True)

    # Check if everyone was matched (there's probably a better way to do this)
    matched_names = []
    for pair in matching:
        matched_names.append(pair[0])
        matched_names.append(pair[1])
    common_names = set(names_list).intersection(matched_names)
    status = ""

    if (len(list(common_names)) == len(names_list)):
        status = f"\nAll {len(names_list)} were matched.\n"
    else:
        leftover = set(names_list) - common_names
        status = f"\nNot everyone was matched. Unmatched: {leftover}\n"

    # Print out the matches.
    matches = ""
    for pair in matching:
        matches += f"  --  {pair[0]} is matched with {pair[1]}"
    return (status, matches)