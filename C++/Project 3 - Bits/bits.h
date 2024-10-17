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
    static int size() {
        return NBITS;
    }
    bool at(int pos) const {  // Returns (tests) the bit at bit-position pos
        assert(0 <= pos && pos < NBITS);
        return bits & (IType(1) << pos);
    }
    void set(int pos) {  // Sets the bit at position pos
        bits |= (IType(1) << pos);
    }

    void set() {            // Sets all bits
        bits |= -1;
    }

    void reset(int pos) {     // Resets (makes zero) the bit at position pos
        bits &= (IType(1) << pos);
    }

    void reset() {             // Resets all bits
        bits &= 0;
    }
    void assign(int pos, bool val); // Sets or resets the bit at position pos depending on val
    void assign(IType n);     // Replaces the underlying integer with n
    void toggle(int pos);     // Flips the bit at position pos
    void toggle();            // Flips all bits
    void shift(int n);        // If n > 0, shifts bits right n places; if n < 0, shifts left
    void rotate(int n);       // If n > 0, rotates right n places; if n < 0, rotates left
    int ones() const;         // Returns how many bits are set in the underlying integer
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