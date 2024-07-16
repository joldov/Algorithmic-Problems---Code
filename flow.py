def find_edges(edges, capacities, s, t):
    # Find maximum flow and construct residual graph
    max_flow, residual_graph = ford_fulkerson_with_residual(edges, capacities, s, t)
    
    reachable_from_s = bfs_reachable(residual_graph, s)
    
    critical_edges = [
        edge for edge in edges
        if edge[0] in reachable_from_s and edge[1] not in reachable_from_s
    ]
    
    priority_edges = []
    for edge in critical_edges:
        if residual_capacity(residual_graph, edge) == 0:
            new_capacities = list(capacities)  
            edge_index = edges.index(edge)
            new_capacities[edge_index] += 1  
            new_max_flow, _ = ford_fulkerson_with_residual(edges, new_capacities, s, t)
            if new_max_flow > max_flow:
                priority_edges.append(edge)

    return priority_edges
