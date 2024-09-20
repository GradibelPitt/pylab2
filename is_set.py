def match(is_set, test_set):
    if len(is_set) != len(test_set):
        return False
    return all(is_set[i] == test_set[i] for i in range(len(is_set)))

