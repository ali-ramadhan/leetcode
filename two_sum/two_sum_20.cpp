#include <vector>
#include <unordered_map>

using namespace std;

vector<int> two_sum(vector<int>& nums, int target) {
    unordered_map<int, int> needed;
    for (auto i = 0; i < nums.size(); i++) {
	auto n = nums[i];
        if (needed.contains(target - n))
            return {needed[target - n], i};
        else
            needed[n] = i;
    }
    return {}; // Should never come to this.
}

int main() {}
