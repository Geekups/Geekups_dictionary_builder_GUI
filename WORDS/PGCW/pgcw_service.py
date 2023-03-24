import itertools as it


def combinations_functions(start_range, end_range, word_list):
    try:
        global results
        results = []
        # loop over range of lengths
        for i in range(start_range, end_range + 1):
            # get possible passwords by using itter.product function
            global prob_pass_list
            prob_pass_list = list(it.combinations(word_list, i))
            # iterate over each pass-list built by 'product' function
            for j in range(len(prob_pass_list)):
                # building our string password by joining probable words in [j] index
                global prob_pass_string
                prob_pass_string = ''.join(prob_pass_list[j])
                # finally should write the password in specific file
                results.append(prob_pass_string)
                results_str = "\r\n".join(results)

        return results_str

    except:
        print("something get fucked! try again or try another service")


def show_len():
    return len(results)


def combinations_functions_save(*, file_path="WORDS\pass_list.txt", start_range, end_range, word_list):
    try:
        # open the pass-list file after the loops to avoid repetitive action => reduce cpu usage
        with open(file_path, 'w') as file:
            # loop over range of lengths
            for i in range(start_range, end_range + 1):
                # get possible passwords by using itter.product function
                prob_pass_list = list(it.combinations(word_list, i))
                # iterate over each pass-list built by 'product' function
                for j in range(len(prob_pass_list)):
                    # building our string password by joining probable words in [j] index
                    prob_pass_string = ''.join(prob_pass_list[j])
                    # finally should write the password in specific file
                    file.write(f"{prob_pass_string} \n")
                    # return prob_pass_string
    except:
        print("something get fucked! try again or try another service")


if __name__ == "__main__":
    show_len()
