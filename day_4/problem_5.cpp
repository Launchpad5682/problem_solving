#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    //cout << n / 2 << endl;
    for (int i = 0; i < n; i++)
    {
        if (i == 0)
        {
            for (int j = 0; j < n; j++)
            {
                if (j == 0)
                    cout << "* ";

                else if (j >= n / 2)
                    cout << "* ";

                else
                    cout << "  ";
            }
            cout << endl;
        }
        if (i == (n - 1))
        {
            for (int j = 0; j < n; j++)
            {
                if (j == (n - 1))
                    cout << "* ";

                else if (j <= n / 2)
                    cout << "* ";

                else
                    cout << "  ";
            }
            cout << endl;
        }
        if (i == n / 2)
        {
            for (int j = 0; j < n; j++)
                cout << "* ";
            cout << endl;
        }
        if (i < n / 2 && i > 0)
        {
            for (int j = 0; j < n; j++)
            {
                if (j == 0)
                    cout << "* ";

                else if (j == (n / 2))
                    cout << "* ";

                else
                    cout << "  ";
            }
            cout << endl;
        }
        if (i > n / 2 && i < (n - 1))
        {
            for (int j = 0; j < n; j++)
            {
                if (j == (n - 1))
                    cout << "* ";

                else if (j == n / 2)
                    cout << "* ";

                else
                    cout << "  ";
            }
            cout << endl;
        }
    }
    return 0;
}