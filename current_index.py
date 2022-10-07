
def get_cur_index():
    #this also increments the current index
    file_name = 'cur_index.txt'
    lines = ""
    
    with open(file_name) as f:
        lines = f.readlines()

    #print("Current cat index: " + lines[0])
    cur_index = int(lines[0])
    new_index = cur_index + 1 #change magic number here to increment cat list
    
    f = open(file_name, "w")
    f.write(str(new_index))
    f.close()
    return cur_index
