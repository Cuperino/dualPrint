/* Personal class for easier software development and debugging
 * by Javier O. Cordero Pérez
 * Shared under the MIT License*/

#ifndef JAVISTD_H
#include "javistd.h"
#endif // JAVISTD_H

//PUBLIC

javistd::javistd(string software, string ver, string message)
{   Software = software;
    Ver = ver;
    Message = message;
} // end ctor for javistd

javistd::~javistd()
{   //dtor
}

void javistd::showHeader()
{   cout << Software << " ver " << Ver << endl << Message << endl;
    return;
} // end showHeader

void javistd::pause() // Multiplatform CUI pause
{   cout << "\nPress <ENTER> to continue . . .";
    cin.ignore ( numeric_limits<streamsize>::max(), '\n' );
    cin.get();
    return;
} // end pause

void javistd::pause( string message ) // Multiplatform CUI pause
{   cout << endl << message;
    cin.ignore ( numeric_limits<streamsize>::max(), '\n' );
    cin.get();
    return;
} // end pause

bool javistd::repeatProcess( )
{   bool flag = false;
    char YN;
    // Re execute process?
    cout << "\nWish to repeat the process? [Y/n]: ";
    cin >> YN;
    YN = toupper(YN);
    while ( !(YN=='Y'||YN=='S'||YN=='N') )
    {
        cout << "\nPlease, enter a valid option... [Y/n]: ";
        cin >> YN;
        YN = toupper(YN);
    } // end while
    cin.ignore(); // Takes care of \n for when user presses enter.
    if (YN == 'Y' || YN == 'S' )
        flag = true;

    cout << endl;
    return flag;
}  // end repeatProcess

bool javistd::repeatProcess( string message )
{   bool flag = false;
    char YN;
    // Re execute process?
    do
    {
        cout << endl << message;
        cin >> YN;
        YN = toupper(YN);
    } while ( !(YN=='Y'||YN=='S'||YN=='N') );
    cin.ignore(); // Takes care of \n for when user presses enter.
    if (YN == 'Y' || YN == 'S' )
        flag = true;

    cout << endl;
    return flag;
}  // end repeatProcess

//PRIVATE
