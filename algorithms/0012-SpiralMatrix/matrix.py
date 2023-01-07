def spiral(size):
    # Update this variable to toggle debugging
    enable_debugging = False

    def debug_values(action):
        if not enable_debugging:
            return

        print(f"===== {action}")
        print(f"start_column: {start_column}")
        print(f"end_column: {end_column}")
        print(f"current_column: {current_column}")
        print(f"start_row: {start_row}")
        print(f"end_row: {end_row}")
        print(f"current_row: {current_row}")
        print(f"counter: {counter}")
        print(f"max_items: {max_items}")

    if size <= 0:
        raise ValueError("Size should be greater than 0.")

    start_row = 0
    start_column = 0
    end_row = size - 1
    end_column = size - 1
    current_row = 0
    current_column = 0

    counter = 0
    max_items = size * size

    _spiral = [[None for _ in range(size)] for _ in range(size)]
    while counter < max_items:
        debug_values("starting while block")

        for current_column in range(start_column, end_column + 1):
            debug_values("increasing column")

            counter += 1
            _spiral[current_row][current_column] = counter

        start_row += 1

        for current_row in range(start_row, end_row + 1):
            debug_values("increasing row")

            counter += 1
            _spiral[current_row][current_column] = counter

        end_column -= 1

        for current_column in range(end_column, start_column - 1, -1):
            debug_values("decreasing column")

            counter += 1
            _spiral[current_row][current_column] = counter

        end_row -= 1

        for current_row in range(end_row, start_row - 1, -1):
            debug_values("decreasing row")

            counter += 1
            _spiral[current_row][current_column] = counter

        start_column += 1

        debug_values("finishing while block")

    if enable_debugging:
        print("==== Final status")
        import pprint

        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(_spiral)
        print(f"counter: {counter}")

    return _spiral
