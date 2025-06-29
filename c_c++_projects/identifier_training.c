#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main()
{
/*
                        Identifiers
              Basic format specifiers include:
/-----------------------------------------------------------\
|     Type      |    Size(bytes)        | Format specifier  |
|---------------|-----------------------|-------------------|
|     int       | at least 2,usually 4  |       %d          |
|---------------|-----------------------|-------------------|
|     char      |           1           |       %c          |
|---------------|-----------------------|-------------------|
|     float     |           4           |       %f          |
|---------------|-----------------------|-------------------|
|     double    |           8           |       %lf         |
|---------------|-----------------------|-------------------|
|   short int   |        2 usually      |       %hd         |
|---------------|-----------------------|-------------------|
| unsigned int  | at least 2, usually 4 |       %u          |
|---------------|-----------------------|-------------------|
|   long int    | at least 4, usually 8 |       %li         |
|---------------|-----------------------|-------------------|
| long long int |       at least 8      |       %lli        |
|---------------|-----------------------|-------------------|
|unsigned long  |       at least 4      |       %lu         |
|     int       |                       |                   |
|---------------|-----------------------|-------------------|
| unsigned long |       at least 8      |       %llu        |
|   long int    |                       |                   |
|---------------|-----------------------|-------------------|
|   signed char |           1           |       %c          |
|---------------|-----------------------|-------------------|
| unsigned char |           1           |       %c          |
|---------------|-----------------------|-------------------|
|  long double  |     at least 10,      |       %c          |
|               |   usually 12 or 16    |                   |
|---------------|-----------------------|-------------------|
*/
    int age = scanf("%d", &age);
    double speed = 2.98E8;
    char grade = 'A';
    char phrase[] = "Fortune's C code";
/*
________Math functions________
__Basic math functions include: 
    ceil()
    floor()
    pow()
    sqrt()
*/
    float num0 = 25.1;
    int num1 = ceil(num0);
    printf("num1");
    return 0;
}
