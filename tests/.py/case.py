num = 1
input_file = 'exampletextfile.txt'

with open(input_file, 'r') as f :
    source_code = f.read()

match(num) :

    case 1:
        pass
    case _:
        pass