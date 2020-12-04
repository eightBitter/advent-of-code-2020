# Code for Day 3 of Advent of Code 2020

## Challenge 1
### The toboggan can only follow a few specific slopes (you opted for a cheaper model 
### that prefers rational numbers); start by counting all the trees you would encounter 
### for the slope right 3, down 1

### From your starting position at the top-left, check the position that is right 3 and down 1. 
### Then, check the position that is right 3 and down 1 from there, and so on until you go past 
### the bottom of the map. Due to something you read about once involving arboreal genetics and 
### biome stability, the same pattern repeats to the right many times.

## Challenge 2
### Determine the number of trees you would encounter if, for each of the following 
### slopes, you start at the top-left corner and traverse the map all the way to the 
### bottom:

### Right 1, down 1.
### Right 3, down 1. (This is the slope you already checked.)
### Right 5, down 1.
### Right 7, down 1.
### Right 1, down 2.

class Map:
    
    # sets variables for each instance
    def __init__(self):
        self.position = [0,0]
        self.map_data = []
        self.num_trees = 0

    def get_position(self):
        return self.position

    def incr_position(self, lat, long):
        # increments the position list
        self.position[0] = self.position[0] + long
        self.position[1] = self.position[1] + lat

    def eval_position(self):
        # uses the position as an index to check a specific point in the map
        return self.map_data[self.position[1]][self.position[0]]
    
    def get_map(self):
        return self.map_data

    def set_map(self):
        # creates the map data by importing a text file
        with open('day3/data/map.txt','r') as map_file:
            for map_line in map_file:
                self.map_data.append(map_line.replace("\n", ""))

    def extend_map(self):
        # double the map data using list comprehension 
        self.map_data = [map_line + map_line for map_line in self.map_data] 

    def incr_num_trees(self):
        self.num_trees = self.num_trees + 1

    def get_num_trees(self):
        return self.num_trees

    def traverse_map(self, lat, long):
        while self.get_position()[1] <= len(self.get_map())-1:
            ## if the longitude of the position is greater than the length of a map line, extend the map
            if self.get_position()[0] >= len(self.get_map()[0]):
                self.extend_map()
            ## if a specific point in the map data equals "#", increment the number trees in num_trees
            if self.eval_position() == "#":
                self.incr_num_trees()
            ## map to the next position by incrementing the position
            self.incr_position(lat, long)

## creates a Map object and calculates the number of trees encountered based on the specified path
def mapping_it_out(lat,long):
    map = Map()
    map.set_map()
    ## while latitude of the position is less than or equal to the length of map data, keep running
    map.traverse_map(lat,long)
    return  map.get_num_trees()

def main():
    trees_combined = mapping_it_out(1,1) * mapping_it_out(1,3) * mapping_it_out(1,5) * mapping_it_out(1,7) * mapping_it_out(2,1)
    print(trees_combined)


if __name__ == "__main__":
    main()

    