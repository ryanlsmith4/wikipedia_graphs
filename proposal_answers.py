from graph import Graph, Vertex
from read_file import read_file
# https://en.wikipedia.org/wiki/Main_Page
main = 'https://en.wikipedia.org/wiki/Main_Page'
philo = 'https://en.wikipedia.org/wiki/Philosophy'


graph = read_file()

'''find the shorest path to philosphy from
   an arbitrary access point'''
print(graph.bfs_ssp(main, philo) + '\n')

'''find a clique in the wikipedia data from a random entry point '''
print('In the test data there occurs an occurance of a clique\n')
print(graph.clique())

'''Is wiki data eulieran'''
print('Is Graph eulieran?\n')
print(graph.eulerian())