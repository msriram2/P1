

def read_calls(file: open) -> {(str, str): int}:

    with open(file) as my_file:
        contents = []
        for line in my_file:
            char = line.split(':')
            contents.append(char)

        print(contents)

    tuples_dict = {}
    for line in contents:
        split_line = line.split()
        caller = split_line[0]
        final_rec = split_line[-1]
        index = 0
        num_times = 0
        while split_line(index) != final_rec:
            if index % 2 == 0:
                receiver = split_line[index]
                key = tuples_dict[caller]
                for key in tuples_dict:
                    if receiver == key[1]:
                        num_times += 1
                        tuples_dict[key] = num_times
                    else:
                        str_tuple = (caller, receiver)
                        tuples_dict[str_tuple] = 0

        return tuples_dict



def call1to2(calls: {(str, str): int}) -> {str: {str: int}}:
    total_calls = {}
    for key, value in calls.items():
        total_call_key = key[0]
        total_keys = calls.key()
        inner_dict = {}
        if total_call_key in total_keys:
            value = calls[total_call_key]
            inner_dict[key[1]] = value
        total_calls[total_call_key] = inner_dict

    return inner_dict
