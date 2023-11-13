"""
    Author: Matthew Vallance 001225832
    Purpose: Task 3 - Revised task_2 but with the Bellman Ford Algorithm
    Date: 23/10/23
"""

from clrs_library_slim.adjacency_list_graph import AdjacencyListGraph
from clrs_library_slim.bellman_ford import bellman_ford
import read_data

# Get data with appropriate variable names
vertices, edges = read_data.get_data()

# Get input from the user
# TODO: Validity check
start_station = input('Input starting station: ')
dest_station = input('Input destination station: ')

# Create a graph from the clrs library for Adjacency lists
underground_graph = AdjacencyListGraph(len(vertices), False, True)

# Insert edges
for edge in edges:
    # Check if edge already exists in the graph
    existing_edges = underground_graph.get_edge_list()
    if (vertices.index(edge[0]), vertices.index(edge[1])) not in existing_edges and (vertices.index(edge[1]), vertices.index(edge[0])) not in existing_edges:
        # Insert edge into graph
        underground_graph.insert_edge(vertices.index(edge[0]), vertices.index(edge[1]), edge[2])

# Run Dijkstra's algorithm from the clrs library to find the shortest route to all stations based on user input
d, pi, negative_weight_cycle = bellman_ford(underground_graph, vertices.index(start_station))
bellman_outputs = []
for i in range(len(vertices)):
    # Create a sensible data structure of the output
    bellman_outputs.append({'dest': vertices[i], 'd': d[i], 'pi': ("None" if pi[i] is None else vertices[pi[i]])})


# Get route by looking for each predecessor in out Dijkstra's output
route = []
all_stations_added = False
next_station_to_find = dest_station
station_count = 0
while all_stations_added is False:
    for bellman_output in bellman_outputs:
        if bellman_output['dest'] == str(next_station_to_find):
            # Add each station to route list to print later
            route.append(bellman_output['dest'])
            next_station_to_find = bellman_output['pi']
            station_count += 1
            # Set all_stations_added to True, this breaks the loop as we have all the details needed
            if bellman_output['pi'] == 'None':
                all_stations_added = True

# TODO: Need to reverse route array at end - if needed depending on start and destination order
# Display routing
print('The shortest route for the given stations is: ' + ' -> '.join(route))

# Display count of stations to get to the destination minus 2 - we only want the count of stations in between
print('You will pass through ' + str(station_count - 2) + ' stations on your journey.')