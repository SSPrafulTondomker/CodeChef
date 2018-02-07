#include <stdio.h>
#include <string.h>
 
int main()
{
	   int number;
	      char unit[3];
	       
	         printf("Enter a number between 0-200 followed by its units: ");
		    do
			       {
				             scanf("%d%60s", &number, unit);
					           if (strlen(unit) > 2)
							         {
									           printf("Units are too long\n");
										         }
						         else if (number < 0 || number > 200)
								       {
									                 printf("Number too large\n");
											       }
							       else
								             {
										               printf("Entered number: %d\tEntered unit:%s\n", number, unit);
											             }
							          } while (number != EOF);
		     
		       return(0);
}
