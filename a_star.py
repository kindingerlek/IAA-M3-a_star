import math
import dists

next_city = ''

closed = {}
visited = {}


# goal sempre sera 'bucharest'
def a_star(start, goal = "Bucharest"):
    """
    Retorna uma lista com o caminho de start até 
    Bucharest segundo o algoritmo A*
    """ 
    
    visited[start] = { "path" : [], "cost" : 0}
    expandNode(start, goal)   
    

    
def expandNode(current_city, goal, it = 0):    
    if current_city == goal:
        print ("DESTINATION FOUND")
        return visited[current_city];
    
    if(it > 50):
        return visited[current_city];
    
    
    #if current_city in visited
    closed[current_city] = visited[current_city]
        
    
    for city,cost in dists.dists[current_city]:        
        if city in closed:
            continue
                                
        if city not in visited:
            
            visited[city] = {
                "path" : (closed[current_city]["path"].copy()),
                "cost" : (closed[current_city]["cost"] + cost) }
            
            visited[city]["path"].append(current_city)               
    
        
    visited.pop(current_city)
        
    best_node = min(visited.items(), key=lambda x: x[1]["cost"])    
    next_city = best_node[0]
    cost = best_node[1]["cost"]
    
    
    it += 1;    
    
    print ("EXPANDING: {0}\nSUBNODES: {1}\n".format(current_city, dists.dists[current_city]))   
    
    print ("\n == CLOSED ==:")
    printDict (closed)
        
    print ("\n == VISITED ==:")
    printDict (visited)
    
    print ("NEXT: {0} WITH COST: {1}\n\n============\n".format(next_city,cost))

    expandNode(next_city,goal, it)
    
    
def printDict(dict = {}):
    for a in dict.items():
        print("{0} : {1}".format(a[0], a[1]))
        