import get_best_completions


def input_fun():
    print("Loading the files and and preparing the system...")
    complete = get_best_completions.Complete()
    search_input = 0
    while search_input != "-1":
        print("The system is ready. Enter your text:")
        search_input = input()
        suggestion_list = complete.get_best_completions(search_input)
        output_fun(suggestion_list)
        print(search_input)


def output_fun(suggestions_list):
    print("Here are the suggestions")
    for index in range(len(suggestions_list)):
        print(
            f"{index + 1}. {suggestions_list[index].completed_sentence} \n"
            f"  score: {suggestions_list[index].score} \n "
            f" offset: {suggestions_list[index].offset * -1}")


if __name__ == '__main__':
    input_fun()
