#include "split.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iomanip>
#include <list>
#include <algorithm>

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

// Global Customer vector
vector<Customer> customers;

// Read a customer txt file and add new customers to list 
void read_customers(const string& file) {
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
int findCustomer(int id) {
    for (size_t i = 0; i < customers.size(); i++) {
        if (customers.at(i).customerID == id) {
            return i;
        }
    }
    cerr << "Customer ID not found" << endl;
    return -1;
}

/* ---------- ITEM ----------------------------------------------------------------------- */
struct Item {
    int itemID;
    string description;
    double price;


    Item(int itemID, const string& description, double price)
        : itemID(itemID), description(description), price(price) {}
};

struct LineItem : public Item {
    int qty;

    LineItem(int itemID, const string& description, double price, int qty)
        : Item(itemID, description, price), qty(qty) {}

    // Compare override for sorting
    friend bool operator<(const LineItem& item1, const LineItem& item2) {
        return item1.itemID < item2.itemID;
    }
};

// Global Items Vector
vector<Item> items;

// Read an item txt file and add new items to list 
void read_items(const string& file) {
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
int findItem(int id) {
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

/* ---------- PAYMENT -------------------------------------------------------------------- */
struct Payment {
    double amount;
    virtual string print_detail() = 0;
    virtual ~Payment() = default;
};

// CREDIT
struct Credit : public Payment
{
    string card_number;
    string expiration;


    Credit(string card_num, string expir) 
    : card_number(card_num), expiration(expir) {}

    string print_detail() override {}
};

// PAYPAL
struct PayPal : public Payment
{
    string paypal_id;

    PayPal(string id) 
    : paypal_id(id){}

    string print_detail() override {}
};

// WIRETRANSFER
struct WireTransfer : public Payment
{
    string bank_id;
    string account_id;

    WireTransfer(string bankID, string accountID) 
    : bank_id(bankID), account_id(accountID) {}

    string print_detail() override {}
};

/* ---------- ORDER ---------------------------------------------------------------------- */

struct Order {
    int order_id;
    string order_date;
    int cust_id;
    vector<LineItem> line_items;
    Payment* payment;

    Order(int order_id, string order_date, int cust_id, vector<LineItem> line_items, Payment* payment) 
            : order_id(order_id), order_date(order_date), cust_id(cust_id), line_items(line_items), payment(payment) {}

    // CALCULATE TOTAL
    double total() const {
        double total = 0;
        for (size_t i = 0; i < line_items.size(); i++) {
            total += line_items.at(i).price * line_items.at(i).qty;
        }
        return total;
    }

    // PRINT ORDER
    string print_order() const {
        stringstream ss;

        ss << "===========================" << endl;
        ss << "Order #" << order_id << ", Date: " << order_date << endl;
        ss << "Amount: $" << fixed << setprecision(2) << total() << ", Paid by ";
        if (dynamic_cast<Credit*>(payment)) {
            auto credit = static_cast<Credit*>(payment);
            ss << "Credit card " << credit->card_number << ", exp. " << credit->expiration << endl;
        } else if (dynamic_cast<PayPal*>(payment)) {
            auto paypal = static_cast<PayPal*>(payment);
            ss << "PayPal ID: " << paypal->paypal_id << "endl";
        } else if (dynamic_cast<WireTransfer*>(payment)) {
            auto wire = static_cast<WireTransfer*>(payment);
            ss << "Wire transfer from Bank ID " << wire->bank_id << ", Account# " << wire->account_id << endl;
        } else {
            ss << "Unknown" << endl;
        }

        ss << endl << "Customer ID #" << cust_id << ":" << endl;

        int custIndex = findCustomer(cust_id);

        ss << customers.at(custIndex).name << ", ph. " << customers.at(custIndex).phoneNumber << ", email: " << customers.at(custIndex).email << endl;
        ss << customers.at(custIndex).streetAddress << endl << customers.at(custIndex).city << ", " << customers.at(custIndex).state << " " << customers.at(custIndex).zipCode << endl;
        ss << endl << "Order Detail:" << endl;

        for (const auto& item : line_items) {
            ss << "       Item " << item.itemID << ": \"" << item.description << "\", "
                 << item.qty << " @ " << fixed << setprecision(2) << item.price << endl;
        }
        return ss.str();
    }
};

// ORDERS LISt
list<Order> orders;

// READ ORDERS
void read_orders(const string& file) {
    // Open orders text file
    ifstream f(file);

    if (!f.is_open()) {
        cerr << "Couldn't open file" << endl;
        return;
    }

    string s;

    while (getline(f, s)) {
        auto fields = split(s, ',');

        // Validate structure
        if (fields.size() < 2) {
            cerr << "Invalid format: " << s << endl;
            continue;
        }

        // Set fields vars
        int custID = stoi(fields[0]);
        string date = fields[2];
        int orderID = stoi(fields[1]);
        vector<LineItem> read_items;

        // Parse items from fields
        for (size_t i = 3; i < fields.size(); ++i) {
            auto item = split(fields[i], '-');
            if (item.size() > 3) {
                cerr << "Invalid line item format: " << fields[i] << endl;
                continue;
            }

            try {
                int item_id = stoi(item[0]);
                int qty = stoi(item[1]);

                // get item from the global items vector
                int itemIndex = findItem(item_id);
                if (itemIndex == -1) {
                    cerr << "Item ID not found: " << item_id << endl;
                    continue;
                }

                Item* globalItem = &items.at(itemIndex);

                // Add line item to the vector
                read_items.push_back(LineItem(globalItem->itemID, globalItem->description, globalItem->price, qty));
            } catch (const exception& e) {
                cerr << "Error with line item: " << fields[i] << " - " << e.what() << endl;
            }
        }

        sort(read_items.begin(), read_items.end());

        // Read payment information
        Payment* pay_ptr = nullptr;
        if (getline(f, s)) {
            auto payline = split(s, ',');

            try {
                int paymentType = stoi(payline[0]);
                if (paymentType == 1 && payline.size() >= 3) {
                    pay_ptr = new Credit(payline[1], payline[2]);
                } else if (paymentType == 2 && payline.size() >= 2) {
                    pay_ptr = new PayPal(payline[1]);
                } else if (paymentType == 3 && payline.size() >= 3) {
                    pay_ptr = new WireTransfer(payline[1], payline[2]);
                } else {
                    cerr << "Invalid payment format: " << s << endl;
                }
            } catch (const exception& e) {
                cerr << "Error processing payment: " << s << " - " << e.what() << endl;
            }
        }

        // Add the order to the orders list
        try {
            orders.push_back(Order(stoi(fields[1]), fields[2], stoi(fields[0]), read_items, pay_ptr));
        } catch (const exception& e) {
            cerr << "Error creating order: " << e.what() << endl;
        }
    }

    f.close();
}

/* ---------- MAIN ----------------------------------------------------------------------- */
int main() {
    read_customers("customers.txt");
    read_items("items.txt");
    read_orders("orders.txt");

    ofstream ofs("order_report.txt");
    for (const auto& order: orders) {
        ofs << order.print_order() << endl;
    }
}