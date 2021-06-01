#include <bits/stdc++.h>

using namespace std;

int main()
{
    // enter distance in kms
    double distance_km;
    cin >> distance_km;
    double distance_meters = distance_km * 1000;
    double distance_inches = distance_km * 39370.07874016;
    double distance_feet = distance_km * 3280.839895;
    double distance_cm = distance_meters * 100;

    cout << "Distance in km: " << distance_km << endl;
    cout << "Distance in meters: " << distance_meters << endl;
    cout << "Distance in inches: " << setprecision(6) << distance_inches << endl;
    cout << "Distance in feet: " << setprecision(6) << distance_feet << endl;
    cout << "Distance in cm: " << setprecision(6) << distance_cm << endl;
    return 0;
}