/**
 * File Name: Rekindle3.c
 * Author: Ahisu Fortune
 * Date: 26th March, 2025
 * Description: A dictionary of all my 'C' knowledge
 * Input Status: Required compulsorily
 */

#include <stdio.h>
#include <stdlib.h>

int main(){
    char nameFirst[40];
    char nameLast[40];
    int age;
    char course[40];
    int jambScore;

    printf("Enter your full name: ");
    scanf("%s%s", nameFirst, nameLast);
    printf("Hello %s, Input more about yourself to move on.\n", nameLast);
    printf("How old are you?: ");
    scanf("%d", &age);
    printf("Input your course: ");
    scanf("%s", course);
    printf("Input your JAMB score: ");
    scanf("%d", &jambScore);
    printf("%s, you are %d and are trying to study %s with %d JAMB score", nameLast, age, course, jambScore);
}
