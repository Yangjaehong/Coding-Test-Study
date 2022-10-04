#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{

    int count = 0;
    for (int i = 0; i < s.size(); i++){
        if (s[i] == 'P'|| s[i] == 'p' ) count += 1;
        
        else if (s[i] == 'y'|| s[i] == 'Y' ) count -= 1;
    }
    if (count == 0) return true;
    return false;
}