def longest_common_prefix(strs):
    if not strs:
        return ""  # If the input list is empty, return an empty string

    # Sort the input list of strings lexicographically
    sorted = strs.sort()

    # Take the first and last strings in the sorted list
    first = strs[0]
    last = strs[-1]

    # Compare the characters of the first and last strings
    # to find the common prefix
    prefix = ""
    for i in range(min(len(first), len(last))):
        if first[i] == last[i]:
            prefix += first[i]
        else:
            break

    return prefix


# Example usage:
strings = ["flaower", "flibo", "flight"]
print(longest_common_prefix(strings))  # Output: "fl"
