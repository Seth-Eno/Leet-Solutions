class Solution {
public:

    void drink(int& bottlesDrunk, int& fullBottles, int& emptyBottles, int& numExchange) {
        emptyBottles += fullBottles;
        bottlesDrunk += fullBottles;
        fullBottles = 0;
    }

    void exchange (int& bottlesDrunk, int& fullBottles, int& emptyBottles, int& numExchange) {
        emptyBottles -= numExchange;
        fullBottles += 1;
        numExchange += 1;
    }

    int maxBottlesDrunk(int numBottles, int numExchange) {
        int bottlesDrunk = 0;
        int fullBottles = numBottles;
        int emptyBottles = 0;

        while (fullBottles > 0 || emptyBottles >= numExchange) {
            while (emptyBottles >= numExchange) {
                exchange(bottlesDrunk, fullBottles, emptyBottles, numExchange);
            }
            drink(bottlesDrunk, fullBottles, emptyBottles, numExchange);
        }

        return bottlesDrunk;

    }
};