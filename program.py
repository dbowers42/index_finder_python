from domain.index_finder import find_index

examples = [
    ['A'],
    ['A', 'B', 'C', 'A', 'C'],
    ['A', 'A', 'B', 'B', 'C'],
    ['A', 'B', 'A', 'C', 'A'],
    ['A', 'B', 'B', 'B'],
    ['B', 'B', 'B', 'A']
]

for example in examples:
    print("-" * 100)
    print(example)
    print(find_index(example))