# Number of binary tree topologies

# n = 0 -> 1 (null) and n = 1 -> 1


def topologies(n, count):

    if n == 0 or n == 1:
        return 1

    else:
        for i in range(1, n):
            count += topologies(i, 0) + topologies(n-i-1, 0)

        return count


# iterative approach
def topologiesIterative(n):

    topology = []
    topology.append(1)
    topology.append(1)

    for i in range(2, n+1):
        topology.append(0)

    for i in range(2, n+1):
        """
        j = 0
        count = 0
        while(j < i):
            count += topology[j] 
            j += 1
        """
        j = 1
        while(j < n+1):
            topology[i] += (topology[j] + topology[n-j-1])
            j+=1

    return topology


print(topologies(3, 0))
print(topologiesIterative(3))
# iterative solution
