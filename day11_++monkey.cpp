#include <vector>

class PlusPlusMonkey {
    public:
    // we use a vector since initializer list construction from cppyy
    // doesn't work for std::list :(
    std::vector<uint64_t> items;
    uint64_t add_amount;
    int divisible_test;
    int true_target;
    int false_target;
    int inspected = 0;

    PlusPlusMonkey(
        std::vector<uint64_t> items,
        uint64_t add_amount,
        int divisible_test,
        int true_target,
        int false_target
    )
    : items(items)
    , add_amount(add_amount)
    , divisible_test(divisible_test)
    , true_target(true_target)
    , false_target(false_target)
    {}

    uint64_t pop_item() {
        const auto x = items.front();
        items.erase(items.begin());
        return x;
    }

    void receive(uint64_t item) {
        items.push_back(item);
    }

    uint64_t next_worry(uint64_t worry) {
        inspected++;
        return worry + add_amount;
    }

    uint64_t throw_to(uint64_t worry) {
        return (worry % divisible_test) ? false_target : true_target;
    }
};
