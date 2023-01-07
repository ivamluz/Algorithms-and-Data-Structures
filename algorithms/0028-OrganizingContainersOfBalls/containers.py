RESULT_IMPOSSIBLE = "Impossible"
RESULT_POSSIBLE = "Possible"


def organizingContainers(containers):
    counts_per_container = {}
    counts_per_type = {}

    for c in range(len(containers)):
        container = containers[c]

        for t in range(len(container)):
            type_count = container[t]

            if c not in counts_per_container:
                counts_per_container[c] = type_count
            else:
                counts_per_container[c] += type_count

            if t not in counts_per_type:
                counts_per_type[t] = type_count
            else:
                counts_per_type[t] += type_count

    is_possible = set(counts_per_container.values()) == set(counts_per_type.values())

    if is_possible:
        return RESULT_POSSIBLE
    else:
        return RESULT_IMPOSSIBLE
