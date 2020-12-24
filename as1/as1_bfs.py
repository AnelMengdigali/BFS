# Author: Dinh-Mao Bui, Anh-Tu Nguyen
# Rule of traversing: Alphabetical ordered, then left to right,
# Points: 2
def traverse(tree, init):

    queue = [init]
    traversed = []

    while queue:

        node = queue.pop(0)

        traversed.append(node)
        leaves = tree[node]

        for leaf in leaves:
            
            if leaf not in queue and leaf not in traversed:
                queue.append(leaf)

    return traversed


# Points: 3
def pathfinder(tree, init, goal):

    traversed = []
    queue = [[init]]

    if init == goal:
        return "No kidding, pls"

    while queue:

        nodes = queue.pop(0)

        traversed.append(nodes[-1])
        leaves = tree[nodes[-1]]

        for leaf in leaves:

            if leaf not in queue and leaf not in traversed:

                result = list(nodes)
                result.append(leaf)

                if leaf == goal:
                    return result

                queue.append(result)
                
    return "No such path exists"
