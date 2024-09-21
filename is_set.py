def is_set(data):
    if data is None:
        return False

if len(data) == 0:
    return True

for i in range(len(data)):
    if data[i] in data[:i:]:
        return False

    return True


