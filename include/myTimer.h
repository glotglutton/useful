#include <iostream>
#include <sys/time.h>

class myTimer{

    private:
        struct  timeval start;
        struct  timeval stop;
        double  msec;

    public:
        myTimer(){msec = 0.0f;}

        void tic(){
            gettimeofday(&start, NULL);
        }

        void toc(){
            gettimeofday(&stop, NULL);
            addElapsedTime();
        }

        void addElapsedTime(){
            msec += ((double)stop.tv_sec * 1.e3 + (double)stop.tv_usec * 1.e-3)
                    - ((double)start.tv_sec * 1.e3 + (double)start.tv_usec * 1.e-3);
        }

        double getElapsedTime(){return msec;}

};
