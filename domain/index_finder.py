def find_index(items):
    buckets = {}

    for index, item in enumerate(items):
        if not buckets.get(item):
            buckets[item] = []

        buckets[item].append(index)

    filtered = [(key, buckets[key][0]) for key in buckets.keys() if len(buckets[key]) == 1]

    result = sorted(filtered, key=lambda x: (x[1], x[1]))

    return result if len(result) == 1 else None




