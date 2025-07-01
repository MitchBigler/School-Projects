#include <iostream>
#include <string>
#include <cstring>

using namespace std;

// Output the menu to console
void PrintMenu() {
    cout << endl << "MENU" << endl;
    cout << "c - Number of non-whitespace characters" << endl;
    cout << "w - Number of words" << endl;
    cout << "f - Find text" << endl;
    cout << "r - Replace all !'s" << endl;
    cout << "s - Shorten spaces" << endl;
    cout << "q - Quit" << endl;
}

// Function to return num of white space chars
int GetNumOfNonWSCharacters(const string input) {
    int num = 0;
    for (auto c : input){
        if (!isspace(c)){
            num++;
        }
    }
    return num;
}

// Function to return num of words
int GetNumOfWords(const string input) {
    int num = 0;
    bool word = false;

    for (auto c : input){
        if (isalpha(c) || isdigit(c) || c == '\''){
            word = true;
        } else{
            if (word){
                word = false;
                num++;
            }
        }
    }
    return num;
}

int FindText(const string target, string input) {
    int num = 0;
    int inLen = input.length();
    int tarLen = target.length();

    for (int i = 0; i <= inLen - tarLen; i++) {
        int j;
        for (j = 0; j < tarLen; j++) {
            if (input[i + j] != target[j]) {
                break;
            }
        }
        if (j == tarLen) {
            num++;
            i += tarLen - 1;
        }
    }
    return num;
}

void ReplaceExclamation(string& input){
    for (auto& c : input) {
        if (c == '!') {
            c = '.';
        }
    }
}

void ShortenSpace(string& input){
    for (size_t i = 0; i < input.length(); i++) {
        if (isspace(input[i]) && isspace(input[i+1])){
            input.erase(i+1,1);
            i--;
        }
    }
}

// Run functions and return t/f if finished
bool ExecuteMenu(char choice, string& input) {
    string target;

    // Handle choice input
    switch (choice) {
        case 'c':
            cout << "Number of non-whitespace characters: " << GetNumOfNonWSCharacters(input) << endl;
            break;
        case 'w':
            cout << "Number of words: " << GetNumOfWords(input) << endl;
            break;
        case 'f':
            cout << "Enter a word or phrase to be found:" << endl;
            cin.ignore();
            getline(cin, target);
            cout << "\"" << target << "\"" << " instances: " << FindText(target, input) << endl;
            break;
        case 'r':
            ReplaceExclamation(input);
            cout << "Edited text: " << input << endl;
            break;
        case 's':
            ShortenSpace(input);
            cout << "Edited text: " << input << endl;
            break;
        case 'q':
            return true;
            break;
        default:
            break;
    }
    return false;
}

int main() {
    // Initialize variables
    string input;
    char choice;
    const char approvedChoices[] = "cwfrsq";
    bool finished = false;

    // Get and output user input
    cout << "Enter a sample text:" << endl << endl;
    //FIXME getline(cin, input);
    input = "We'll continue our quest in space.  There will be more shuttle flights and more shuttle crews and,  yes,  more volunteers, more civilians,  more teachers in space.  Nothing ends here;  our hopes and our journeys continue!";
    cout << "You entered: " << input << endl;

    while (!finished){

    // Output menu
    PrintMenu();

    // Get choice until valid
    cout << endl << "Choose an option:" << endl;
    cin >> choice;
    while (!(strchr(approvedChoices, choice))){
        cin >> choice;
    }

    // Send choice to switch
    finished = ExecuteMenu(choice, input);

    }

}