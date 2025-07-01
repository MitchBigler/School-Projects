#include <iostream>
#include <cassert>
#include <bitset>

class Bits {
    using IType = unsigned long long; // We only have to change the integer type here, if desired
    enum {NBITS = sizeof(IType)*8};
    IType bits = 0;
public:
    Bits() = default;
    Bits(IType n) {
        bits = n;
    }

    // Returns size of bits
    static int size() {
        return NBITS;
    }

    // Returns (tests) the bit at bit-position pos
    bool at(int pos) const {  
        assert(0 <= pos && pos < NBITS);
        return bits & (IType(1) << pos);
    }

    // Sets the bit at position pos
    void set(int pos) {  
        bits |= (IType(1) << pos);
    }
    // Sets all bits
    void set() {            
        bits |= -1;
    }

    // Resets (makes zero) the bit at position pos
    void reset(int pos) {     
        bits &= ~(IType(1) << pos);
    }
    // Resets all bits
    void reset() {             
        bits = 0;
    }

    // Sets or resets the bit at position pos depending on val
    void assign(int pos, bool val) { 
        if (val){
            bits |= (IType(1) << pos);
        } else {
            bits &= ~(IType(1) << pos);
        }
    }
    // Replaces the underlying integer with n
    void assign(IType n){
        bits = n;
    }

    // Flips the bit at position pos
    void toggle(int pos) {
        bits ^= (IType(1) << pos);
    }
    // Flips all bits
    void toggle(){
        bits ^= -1;
    }

    // If n > 0, shifts bits right n places; if n < 0, shifts left
    void shift(int n){
        if (n > 0) {
            bits >>= n;
        } else {
            bits <<= -n;
        }
    }

    // If n > 0, rotates right n places; if n < 0, rotates left
    void rotate(int n) {
        if (n > 0) { // Rotate Right
            while (n > 0) {
                if (bits & IType(1)) {
                    bits = (bits >> IType(1));
                    this->set(NBITS-1);
                } else {
                    bits = (bits >> IType(1));
                }
                n -= 1;
            }
        }
        if (n < 0) { // Rotate Left
            while (n < 0) {
                if (this->at(NBITS-1)) {
                    bits = (bits << IType(1));
                    this->set(0);
                } else {
                    bits = (bits << IType(1));
                }
                n += 1;
            }           
        }
    }

    // Returns how many bits are set in the underlying integer
    int ones() const {
        int num = 0;
        IType nbits = bits;
        while (nbits) {
            if (nbits & IType(1)) {
                num += IType(1);
            }
            nbits >>= IType(1);
        }
        return num;
    }
    int zeroes() const {      // Returns how many bits are reset in the underlying integer
        return NBITS - ones();
    }

    IType to_int() const {
        return bits;
    }
    friend bool operator==(const Bits& b1, const Bits& b2) {
        return b1.bits == b2.bits;
    }
    friend bool operator!=(const Bits& b1, const Bits& b2) {
        return b1.bits != b2.bits;
    }
    friend std::ostream& operator<<(std::ostream& os, const Bits& b) {
        return os << std::bitset<NBITS>(b.bits);    // Be sure to #include <bitset>
    }
};