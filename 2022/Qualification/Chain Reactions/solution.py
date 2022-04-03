import copy
T = int(input())
for t in range(1, T+1):
    N = int(input())
    F = list(map(int, input().split()))
    P = list(map(int, input().split()))
    # Create graph with nodes and edges.
    graph = {}
    for i in range(N):
        graph[i+1] = []
    for i in range(N):
        if P[i] != 0:
            graph[i+1].append(P[i])
    initiators = []
    for i in range(N):
        allNodes = [i for i in range(1, N+1)]
        for node in allNodes:
            if node not in graph:
                continue
            if i+1 in graph[node]:
                break
        else:
            initiators.append(i+1)
    # Find all chains.
    chains = []
    used = set()
    reused = {}
    for initiator in initiators:
        chain = []
        node = initiator
        while node != 0:
            # dount reused nodes
            if node in used:
                reused[node] = reused.get(node, 0) + 1
            else:
                used.add(node)
            chain.append(node)
            node = P[node-1]
        chains.append(chain)
    for node in reused.keys():
        sharing_chains = []
        non_sharing_chains = []
        for chain in chains:
            if node in chain:
                sharing_chains.append(chain)
            else:
                non_sharing_chains.append(chain)
        new_chains = []
        new_sharing_chains = []
        for i in range((reused[node]+1)):
            new_sharing_chains.append(copy.deepcopy(sharing_chains))
        for i in range(len(new_sharing_chains)):
            new_sharing_chains[i][i].remove(node)
    new_chains = []
    for chain in new_sharing_chains:
        new_chains.append(chain + non_sharing_chains)
    chains = new_chains
    max_fun = 0
    for chain_group in new_sharing_chains:
        chain_group += non_sharing_chains
        fun = 0
        for chain in chain_group:
            fun += max([F[i-1] for i in chain])
        if fun > max_fun:
            max_fun = fun
    print("NIT. Serious bug here. Needs some fixing before submission.")
    break
    print('Case #{}: {}'.format(t, max_fun))
