#include <iostream>
#include <mutex>
using namespace std;

void f(const string & s) {
   mutex m;
    for (int i=0; i < 10; ++i) {
        m.lock();
        for (char c: s)
            cout << c;
        cout << '\n';
        m.unlock();
    }
}

int main() {
    thread t1{f,"It's a Dessert Topping"};
    thread t2{f,"It's a Floor Wax"};
    t1.join();
    t2.join();
}
