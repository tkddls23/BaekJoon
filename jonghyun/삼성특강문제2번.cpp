
#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <string>
#include <cstring>
#include <cmath>
#include <stack>
#include <queue>
#include <cstring>
#include <sstream>
#include <map>
#include <unordered_map>

void solution(std::string string, int i, int i1);

int checkNum1(int x, int y, int stp, std::string str, std::string& ans);

using namespace std;


int main(int argc, char **argv) {
    cin.tie(NULL);
    cout.tie(NULL);
    int test_case;
    int T;
    cin >> T;
    for (test_case = 1; test_case <= T; ++test_case) {

        string str;
        int x, y;
        cin >> str >> x >> y;

        cout << "#" << test_case << " ";
        solution(str, x, y);
        cout << "\n";
    }
    return 0;
}

void solution(string str, int x, int y) {
    int ca = 0;
    int flag = 0;
    int targetIndex = -1;
    string ans = "";
    if((str.length() == 1 && str[0] - '0' < x) || (str.length() == 1 && x == 0 && str[0] - '0' < y)) {
        cout << -1;
        return;
    }

    flag = checkNum1(x, y, 0, str, ans);

    for(int startPoint=1; startPoint < str.length(); startPoint++) {
        if(flag == -1 || flag == 1) {
            ans += to_string(y);
        } else if(flag == 2 || flag == 3) {
            int num = str[startPoint] - '0';
            if(num < x) {
                if(flag == 2) {
                    flag = 100;
                    ans = "";
                    break;
                }
                if(targetIndex == -1) {
                    flag = 101;
                    ans = "";
                    break;
                }
                ans[targetIndex] = (char)(x + 48);
                flag = -1;
                for (int i = targetIndex + 1; i < ans.length(); ++i) {
                    ans[i] = (char)(y + 48);
                }
                ans += (char)(y + 48);
            } else if(num == x) {
                ans += to_string(x);
            } else if(num == y) {
                if(str.length() >= startPoint + 2 && str[startPoint + 1] - '0' < x) {
                    ans += to_string(x);
                    flag = -1;
                    continue;
                }
                targetIndex = startPoint;
                ans += to_string(y);
                flag = 3;
            } else {
                if(num > y) {
                    ans += to_string(y);
                } else {
                    ans += to_string(x);
                }
                flag =  1;
            }
        }
    }
    if(flag == 100) {
        for (int i = 0; i < str.length()-1; ++i) {
            cout << y;
        }
    } else if(flag == 101) {
        cout << x;
        for (int i = 0; i < str.length()-1; ++i) {
            cout << y;
        }
    }
    else cout << ans;
}

int checkNum1(int x, int y, int startPoint, string str, string& ans) {

    int num = str[startPoint] - '0';
    if(num < x) {
        return -1;
    } else if(num == x) {
        ans += to_string(x);
        return 2;
    } else if(num == y) {
        if(str.length() >= startPoint + 2 && str[startPoint + 1] - '0' < x) {
            ans += to_string(x);
            return -1;
        }
        ans += to_string(y);
        return 3;
    } else {
        if(num > y) {
            ans += to_string(y);
        } else {
            if(x != 0)
                ans += to_string(x);
        }
        return 1;
    }
}