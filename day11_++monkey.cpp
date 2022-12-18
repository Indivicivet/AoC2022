#include <vector>

class PlusPlusMonkey {
    public:
    std::vector<int> items;
    int add_amount;
    int divisible_test;
    int true_target;
    int false_target;

    PlusPlusMonkey(
        std::vector<int> items,
        int add_amount,
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
};