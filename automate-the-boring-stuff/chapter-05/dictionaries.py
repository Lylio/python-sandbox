birthtowns = {'Jeff': 'London', 'Andrea': 'Edinburgh', 'Polly': 'Glasgow', 'Billy': 'Manchester'}


def get_values():
    for v in birthtowns.values():
        print(v)

def get_keys():
    for k in birthtowns.keys():
        print(k)

def get_items():
    for i in birthtowns.items():
        print(i)

if __name__ == '__main__':
    get_keys()
    get_values()
    get_items()