class Cli:
    def __init__(self):
        print("Loading the files and and preparing the system...")
        self.search_input = None

    def input(self):
        """"
        Receives sentence to complete from user.
        """
        print("The system is ready. Enter your text:")
        self.search_input = input()
        return self.search_input

    def output(self, suggestions_list):
        """"
        Prints the suggestions list.
        """
        print(self.search_input)
        print("Here are the suggestions")
        for index in range(len(suggestions_list)):
            print(
                f"{index + 1}. {suggestions_list[index].completed_sentence} \n")
