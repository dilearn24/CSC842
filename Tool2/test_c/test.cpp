#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_BUF 128

// Single‐line comment: unsafe I/O functions below
/*
  Block comment:
  fscanf(fp, "%s", buf); // should not be flagged here
  strcat(dest, src);     // should not be flagged here
*/

int main(int argc, char **argv) {
    char buf1[64];
    char buf2[64];
    FILE *fp = fopen("input.txt", "r");

    // vulnerable: gets()
    gets(buf1);

    // vulnerable: strcpy()
    strcpy(buf2, buf1);

    // vulnerable: strcat()
    strcat(buf2, "_suffix");

    // vulnerable: sprintf()
    sprintf(buf1, "Hello %s", buf2);

    // vulnerable: vsprintf()
    va_list args;
    va_start(args, argv);
    vsprintf(buf1, "Arg0=%s", args);
    va_end(args);

    // vulnerable: scanf without width
    scanf("%s", buf1);

    // vulnerable: fscanf without width
    fscanf(fp, "%s", buf2);

    // safe alternative for reference (should not be flagged):
    fgets(buf1, MAX_BUF, stdin);

    // vulnerable: system()
    system("rm -rf /tmp/testdir");

    // vulnerable: popen()
    FILE *pp = popen("ls -la", "r");
    pclose(pp);

    fclose(fp);
    return 0;
}
