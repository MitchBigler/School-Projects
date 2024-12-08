#include <iostream>
#include <fstream>
#include <vector>
#include <thread>
#include <mutex>
#include <cmath>

using namespace std;

// Global vars
const int MAX = 1000000;
const int THREADS = 4;
int currentNum = 2;
int totalPrimes = 0;
vector<int> primesFound(THREADS, 0);
mutex fileMutex;
mutex counterMutex;

// Global output file
ofstream f("primes.dat");

// Return t/f if number is prime
bool isPrime(int number) {
    if (number < 2){ 
        return false;
    }
    else if (number == 2) {
        return true;
    }
    else if (number % 2 == 0) {
        return false;
    }

    for (int i = 3; i <= sqrt(number); i += 2) {
        if (number % i == 0) { 
            return false;
        }
    }
    return true;
}


void findPrimes(int threadId) {
    while (true) {
        int num;

        // Lock to get next number
        {
            lock_guard<mutex> lock(counterMutex);
            if (currentNum > MAX) { 
                break;
            }
            num = currentNum += 1;
        }

        if (isPrime(num)) {
            // Lock to output to file
            {
                lock_guard<mutex> lock(fileMutex);
                f << num << endl;
                totalPrimes += 1;
            }
            primesFound[threadId] += 1;
        }
    }
}

int main() {
    vector<thread> threads_list;

    // Create threads
    for (int i = 0; i < THREADS; i++) {
        threads_list.emplace_back(findPrimes, i);
    }

    // Join threads
    for (auto &thread : threads_list) {
        thread.join();
    }

    f.close();

    // Output results
    cout << "--------------------------------" << endl;
    cout << " Total # of primes found: " << totalPrimes << endl;
    for (int i = 0; i < THREADS; i++) {
        cout << "  Thread " << i << ": " << primesFound[i] << " primes found" << endl;
    }
    cout << "--------------------------------" << endl;

    return 0;
}
