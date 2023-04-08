#include <string>
#include <stack>
#include <unordered_map>

using namespace std;

bool is_valid(string s) {
    stack<char> stack;
    unordered_map<char, char> match = {
        {'(', ')'},
        {'[', ']'},
        {'{', '}'}
    };
    
    for (char c : s) {
        if (c == '(' || c == '[' || c == '{') {
            stack.push(c);
        } else if (c == ')' || c == ']' || c == '}') {
            if (stack.empty()) {
                return false;
            }

            char top = stack.top();
            if (c != match[top]) {
                return false;
            }
            stack.pop();
        } else {
            return false;
        }
    }
    return stack.empty();
}
