import math
import dists

next_city = ''

visited = []
closed = []
destination_costs = {}


# goal sempre sera 'bucharest'
def a_star(start):
    """
    Retorna uma lista com o caminho de start até 
    Bucharest segundo o algoritmo A*
    """ 
    destination_costs = {}

    expandNode(start)
    
    
def expandNode(currentCity, path = [], it = 0):
    
    if currentCity == "Bucharest":
        print ("Bucharest Found")
        return path;
    
    if(it > 10):
        return path
    
    
    path.append(currentCity)    
    closed.append(currentCity)    
    print ("Expanding: {0} SubNodes: {1}".format(currentCity, dists.dists[currentCity]))
        
    for city,cost in dists.dists[currentCity]:        
        if city in closed:
            continue
                
        if city in destination_costs:
            destination_costs[city] += cost
        else:
            destination_costs[city] = cost
    
    print ("closed: {0}".format(closed))
    print ("cost: {0}".format(destination_costs))
    
    next_city = min(destination_costs.items(), key=lambda x: x[1])[0]
    cost = min(destination_costs.items(), key=lambda x: x[1])[1]
    destination_costs.pop(next_city)
    
    it += 1;
    
    print ("Next City: {0} cost: {1}\n\n".format(next_city,cost))

    expandNode(currentCity = next_city, it = it)
    
        