#include <bits/stdc++.h>

using namespace std;

int main()
{
    int lines;
    cin >> lines;
    for (int i = 1; i <= lines; i++)
    {
        for (int space = 1; space <= lines - i; space++)
        {
            cout << " ";
        }

        int k = 0;

        while (k != i)
        {
            cout << "* ";
            ++k;
        }
        cout << endl;
    }
    return 0;
}