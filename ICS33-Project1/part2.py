def question1(n: dict) -> dict:
    new_dict = {value: key for (key,value) in n.items()}
    return new_dict

def question2(n: dict) -> dict:
    new_dict = {value: key for (key,value) in n.items() if value == key[value]}
    return new_dict

def question3(n: dict, m: dict) -> dict:
    new_dict = {n[k] + m[k] for (k,v) in n.items() and m.items() if n.key() == m.key()}
    return new_dict

def question4(n: list) -> list:
    new_list = [y for x in list1 for list1, list2 in n if y==x]
    return new_list
