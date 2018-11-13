import numpy as np

trans_matrix = np.array(([0.3, 0, 0.5], [0.8, 0.2, 0], [0.6, 0.2, 0]))
emis_matrix = np.array(([0.2, 0.4, 0.4], [1, 0, 0], [0, 0.5, 0.5]))
words = ["young", "man", "wall"]
trans_symbol = ["N", "A", "V"]
start_prob = np.array([0.8, 0.2, 0])
end_prob = np.array([0.2, 0, 0.2])
path = "viterbi.txt"
backtrace = []
pos = []

viterbi_matrix = np.zeros((len(trans_matrix), len(words)))
forward_matrix = np.zeros((len(trans_matrix), len(words)))
word_index = words.index(words[0])
backtrace = np.zeros((len(trans_matrix), len(words)))

with open(path, "w") as write_file:
    print "----- viterbi algorithm calculation -----"
    write_file.write("----- viterbi algorithm calculation -----\n")
    total = 0
    pos.append("<s>")
    for col in range(0, len(trans_matrix)):
        viterbi_matrix[col, 0] = start_prob[col] * emis_matrix[col, word_index]
        forward_matrix[col, 0] = start_prob[col] * emis_matrix[col, word_index]
        if start_prob[col] * emis_matrix[col, word_index] > total:
            backtrace[col, 0] = col
        print str(start_prob[col]) + " * " + str(emis_matrix[col, word_index]) + " = " + str(viterbi_matrix[col, 0])
        write_file.write(str(start_prob[col]) + " * " + str(emis_matrix[col, word_index]) + " = " + str(viterbi_matrix[col, 0]) + "\n")
    
    for row in range(1, len(words)):
        word_index = words.index(words[row])
        for col in range(0, len(trans_matrix)):
            total = 0
            f_total = 0
            for t_col in range(0, len(trans_matrix)):
                arr = []
                arr.append(str(viterbi_matrix[t_col, row-1]))
                arr.append("*")
                arr.append(str(trans_matrix[t_col, col]))
                arr.append("*")
                arr.append(str(emis_matrix[col, word_index]))
                arr.append("=")
                arr.append(str(viterbi_matrix[t_col, row-1] * trans_matrix[t_col, col] * emis_matrix[col, word_index]))
                print " ".join(arr)
                write_file.write(" ".join(arr) + "\n")
                
                f_total += forward_matrix[t_col, row-1] * trans_matrix[t_col, col] * emis_matrix[col, word_index]
                if viterbi_matrix[t_col, row-1] * trans_matrix[t_col, col] * emis_matrix[col, word_index] > total:
                    total = viterbi_matrix[t_col, row-1] * trans_matrix[t_col, col] * emis_matrix[col, word_index]
                    backtrace[col, row] = t_col
            viterbi_matrix[col, row] = total
            forward_matrix[col, row] = f_total

            print "- SELECT = " + str(viterbi_matrix[col, row])
            write_file.write("- SELECT = " + str(viterbi_matrix[col, row]) + "\n")

    viterbi_final = 0
    forward_final = 0
    for col in range(0, len(trans_matrix)):
        final = []
        final.append(str(viterbi_matrix[col, len(words)-1]))
        final.append("*")
        final.append(str(end_prob[col]))
        final.append("=")
        final.append(str(viterbi_matrix[col, len(words)-1] * end_prob[col]))
        print " ".join(final)
        write_file.write(" ".join(final) + "\n")
        
        forward_final += forward_matrix[col, len(words)-1] * end_prob[col]
        if viterbi_matrix[col, len(words)-1] * end_prob[col] > viterbi_final:
            viterbi_final = viterbi_matrix[col, len(words)-1] * end_prob[col]
            backtrace[col, len(words)-1] = col
    print "- SELECT = " + str(viterbi_final)
    write_file.write("- SELECT = " + str(viterbi_final) + "\n")

    final_backtrace = np.argmax(backtrace, axis=0)
    for i in final_backtrace:
        pos.append(trans_symbol[i])
    pos.append("</s>")

    print "----- viterbi algorithm matrix -----"
    write_file.write("----- viterbi algorithm matrix -----\n")
    print viterbi_matrix
    write_file.write(str(viterbi_matrix) + "\n")
    print "----- final viterbi probability -----"
    write_file.write("----- final viterbi probability -----\n")
    print viterbi_final
    write_file.write(str(viterbi_final))
    print "----- most likely sequence of part-of-speech -----"
    write_file.write("----- most likely sequence of part-of-speech -----\n")
    print " ".join(pos)
    write_file.write(" ".join(pos) + "\n")
    print "----- conditional probability of most-lilkely sequence given the words -----"
    write_file.write("----- conditional probability of most-lilkely sequence given the words -----\n")
    print "p(tags|words) : " + str(viterbi_final / forward_final)
    write_file.write("p(tags|words) : " + str(viterbi_final / forward_final) + "\n")

