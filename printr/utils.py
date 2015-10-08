def write(string, commit=False):
    ending = '\n' if commit else '\r'
    print(string, end=ending)

def commit():
    print()