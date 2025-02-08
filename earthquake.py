
def findEarthquake(sequence):
    n = len(sequence)
    max_duration = 0
    count_ones = 0  # Track the length of the current cluster of 1's
    leading_zeros = 0  # Track the number of leading zeros before the cluster

    i = 0
    while i < n:
        if sequence[i] == "0":
            if count_ones == 0:
                leading_zeros += 1  # Count leading zeros
            else:
                # End of a cluster of 1's, check for trailing zeros
                trailing_zeros = 0
                while i < n and sequence[i] == "0":
                    trailing_zeros += 1
                    i += 1

                # Valid earthquake: at least 2 leading and trailing zeros
                if leading_zeros >= 2 and trailing_zeros >= 2:
                    max_duration = max(max_duration, count_ones)

                # Reset for the next cluster
                count_ones = 0
                leading_zeros = trailing_zeros
                continue
        else:
            # Count the length of the current cluster of 1's
            count_ones += 1

        i += 1

    return max_duration


# Input parsing
n = int(input().strip())
sequence = input().strip().replace(" ", "")

# Output the maximum duration
print(findEarthquake(sequence))
