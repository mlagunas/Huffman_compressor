
#include <stdio.h>
#include <stdlib.h>


void writefile(char* data, char* out) {
  FILE* pFile = fopen( out, "wb" );
  char c = strtol(data, 0, 2);
  fwrite(c,1,sizeof(c),pFile);
  fclose(pFile);
}

int main( int argc, char *argv[] )  {

   if( argc == 3 ) {
      printf("The arguments supplied are [%s, %s]\n", argv[1], argv[2]);
      writefile(argv[1], argv[2]);
   }
   else if( argc > 3 ) {
      printf("Too many arguments supplied.\n");
   }
   else {
      printf("One argument expected.\n");
   }
}

1.576.566 7.903.248 1.975.811
if benchmark:
    start = time.time()
a = count.join(chr(int(output[i:i+8], 2)) for i in xrange(0, len(output), 8))
if benchmark:
    end = time.time()
    print "To ascii " + str(end-start)
