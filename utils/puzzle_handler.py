from utils.dag import Graph
from collections import deque


def build_topology(num_chars: int, char_codes: list) -> deque:
    """
    Build a topologically sorted node structure from the passed character codec.
    It is expected that the codec resolves into a directed acyclic graph
    Args:
        num_chars: the total number of chars in puzzle. Each corresponds to a node in the graph
        char_codes: array of string containing the codes

    Returns:
        Topologically sorted dequeue of nodes

    """
    graph = Graph()

    for node in range(num_chars):
        graph.add_node(node)
    for idx, char_code in enumerate(char_codes):
        lt = char_code.find('<')
        if lt >= 0:
            graph.add_edge((lt - 1, idx))
        gt = char_code.find('>')
        if gt >= 0:
            graph.add_edge((idx, gt - 1))

    return graph.topological_sort()


def build_charset_from_topology(char_set: str, top_order: deque) -> list:
    """
    Build the solved character set using the sorted nodes.
    Args:
        char_set: string of characters (nodes of graph) eg: 'ABCD'
        top_order: topologically sorted nodes

    Returns:
        List containing the solved codes for each node

    """

    # initialize the response array. equal to the number of nodes
    char_code_array = [char_set] * len(char_set)
    # initialize the character code that will be associated with each node.
    char_code = ["<"] * (len(char_set)+1)   # space for character + all nodes: A<<<<

    last_node = top_order.pop()
    char_code[0] = char_set[last_node]
    char_code[last_node + 1] = "="
    char_code_array[last_node] = ''.join(char_code)

    while True:
        try:
            # since the next node will always be higher than the previous
            # we set the location of that last node in the current codec to be greater than
            char_code[last_node + 1] = ">"
            last_node = top_order.pop()
            char_code[0] = char_set[last_node]
            # set the current node's value as equals in the codec
            char_code[last_node + 1] = "="
            char_code_array[last_node] = ''.join(char_code)
        except IndexError:
            break

    return char_code_array


def solve_puzzle(puzzle: str) -> str:
    """
    Helper function that takes the puzzle string and returns the resulting response
    Args:
        puzzle: string

    Returns:
        string containing the solved response

    """
    puzzle = puzzle.split(':')[1].split('\n')[1:-1]
    char_set, char_codes = puzzle[0], puzzle[1:]
    num_chars = len(char_set) - 1
    if num_chars == len(char_codes):
        top_order = build_topology(num_chars, char_codes)
        codec = build_charset_from_topology(char_set.strip(), top_order)
        resp = char_set+'\n'+'\n'.join(codec)
        return resp



#print(solve_puzzle('Please solve this puzzle:\n ABCD\nA-->-\nB--<-\nC--=-\nD>---\n'))