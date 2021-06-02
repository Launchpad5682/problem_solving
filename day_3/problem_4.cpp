#include <bits/stdc++.h>

using namespace std;

int main()
{
    int a, b, c;
    cin >> a >> b >> c;
    if (a >= b && a >= c)
    {
        if (b >= c)
        {
            cout << a << " " << b << " " << c << endl;
            cout << c << " " << b << " " << a << endl;
        }
        else
        {
            cout << a << " " << c << " " << b << endl;
            cout << b << " " << c << " " << a << endl;
        }
    }
    else if (b >= c && b >= a)
    {
        if (a >= c)
        {
            cout << b << " " << a << " " << c << endl;
            cout << c << " " << a << " " << b << endl;
        }
        else
        {
            cout << b << " " << c << " " << a << endl;
            cout << a << " " << c << " " << b << endl;
        }
    }
    else if (c >= a && c >= b)
    {
        if (a >= b)
        {
            cout << c << " " << a << " " << b << endl;
            cout << b << " " << a << " " << c << endl;
        }
        else
        {
            cout << c << " " << b << " " << a << endl;
            cout << a << " " << b << " " << c << endl;
        }
    }
    return 0;
}