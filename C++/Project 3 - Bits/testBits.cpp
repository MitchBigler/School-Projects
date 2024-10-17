#include <iostream>
#include "bits.h"

using namespace std;

int main() {
    // Create bits class obj
    Bits testBits; // Default constructor
    cout << endl << " ---------------------- Bits object created ----------------------------------------------- " << endl;
    cout << "   Test Bits: " << testBits << endl;
    cout << "        Size: " << testBits.size() << endl;
    cout << "        At 0: " << testBits.at(0) << endl;
    cout << "        At 1: " << testBits.at(1) << endl;
    testBits.set(10);
    cout << "   Set At 10: " << testBits << endl;
    testBits.set();
    cout << "     Set All: " << testBits << endl;
    testBits.reset(10);
    cout << " Reset At 10: " << testBits << endl;
    testBits.reset();
    cout << "       Reset: " << testBits << endl;

    // You can test other functions if you implement them later
    return 0;
};