#include "split.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;

/* ---------- CUSTOMER ------------------------------------------------------------------- */
struct Customer
{
    int customerID;
    string name;
    string streetAddress;
    string city;
    string state;
    string zipCode;
    string phoneNumber;
    string email;

    // Constructor
    Customer(int customerID, const string& name, const string& streetAddress, const string& city, const string& state, const string& zipCode, const string& phoneNumber, const string& email)
    : customerID(customerID), name(name), streetAddress(streetAddress), city(city), state(state), zipCode(zipCode), phoneNumber(phoneNumber), email(email) {}
};

// Read a customer txt file and add new customers to list 
void readCustomers(const string& file, vector<Customer>& customers) {
    // Open customer text file
    ifstream f(file);

    if (!f.is_open()) {
        cerr << "Couldn't open file";
        return;
    }

    string s;

    // Create customer records
    while (getline(f, s)) {
        auto fields = split(s, ',');
        try {
            customers.push_back(Customer(stoi(fields[0]),fields[1],fields[2],fields[3],fields[4],fields[5],fields[6],fields[7]));
        }
        catch (const invalid_argument& e) {
            cerr << "Invalid customer creation";
        }
    }

    f.close();
}

// Search for customer by ID and print name if found
int findCustomer(int id, vector<Customer>& customers) {
    for (size_t i = 0; i < customers.size(); i++) {
        if (customers.at(i).customerID == id) {
            return i;
        }
    }
    cerr << "Customer ID not found" << endl;
    return -1;
}

/* ---------- ITEM ----------------------------------------------------------------------- */
struct Item
{
    int itemID;
    string description;
    double price;

    // Constructor
    Item(int itemID, const string& description, double price) : itemID(itemID), description(description), price(price) {}
};

// Read an item txt file and add new items to list 
void readItems(const string& file, vector<Item>& items) {
    // Open items text file
    ifstream f(file);

    if (!f.is_open()) {
        cerr << "Couldn't open file";
        return;
    }

    string s;

    // Create item records
    while (getline(f, s)) {
        auto fields = split(s, ',');
        try {
            items.push_back(Item(stoi(fields[0]),fields[1],stod(fields[2])));
        }
        catch (const invalid_argument& e) {
            cerr << "Invalid item creation";
        }
    }

    f.close();
}

// Search for item by ID and print description and price if found
int findItem(int id, const vector<Item>& items) {
    for (size_t i = 0; i < items.size(); i++) {
        if (items.at(i).itemID == id) {
            return i;
        }
    }
    return -1;
}

/* ---------- PURCHASE ------------------------------------------------------------------- */
// Calculate total of all items in purchases
double calculateTotal(const vector<Item>& purchases) {
    double total = 0;
    for (size_t i = 0; i < purchases.size(); i++) {
        total += purchases.at(i).price;
    }
    return total;
}

/* ---------- MAIN ----------------------------------------------------------------------- */
int main() {
    // Initialize lists
    vector<Customer> customers;
    vector<Item> items;
    vector<Item> purchases;

    // Process txt files
    readCustomers("customers.txt", customers);
    readItems("items.txt", items);

    // Output results of reading files
    cout << string(70, '-') << endl;
    cout << "Number of Customers: " << customers.size() << endl;
    cout << "    Number of Items: " << items.size() << endl;

    // Get customer
    cout << string(70, '-') << endl;
    cout << "Enter a Customer Number:" << endl;
    int input;
    cin >> input;
    int customerIndex = findCustomer(input, customers);
    if (customerIndex == -1) {
        cerr << "Customer not found. Exiting..." << endl;
        return 1;
    }
    cout << "Customer: " << customers.at(customerIndex).name << endl;

    // Item purchase loop
    bool purchasing = true;
    while (purchasing) {
        cout << endl << "Enter item ID to purchase. Enter 0 to finish:" << endl;
        cin >> input;
        if (input == 0) {
            purchasing = false;
        } else {
            int itemIndex = findItem(input, items);
            if (itemIndex != -1) {
                purchases.push_back(items.at(itemIndex));
                cout << endl << left << setw(40) << purchases.back().description << fixed << setprecision(2) << purchases.back().price << endl;
            } else {
                cerr << endl << "Item not found." << endl;
            }
        }
    }

    // Output totals
    cout << string(70, '-') << endl;
    cout << "Total Items: " << purchases.size() << endl;
    cout << " Total Cost: $" << fixed << setprecision(2) << calculateTotal(purchases) << endl;
    cout << string(70, '-') << endl;

    return 0;
}