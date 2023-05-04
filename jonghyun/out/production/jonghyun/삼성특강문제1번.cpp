//
// Created by jonghyun on 2023-01-07.
//

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

using namespace std;

char board[21][21];
int col, row;
pair<int, int> dir[4] = {{0,1}, {0,-1}, {1, 0}, {-1, 0}};
int DFS(pair<int, int> pair, string basicString, unordered_map<string, bool> checkMap[21][21]);
int size;
bool flag;

void solution(int i, int i1) {
    unordered_map<string, bool> checkMap[21][21];
    pair<int, int> start = {0, 0};
    string tempStr = "";
    tempStr += board[0][0];
    checkMap[0][0][tempStr] = true;
    cout << DFS(start, tempStr, checkMap);
}

bool stringContainsChar(string s, char c) {
    for (int i = 0; i < s.length(); ++i) {
        if (s[i] == c) return true;
    }
    return false;
}

int DFS(pair<int, int> start, string str, unordered_map<string, bool> checkMap[21][21]) {
    int ans = str.length();
    int x = start.first;
    int y = start.second;

    for (int i = 0; i < 4; ++i) {
        if (flag) return size;
        int x1 = x + dir[i].first;
        int y1 = y + dir[i].second;
        char boardVal = board[x1][y1];
        if (x1 >= col || y1 >= row || x1 < 0 || y1 < 0) continue;
        if (stringContainsChar(str, boardVal)) continue;
        if (checkMap[x1][y1].find(str) != checkMap[x1][y1].end()) continue;

        pair<int, int> temp = {x1, y1};
        string s = str + boardVal;
        sort(s.begin(),s.end());
        checkMap[x1][y1][s] = true;
        int dfs = DFS(temp, s, checkMap);
        ans = max(dfs, ans);
        if(size == ans) {
            flag = true;
        }
    }
    return ans;
}

int main(int argc, char **argv) {
    cin.tie(NULL);
    cout.tie(NULL);
    int test_case;
    int T;
    cin >> T;

    for (test_case = 1; test_case <= T; ++test_case) {
        size = 0;
        flag = false;
        unordered_map<char, int> sizeMap;
        cout << "#" << test_case << " ";

        cin >> col >> row;
        for (int i = 0; i < col; ++i) {
            string s;
            cin >> s;
            for (int j = 0; j < s.length(); ++j) {
                board[i][j] = s[j];
                sizeMap[s[j]] = 1;
            }
        }
        size = sizeMap.size();
        solution(0, 0);
        cout << "\n";
    }
    return 0;
}