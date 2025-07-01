#include "Vector.h"
#include <stdexcept>
using namespace std;

// GROW - Allocate new array to increase capacity
void Vector::grow() {
    size_t new_capacity = this->capacity + CHUNK;
    int* new_data_ptr = new int[new_capacity];

    for (size_t i = 0; i < n_elems; i++) {
        new_data_ptr[i] = this->data_ptr[i];
    }

    delete[] this->data_ptr;
    this->data_ptr = new_data_ptr;
    this->capacity = new_capacity;

}

// DEFAULT CONSTRUCTOR
Vector::Vector() : capacity(CHUNK), n_elems(0), data_ptr(new int[CHUNK]) {
}

// COPY CONSTRUCTOR
Vector::Vector(const Vector& v) : capacity(v.capacity), n_elems(v.n_elems) {
    data_ptr = new int[capacity];

    for (size_t i = 0; i < n_elems; i++) {
        data_ptr[i] = v.data_ptr[i];
    }
}

// COPY ASSIGNMENT OPERATOR OVERLOAD
Vector& Vector::operator=(const Vector& v) {
     if (this != &v) {
        delete[] data_ptr;
        this->capacity = v.capacity;
        this->n_elems = v.n_elems;
        data_ptr = new int[capacity];
        for (size_t i = 0; i < n_elems; i++) {
            data_ptr[i] = v.data_ptr[i];
        }
     }
     return *this;
}

// DESTRUCTOR
Vector::~Vector() {
    delete[] data_ptr;
    data_ptr = nullptr;
}

// FRONT - Return int in position 0
int Vector::front() const {
    if (n_elems > 0) {
        return data_ptr[0];
    }
    else{
        throw std::range_error("Front() - empty list");
    }
}

// BACK - Return last element
int Vector::back() const {
    if (n_elems > 0) {
        return data_ptr[n_elems - 1];
    }
    else {
        throw std::range_error("Back() - empty list");
    }
}

// AT - Return element at pos parameter
int Vector::at(size_t pos) const {
    if (pos >= n_elems) {
        throw std::range_error("At() cannot access number not in vector");
    } 
    else {
        return data_ptr[pos];
    }
}

// SIZE - Return num of elements
size_t Vector::size() const {
    return n_elems;
}

// EMPTY - Return T/F if vector is empty
bool Vector::empty() const {
    return (n_elems == 0);
}

// Operator[] - At but with no bounds check
int& Vector::operator[](size_t pos) {
    return data_ptr[pos];
}

// PUSH_BACK - Append new element to end of array
void Vector::push_back(int elem) {
    if (n_elems == capacity) {
        grow();
    }
    data_ptr[n_elems] = elem;
    n_elems++;
}

// POP_BACK - decrease n_elems by 1
void Vector::pop_back() {
    if (n_elems == 0) {
        throw std::range_error("Pop_back() - empty list");
    } else {
    this->n_elems--;
    }
}

// ERASE - Remove item at pos paramter
void Vector::erase(size_t pos) {
    if (pos >= n_elems) {
        throw std::range_error("Erase() - pos out of range");
    } else {
        for (size_t i = pos; i < n_elems - 1; i++) {
            data_ptr[i] = data_ptr[i+1];
        }
    }
    n_elems--;
}

// INSERT - Add elem at pos parameter
void Vector::insert(size_t pos, int elem) {
    if (pos > n_elems) {
        throw std::range_error("Insert() - pos out of range");
    } else {
        if (n_elems == this->capacity) {
            grow();
        }

        for (size_t i = n_elems; i > pos; i--) {
            data_ptr[i] = data_ptr[i-1];
        }

        data_ptr[pos] = elem;

        n_elems++;
    }
}

// CLEAR - Set n_elems to 0
void Vector::clear() {
    this->n_elems = 0;
}

// BEGIN - Return pointer to first element
int* Vector::begin() {
    if (n_elems == 0) {
        return nullptr;
    }
    return &data_ptr[0];
}

// END - Return pointer to last element
int* Vector::end() {
    if (n_elems == 0) {
        return nullptr;
    }
    return &data_ptr[n_elems];
}

// OPERATOR'==' - Check if vectors are equal
bool Vector::operator==(const Vector& v) const {
    if (this->n_elems != v.n_elems) {
        return false;
    }

    for (size_t i = 0; i < this->n_elems; i++) {
        if (this->data_ptr[i] != v.data_ptr[i]) {
            return false;
        }
    }

    return true;
}

// OPERATOR'!=' - Return opposite of '=='
bool Vector::operator!=(const Vector& v) const {
    return !(*this == v);
}