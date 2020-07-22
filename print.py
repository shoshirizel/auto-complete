from search import get_best_completions, open_files


def input_fun():
    print("Loading the files and and preparing the system...")
    open_files()
    print("The system is ready. Enter your text:")
    search_input = input()
    suggestion_list = get_best_completions(search_input)
    output_fun(suggestion_list)
    print(search_input)


def output_fun(suggestions_list):
    print("Here are 5 suggestions")
    for index in range(len(suggestions_list)):
        print(
            f"{index + 1}. {suggestions_list[index].completed_sentence} \nscore: {suggestions_list[index].score} \n offset: {suggestions_list[index].offset}")


input_fun()
