/* Personal class for easier software development and debugging
 * by Javier O. Cordero Pérez
 * Shared under the MIT License */

#ifndef JAVISTD_H
#define JAVISTD_H
#include <iostream>
#include <limits>

using namespace std;

class javistd
{   public:
        explicit javistd(string, string, string);
        ~javistd();
        void showHeader();
        void pause();
        void pause ( string /*message*/ );
        bool repeatProcess();
        bool repeatProcess( string /*message*/ );

    private:
       string Software, Ver, Message;
};

#endif // JAVISTD_H
