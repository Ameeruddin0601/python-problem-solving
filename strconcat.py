# def print_full_name(first_name, last_name):
#     # Write your code here
#     full_name = "Hello " + first_name + " " + last_name + "! You just delved into python"
#     print(full_name) 

# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)


def mutate_string(string, position, character):
    # li = list(string)
    # li[position] = character
    # string = ''.join(li)
    string = string[:position]+character+string[position+1:]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
