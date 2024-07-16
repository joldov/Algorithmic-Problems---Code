import math

def arbitrage(exchange_rates):
    # transform the exchange rates using negative logarithm
    edges = [(i, j, -math.log(w)) for i, j, w in exchange_rates]
    # initiaize graph
    V = max(max(u, v) for u, v, _ in exchange_rates) + 1  # 0-based indexing for vertices
    distance = [float('inf')] * V
    predecessor = [-1] * V

    #arbitrarily choose 0 as the starting vertex
    distance[0] = 0

    #run bellman ford 
    for _ in range(V - 1):
        for u, v, w in edges:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                predecessor[v] = u

    # check for negative weight cycles
    for u, v, w in edges:
        if distance[u] + w < distance[v]:
            # reconstruct the negative cycle path
            arbitrage_cycle = []
            for _ in range(V):
                v = predecessor[v]
            # traverse the cycle
            start = v
            while True:
                arbitrage_cycle.append(v)
                v = predecessor[v]
                if v == start:
                    break
            arbitrage_cycle.append(start)
            arbitrage_cycle.reverse()

            # verify if the cycle is an arbitrage opportunity
            if verify_arbitrage_cycle(arbitrage_cycle, exchange_rates):
                return arbitrage_cycle

    return None

def verify_arbitrage_cycle(cycle, exchange_rates):
    # convert the cycle back from the log space
    product_of_rates = 1
    for i in range(len(cycle) - 1):
        for (u, v, w) in exchange_rates:
            if u == cycle[i] and v == cycle[i + 1]:
                product_of_rates *= w
                break
    return product_of_rates > 1
