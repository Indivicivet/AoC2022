#include <vector>

class PlusPlusMonkey {
    public:
    std::vector<int> items;
    int add_amount;
    int divisible_test;
    int true_target;
    int false_target;
    int inspected = 0;

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

    int pop_item() {
        const auto x = items.back();
        items.pop_back();
        return x;
    }

    void receive(int item) {
        items.push_back(item);
    }

    int next_worry(int worry) {
        return worry + add_amount;
    }

    int throw_to(int worry) {
        return (worry % divisible_test) ? false_target : true_target;
    }
};
