#include <bits/stdc++.h>

using namespace std;

int main()
{
    double salary;
    cin >> salary;
    double dearness_allowance = 0.4 * salary;
    double house_rent_allowance = 0.2 * salary;
    double gross_salary = salary + dearness_allowance + house_rent_allowance;
    cout << setprecision(8) << gross_salary << endl;
    return 0;
}