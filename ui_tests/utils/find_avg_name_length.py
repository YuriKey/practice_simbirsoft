def find_name_closest_to_average(names):
    lengths = [len(name) for name in names]

    average_length = sum(lengths) / len(lengths)

    closest_name = min(
        names,
        key=lambda name: abs(len(name) - average_length)
    )
    return closest_name
