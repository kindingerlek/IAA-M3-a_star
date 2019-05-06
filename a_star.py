import math
import dists
import copy



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
    
    
    if expandNode(start, goal, out, visited, debug = True) is not None:
        print ("DESTINATION FOUND: ")
        print ("{0:>15} {1}".format(goal,visited[goal]))
    else:
        print ("MAX DEEP ITERATIONS REACHED")

    
def expandNode(current_city, goal, out = {}, visited = {}, debug = False, it = 0):    
    if current_city == goal:
        return visited[goal]
    
    if(it > 50):
        return None;    
    
    #if current_city in visited
    out[current_city] = visited[current_city]        
    
    for city,cost in dists.dists[current_city]:        
        if city in out:
            continue
                                
        if city not in visited:            
            visited[city] = {
                "path" : (out[current_city]["path"].copy()),
                "cost" : (out[current_city]["cost"] + cost) }
            
            visited[city]["path"].append(current_city)     
        
    visited.pop(current_city)    
   
    next_city = look_for_next_city(visited, goal)
    
    
    it += 1;    
    
    if debug:
        debugPrint(current_city,out,visited,next_city)

    return expandNode(next_city[0],goal,out, visited,debug,it)


def look_for_next_city(visited = {}, goal = ""):
    candidates = copy.deepcopy(visited)
    
    """
    for candidate in candidates.items():        
        if goal in dists.straightline_dists:    
            candidate[1]["cost"] += dists.straightline_dists[goal][candidate[0]]
            continue
        
        if candidate.key in dists.straightline_dists:
            candidate["cost"] += dists.straightline_dists[candidate[0]][goal]
            continue                
    """
    
    best_node = min(candidates.items(), key=lambda x: x[1]["cost"])
        
    print(">>>>>{0}".format(best_node))
    
    return best_node

def debugPrint(current_city,out,visited, next_city):    
        print ("EXPANDING: {0}\nSUBNODES: {1}".format(current_city, dists.dists[current_city]))          
        print ("\n{0}{1:-^85}\n".format('\x1b[6;37;41m','OUT:'))
        printDict (out)            
        print ("\n{0}{1:-^85}".format('\x1b[6;37;42m','VISITED'))
        printDict (visited)        
        print ("\x1b[0m")
        print ("\nNEXT: {0} WITH COST: {1}\n\n{2:=>85}\n".format(next_city[0],next_city[1]["cost"],''))
    
    
def printDict(dict = {}):
    for a in dict.items():
        print("{0: >15} : {1}".format(a[0], a[1]))
        