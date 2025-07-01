#include <iostream>
#include "bits.h"

using namespace std;

int main() {
    // Create bits class obj
    Bits testBits; // Default constructor
    cout << endl << " ---------------------- Bits object created ----------------------------------------------- " << endl;
    cout << "    Test Bits: " << testBits << endl;
    cout << "         Size: " << testBits.size() << endl;
    cout << "         At 0: " << testBits.at(0) << endl;
    cout << "         At 1: " << testBits.at(1) << endl;
    testBits.set(10);
    cout << "    Set At 10: " << testBits << endl;
    testBits.set();
    cout << "      Set All: " << testBits << endl;
    testBits.reset(10);
    cout << "  Reset At 10: " << testBits << endl;
    testBits.reset();
    cout << "        Reset: " << testBits << endl;
    testBits.assign(8, true);
    cout << "Assign T at 8: " << testBits << endl; 
    testBits.assign(8, false);
    cout << "Assign F at 8: " << testBits << endl;
    testBits.assign(964);
    cout << "Assign to 964: " << testBits << endl;
    testBits.toggle(7);
    cout << "  Toggle at 7: " << testBits << endl;
    testBits.toggle();
    cout << "   Toggle All: " << testBits << endl;
    testBits.shift(2);
    cout << "      Shift 2: " << testBits << endl;
    testBits.shift(-2);
    cout << "     Shift -2: " << testBits << endl;
    testBits.rotate(4);
    cout << "     Rotate 4: " << testBits << endl;
    testBits.rotate(-4);
    cout << "    Rotate -4: " << testBits << endl;
    cout << "         Ones: " << testBits.ones() << endl;
    cout << "       Zeroes: " << testBits.zeroes() << endl;


    cout << " ------------------------------------------------------------------------------------------ " << endl << endl;

    // You can test other functions if you implement them later
    return 0;
};