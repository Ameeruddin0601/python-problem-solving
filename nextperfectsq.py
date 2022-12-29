import math
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    if math.sqrt(sq)%1==0:
        return (math.sqrt(sq)+1)**2
    return -1
    #return (math.sqrt(sq)+1)**2 if math.sqrt(sq)%1==0 else -1
print(find_next_square(121))