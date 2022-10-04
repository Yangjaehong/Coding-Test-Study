#include <string>
#include <vector>
#include <iostream>

using namespace std;

bool solution(int x) {
    int answer = 0;
    int k = x;
    while (true){
        answer += x % 10;
        x = x / 10;
        if (x == 0){
            break;
        }
    }
    if (k % answer == 0) return true;
    return false;
}