import sys

def find_paths(graph, scenario, cities, villages_with_passport):
	''' Find all the appropiate paths from 'S' to 'F' gven the scenario. '''
	num_paths = 0
	queue = []
	path = []
	path.append('S')
	queue.append(path.copy())  # stores arrays of vertices, not just the vertex
	# loop while the queue is n
	while len(queue) > 0:
		path = queue.pop(0)
		last = path[len(path) - 1]
		if (last == 'F'):
			print_path(path)
			num_paths += 1
		# loop through all the childern of "last"
		for i in range(len(graph[last])):
			node = graph[last][i]
			num_visits = get_num_vertex_in_path(node, path)
			if ((num_visits == 0)
				or ((scenario == 2 or scenario == 3) and node in cities)
				or (scenario == 3 and node in villages_with_passport and num_visits < 2)):
				new_path = path.copy()
				new_path.append(node)
				queue.append(new_path)
	print("Total number of paths: " + str(num_paths))

def print_path(path):
	''' Print path to the console. '''
	for i in range(len(path)):
		print(path[i], end = " ")
	print()
    
def get_num_vertex_in_path(v, path):
	''' Find the number of time vertex v appears in path. '''
	num = 0
	for i in range(len(path)):
		if (path[i] == v):
			num += 1
	return num

def get_list(line):
	''' Parse the line and return a list of vertices. '''
	lst = []
	for i in range(1, len(line)):
		x = line[i]
		if x.isupper():
			lst.append(x)
	return lst

if len(sys.argv) != 2:
	print("Usage: python3 Routes.py <inputfilename>")
	sys.exit()
file = open(sys.argv[1])
# file = open("test1.txt")

# read the file to get the vertices of the graph
cities = get_list(file.readline())
villages = get_list(file.readline())
villages_with_passport = get_list(file.readline())

# construct the graph
graph = dict()
line = "csc209 is the best"  # this is a placeholder string so that the while loop starts true
while(line):
	line = file.readline()
	if line:
		graph[line[0]] = get_list(line)

print("SCENARIO 1")
find_paths(graph, 1, cities, villages_with_passport)
print("SCENARIO 2")
find_paths(graph, 2, cities, villages_with_passport)
print("SCENARIO 3")
find_paths(graph, 3, cities, villages_with_passport)