import sys

treemap_file = open(sys.argv[1])
treemap = treemap_file.read().strip().split("\n")
treemap_file.close()

max_x = len(treemap[0])
max_y = len(treemap)

def traversal(rate_x, rate_y):
    treecount = 0

    coord_x = 0
    coord_y = 0

    for line in treemap:
        if coord_y >= max_y:
            break

        if treemap[coord_y][coord_x] == '#':
            treecount += 1

        coord_x = (coord_x + rate_x) % max_x
        coord_y += rate_y

    return treecount
    
part1 = traversal(3, 1)
part2 = traversal(1, 1) * traversal(3, 1) * traversal(5, 1) * traversal(7, 1) * traversal(1, 2)

print("Part 1: %s" % part1)
print("Part 2: %s" % part2)
