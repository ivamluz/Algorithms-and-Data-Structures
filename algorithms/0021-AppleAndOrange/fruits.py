def countApplesAndOranges(
    house_start,
    house_end,
    apples_tree_location,
    oranges_tree_location,
    apple_distances,
    orange_distances,
):
    def countFruits(tree_location, fruit_distances):
        count = 0
        for distance in fruit_distances:
            location = tree_location + distance
            if location >= house_start and location <= house_end:
                count += 1

        return count

    apples = countFruits(apples_tree_location, apple_distances)
    oranges = countFruits(oranges_tree_location, orange_distances)

    return (apples, oranges)
