class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        // solution expects a vector output, so here is it created to hold the solution
        vector<int> solution;

        // for all 1st digits (i)...
        for (int i = 0; i < nums.size(); i++) {

                // for all 2nd digits (j)...
                for (int j = i+1; j < nums.size(); j++ ) {

                    // if first (i) + second (j) = target...
                    if (nums[i] + nums[j] == target) {

                        // add the indices to the solution set
                        solution.push_back(i);
                        solution.push_back(j);
                    }
                }
    }
    // submit solution
    return solution; 
    };
};