#include <bits/stdc++.h>

using namespace std;

int main()
{
    // enter distance in kms
    double distance_km;
    cin >> distance_km;
    double distance_meters = distance_km * 1000;
    double distance_feet = distance_km * 3280.839895;
    double distance_cm = distance_meters * 100;

    cout << "Distance in km: " << distance_km << endl;
    cout << "Distance in meters: " << distance_meters << endl;
    cout << "Distance in feet: " << distance_feet << endl;
    cout << "Distance in cm: " << distance_cm << endl;
    return 0;
}