class SimplePrintr():
    @classmethod
    def write(string, commit=False):
        if commit:
            print(string)
        else:
            print(string, end='\r')

    @classmethod
    def commit():
        print()