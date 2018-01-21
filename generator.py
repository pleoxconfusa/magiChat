carp_1 = [[0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],[1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1]]
carp_2 = [[0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1],[1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0]]
carp_3 = [[0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],[1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0]]
carp_4 = [[1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1],[0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0]]

#function that calls the 16 number function and breaks up the list 
def generate_squares():
    squares = []
    
    #for each rotation of s, a, n, c
    for (s, a, n, c) in ((8, 1, 4, 2), (8, 4, 2, 1), (8, 2, 4, 1), (2, 4, 1, 8)):
        for s_val in (0, 1, 2, 3):
            for a_val in (0, 1):
                for n_val in (0, 1, 2, 3):
                    for c_val in (0, 1):
                        if s_val > 1:
                            s_mat = map(lambda x: x * s, carp_2[s_val%2])
                            a_mat = map(lambda x: x * a, carp_1[a_val])
                        else:
                            s_mat = map(lambda x: x * s, carp_1[s_val%2])
                            a_mat = map(lambda x: x * a, carp_2[a_val])
                        if n_val > 1:
                            n_mat = map(lambda x: x * n, carp_4[n_val%2])
                            c_mat = map(lambda x: x * c, carp_3[c_val])
                        else:
                            n_mat = map(lambda x: x * n, carp_3[n_val%2])
                            c_mat = map(lambda x: x * c, carp_4[c_val])
                        
                        square = map(sum, zip(s_mat, a_mat, n_mat, c_mat))
                        
                        if square not in squares:
                            squares.append(square)
                        
    return squares
    
def write_output(squares, file_name):
    destination = open(file_name, "w")
    
    write_string = ""
    
    count = 0
    
    for square in squares:
        for index in range(16):
            write_string = write_string + str(square[index])
            write_string = write_string + " "
        write_string = write_string + ": " + str(count) + "\n"
        count = count + 1
    
    destination.write(write_string)
    
    return 0

#main function to call previous function
def main():
    #write output to a new file in new format
    write_output(generate_squares(), "squares.txt")
    

if __name__ == "__main__": main()  