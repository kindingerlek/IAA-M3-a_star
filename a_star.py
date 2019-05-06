import dists
import copy

MAX_ITERATIONS = 50

# goal sempre sera 'bucharest'
def a_star(start, goal = "Bucharest"):
    """
    Retorna uma lista com o caminho de start até 
    Bucharest segundo o algoritmo A*
    """ 
    
    if start not in dists.dists or goal not in dists.dists:
        print ("START OR GOAL IS INVALID!")
        return;
        
    out = {}
    visited = {}
    visited[start] = { "path" : [], "cost" : 0}    
    
    if expand_node(start, goal, out, visited, debug = True) is not None:
        print ("DESTINATION FOUND: ")
        print ("{0:>15} : {1}".format(goal,visited[goal]))
    else:
        print ("MAX DEEP ITERATIONS REACHED")

    
def expand_node(currentCity, goal, out = {}, visited = {}, debug = False, it = 0):
    """
    Iterate every city node in recursive way. This functions is main core of
    the algorithm. The way how its works is:
    
    From actual node: expand to all other connected nodes and make this node
    out of next iterations. If the expanded subnodes aren't previously visited,
    calculate the cost and save the path. But if the city are already visited,
    update path and cost. Otherwise, ignore it.
    
    Then to all visited cities, calculate new cost based at the cost to trace
    and distance to goal. The less cost city will be expanded.
    """
    
    if currentCity == goal:
        return visited[goal]
    
    if(it > MAX_ITERATIONS):
        return None;    
    
    out[currentCity] = visited[currentCity]        
    
    #Look if the subnodes are visited, out or new
    for city,cost in dists.dists[currentCity]:        
        if city in out:
            continue
        
        if city not in visited:     
            visited[city] = {
                "path" : (out[currentCity]["path"].copy()),
                "cost" : (out[currentCity]["cost"] + cost) }
            
        elif out[currentCity]["cost"] + cost < visited[city]["cost"]:
                visited[city] = {
                        "path" : (out[currentCity]["path"].copy()),
                        "cost" : (out[currentCity]["cost"] + cost) }
            
        visited[city]["path"].append(currentCity)                
        
    visited.pop(currentCity)    
   
    next_city = look_for_next_city(visited, goal)
    it += 1;    
    
    if debug: print_debug(currentCity,out,visited,next_city)

    return expand_node(next_city[0],goal,out, visited,debug,it)

def look_for_next_city(visited = {}, goal = ""):
    """
    Makes a copy of all visited cities to a temporary list and then add the
    value of straight line to goal.
    
    If this info is unavailable, nothing is added.
    """
    candidates = copy.deepcopy(visited)    
    
    for candidate in candidates.items():        
        if goal in dists.straightline_dists:    
            candidate[1]["cost"] += dists.straightline_dists[goal][candidate[0]]
            continue
        
        if candidate.key in dists.straightline_dists:
            candidate["cost"] += dists.straightline_dists[candidate[0]][goal]
            continue
    
    return min(candidates.items(), key=lambda x: x[1]["cost"])

def print_debug(currentCity,out,visited, next_city):
    """
    Print in console the important infomations
    """
    
    print ("EXPANDING: {0}\nSUBNODES: {1}".format(currentCity, dists.dists[currentCity]))          
    print ("\n{0}{1:-^85}\n".format('\x1b[6;37;41m','OUT:'))
    print ( printDict (out))
    print ("\n{0}{1:-^85}".format('\x1b[6;37;42m','VISITED'))
    print ( printDict (visited))
    print ("\x1b[0m")
    print ("\nNEXT: {0} WITH COST: {1}\n\n{2:=>85}\n".format(next_city[0],next_city[1]["cost"],''))
    
def printDict(dict = {}):
    str = ''
    
    for a in dict.items():
        str = str + "{0: >15} : {1}\n".format(a[0], a[1])
    
    return str
        