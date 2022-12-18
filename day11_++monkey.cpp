#include <vector>

class PlusPlusMonkey {
    public:
    std::vector<int> items;
    int mult_by;
    int divisible_test;
    int true_target;
    int false_target;

    PlusPlusMonkey(
        std::vector<int> items,
        int mult_by,
        int divisible_test,
        int true_target,
        int false_target
    )
    : items(items)
    , mult_by(mult_by)
    , divisible_test(divisible_test)
    , true_target(true_target)
    , false_target(false_target)
    {}
};
