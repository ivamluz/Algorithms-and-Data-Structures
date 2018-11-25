# Solution was based on this really nice explanation from @dcvrn:
# https://www.hackerrank.com/challenges/unbounded-knapsack/forum/comments/87616

# Set this to True to enable debugging.
DEBUG = False

def unboundedKnapsack(targetSum, values, calculated = None):
    # calculated is initialized as None, instead of as {}, because of the way
    # Python treats default arguments: https://docs.python-guide.org/writing/gotchas/
    # In summary, the calculated value is kept for different function calls and the result
    # for a second list (see the unit tests) are wrongly inferred from the first call.
    if not calculated:
        calculated = {}
    
    if DEBUG:
        print "targetSum: %s" % targetSum
        print "values: %s" % values
        print "calculated: %s" % calculated

    if targetSum in calculated:
        return calculated[targetSum]

    # Sort the values first, so we don't need to iterate through the whole list
    # on every execution.
    sorted_values = sorted(values)

    for slot in range (1, targetSum + 1):
        calculated[slot] = 0

        for i in range(0, len(sorted_values)):
            value = sorted_values[i]
            if value == slot:
                calculated[slot] = value
                break
            elif value < slot:
                rest = slot - value

                result = value + unboundedKnapsack(rest, sorted_values, calculated)
                if result > calculated[slot]:
                    calculated[slot] = result
            else:
                break

    if DEBUG:
        print "calculated before return: %s" % calculated
        print "targetSum: %s, calculated[%s]: %s" % (targetSum, targetSum, calculated[targetSum])
    
    return calculated[targetSum]
