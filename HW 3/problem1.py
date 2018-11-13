import numpy as np

trans_matrix = np.array(([0.3, 0, 0.5], [0.8, 0.2, 0], [0.6, 0.2, 0]))
emis_matrix = np.array(([0.2, 0.4, 0.4], [1, 0, 0], [0, 0.5, 0.5]))
words = ["young", "man", "wall"]
start_prob = np.array([0.8, 0.2, 0])
end_prob = np.array([0.2, 0, 0.2])
path = "forward.txt"

forward_matrix = np.zeros((len(trans_matrix), len(words)))
word_index = words.index(words[0])

with open(path, "w") as write_file:
    print "----- forward algorithm calculation -----"
    write_file.write("----- forward algorithm calculation -----\n")
    for col in range(0, len(trans_matrix)):
        forward_matrix[col, 0] = start_prob[col] * emis_matrix[col, word_index]
        print str(start_prob[col]) + " * " + str(emis_matrix[col, word_index]) + " = " + str(forward_matrix[col, 0])
        write_file.write(str(start_prob[col]) + " * " + str(emis_matrix[col, word_index]) + " = " + str(forward_matrix[col, 0]) + "\n")

    for row in range(1, len(words)):
        word_index = words.index(words[row])
        for col in range(0, len(trans_matrix)):
            total = 0
            arr = []
            for t_col in range(0, len(trans_matrix)):
                total += forward_matrix[t_col, row-1] * trans_matrix[t_col, col] * emis_matrix[col, word_index]
                arr.append(str(forward_matrix[t_col, row-1]))
                arr.append("*")
                arr.append(str(trans_matrix[t_col, col]))
                arr.append("*")
                arr.append(str(emis_matrix[col, word_index]))
                if t_col == len(trans_matrix)-1:
                    arr.append("=")
                else:
                    arr.append("+")
            forward_matrix[col, row] = total
            arr.append(str(forward_matrix[col, row]))
            print " ".join(arr)
            write_file.write(" ".join(arr) + "\n")

    forward_final = 0
    final = []
    for col in range(0, len(trans_matrix)):
        forward_final += forward_matrix[col, len(words)-1] * end_prob[col]
        final.append(str(forward_matrix[col, len(words)-1]))
        final.append("*")
        final.append(str(end_prob[col]))
        if col == len(trans_matrix)-1:
            final.append("=")
        else:
            final.append("+")
    final.append(str(forward_final))
    print " ".join(final)
    write_file.write(" ".join(final) + "\n")

    print "----- forward algorithm matrix -----"
    write_file.write("----- forward algorithm matrix -----\n")
    print forward_matrix
    write_file.write(str(forward_matrix) + "\n")
    print "----- final forward probability -----"
    write_file.write("----- final forward probability -----\n")
    print forward_final
    write_file.write(str(forward_final))

