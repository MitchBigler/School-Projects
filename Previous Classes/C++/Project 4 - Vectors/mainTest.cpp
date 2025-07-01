#include "Vector.h"
#include "test.h"
#include <stdexcept>
using namespace std;

int main() {
    Vector v;
    cout << "Made Vector" << endl;
    v.push_back(2);
    cout << "Added 2. " << "Front: " << v.front() << endl;
    v.push_back(4);
    cout << "Added 4. " << " Back: " << v.back() << endl;
    return 0;
}