#include <iostream>
#include <vector>
using namespace std;

int main() {

    // Initialize variables
    vector<int> jerseyNums;
    vector<int> ratings;
    size_t numMembers = 5;
    int jersey;
    int rating;
    char option;
    bool menu = true;

    // Get player num/rating numMember times
    for (size_t i = 0; i < numMembers; i++) {
        cout << "Enter player " << i + 1 << "'s jersey number:" << endl;
        cin >> jersey;
        cout << "Enter player " << i + 1 << "'s rating:" << endl << endl;
        cin >> rating;

        // Add input to vectors
        jerseyNums.push_back(jersey);
        ratings.push_back(rating);
    }

    // lambda functions
    auto addPlayer = [&ratings, &jerseyNums, &numMembers, &jersey, &rating](){
        cout << "Enter a new player's jersey number:" << endl;
        cin >> jersey;
        cout << "Enter the player's rating:" << endl;
        cin >> rating;
        cout << endl;

        // Add input to vectors
        jerseyNums.push_back(jersey);
        ratings.push_back(rating);
        numMembers++;
    };

    auto deletePlayer = [&ratings, &jerseyNums, &numMembers, &jersey, &rating](){
    cout << "Enter a new player's jersey number:" << endl;
    cin >> jersey;

    for (int i = 0; i < jerseyNums.size(); i++){
        if (jerseyNums.at(i) == jersey) {
            jerseyNums.erase(jerseyNums.begin() + i);
            ratings.erase(ratings.begin() + i);
            break;
        }
    }

    cout << endl;
    numMembers--;
    };

    auto updateRating = [&ratings, &jerseyNums, &numMembers, &jersey, &rating](){
    cout << "Enter a new player's jersey number:" << endl;
    cin >> jersey;

    for (int i = 0; i < jerseyNums.size(); i++){
        if (jerseyNums.at(i) == jersey) {
            cout << "Enter a new rating for player" << endl;
            cin >> rating;
            ratings.at(i) = rating;
            break;
        }
    }
    
    cout << endl;

    };

    auto outputAboveRating = [&ratings, &jerseyNums, &numMembers, &rating](){
        cout << "Enter a rating:" << endl;
        cin >> rating;
        
        cout << "ABOVE " << rating << endl;
        for (size_t i = 0; i < numMembers; i++) {
            if (ratings.at(i) > rating){
                cout << "Player " << i + 1 << " -- Jersey number: " << jerseyNums.at(i) << ", Rating: " << ratings.at(i) << endl;
            }
        }
        cout << endl;
    };

    auto outputRoster = [&ratings, &jerseyNums, &numMembers](){
        cout << "ROSTER" << endl;
        for (size_t i = 0; i < numMembers; i++) {
            cout << "Player " << i + 1 << " -- Jersey number: " << jerseyNums.at(i) << ", Rating: " << ratings.at(i) << endl;
        }
        cout << endl;
    };

    outputRoster();

    // Menu
    while (menu) {
        cout << "MENU" << endl;
        cout << "a - Add player" << endl;
        cout << "d - Remove player" << endl;
        cout << "u - Update player rating" << endl;
        cout << "r - Output players above a rating" << endl;
        cout << "o - Output roster" << endl;
        cout << "q - Quit" << endl;
        cout << endl << "Choose an option:" << endl;

        cin >> option;

    switch (option) {
        case 'a':
            addPlayer();
            break;
        case 'd':
            deletePlayer();
            break;
        case 'u':
            updateRating();
            break;
        case 'r':
            outputAboveRating();
            break;
        case 'o':
            outputRoster();
            break;
        case 'q':
            menu = false;
            break;
        default:
            cout << "Please select from the menu" << endl;
            break;
    }
    }



    return 0;
}