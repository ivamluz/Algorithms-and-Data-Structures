# lvl |  chars
# 1   | '   #   '
# 2   | '  ###  '
# 3   | ' ##### '
# 4   | '#######'
# spaces_before_and_after = levels - lvl
# chars = (lvl * 2) -1


def pyramids(levels):
    if levels <= 0:
        raise ValueError("Levels should be greather than 0.")

    pyramid = ""
    for level in range(1, levels + 1):
        spaces = levels - level
        blocks = (level * 2) - 1

        pyramid += (" " * spaces) + ("#" * blocks) + (" " * spaces)

        if level < levels:
            pyramid += "\n"

    return pyramid
