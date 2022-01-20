# Filters out spaces and removes unwanted characters
def parse(f):
    # Reads in file text
    t_text = f.read()
    # Sorts through letters
    p_text = ''.join(filter(str.isalpha, t_text))
    # Makes all letters uppercase
    p_text = p_text.upper()

    return p_text


# Used to count the number of all the letters in the given file
def count_alpha(text):
    alpha = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    count = 0
    # Goes through and adds one to whichever letter has been found
    for i in text:
        count = count + 1
        if i == 'A':
            alpha[0] = alpha[0] + 1
        elif i == 'B':
            alpha[1] = alpha[1] + 1
        elif i == 'C':
            alpha[2] = alpha[2] + 1
        elif i == 'D':
            alpha[3] = alpha[3] + 1
        elif i == 'E':
            alpha[4] = alpha[4] + 1
        elif i == 'F':
            alpha[5] = alpha[5] + 1
        elif i == 'G':
            alpha[6] = alpha[6] + 1
        elif i == 'H':
            alpha[7] = alpha[7] + 1
        elif i == 'I':
            alpha[8] = alpha[8] + 1
        elif i == 'J':
            alpha[9] = alpha[9] + 1
        elif i == 'K':
            alpha[10] = alpha[10] + 1
        elif i == 'L':
            alpha[11] = alpha[11] + 1
        elif i == 'M':
            alpha[12] = alpha[12] + 1
        elif i == 'N':
            alpha[13] = alpha[13] + 1
        elif i == 'O':
            alpha[14] = alpha[14] + 1
        elif i == 'P':
            alpha[15] = alpha[15] + 1
        elif i == 'Q':
            alpha[16] = alpha[16] + 1
        elif i == 'R':
            alpha[17] = alpha[17] + 1
        elif i == 'S':
            alpha[18] = alpha[18] + 1
        elif i == 'T':
            alpha[19] = alpha[19] + 1
        elif i == 'U':
            alpha[20] = alpha[20] + 1
        elif i == 'V':
            alpha[21] = alpha[21] + 1
        elif i == 'W':
            alpha[22] = alpha[22] + 1
        elif i == 'X':
            alpha[23] = alpha[23] + 1
        elif i == 'Y':
            alpha[24] = alpha[24] + 1
        elif i == 'Z':
            alpha[25] = alpha[25] + 1

    return alpha, count


# Print out function to print given letter array
def print_out(alpha_array, count):
    for idx in range(len(alpha_array)):
        print(chr(idx + ord('A')) + " -- " + str(alpha_array[idx]) + " With a Frequency of: %" + (str(int((alpha_array[idx] / count)*100))), end="\n")

    return


# Main function used for user input and program output
def main():
    print("Enter the name of the file you would like to check(ie: test.txt): ")
    name = input()

    # opens file defined by user
    f = open(name, 'r')

    # read all the letter and sort out unwanted characters
    p_text = parse(f)
    # close file
    f.close()
    # walk through text and count each letter
    alpha_array, count = count_alpha(p_text)
    # print out info
    print_out(alpha_array, count)

    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
