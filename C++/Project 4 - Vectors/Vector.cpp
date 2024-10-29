#include "Vector.h"
using namespace std;

void Vector::grow() {

}

Vector::Vector(){

}

// COPY CONSTRUCTOR
Vector::Vector(const Vector& v) : capacity(v.capacity), n_elems(v.n_elems) {
    data_ptr = new int[capacity];

    for (size_t i = 0; i < capacity; i++) {
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
        for (size_t i = 0; i < capacity; i++) {
            data_ptr[i] = v.data_ptr[i];
        }
     }
     return *this;
}

int Vector::front() const {

}