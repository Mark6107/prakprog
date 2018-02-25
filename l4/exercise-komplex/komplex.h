#ifndef HAVE_KOMPLEX_H

struct komplex {double re; double im;};
typedef struct komplex komplex;

void	komplex_print	(char* s, komplex z);
void	komplex_set		(komplex* z, double x, double y);
komplex	komplex_new		(double x, double y);
komplex	komplex_add		(komplex a, komplex b);
komplex	komplex_sub		(komplex a, komplex b);

/* Insert optional */

int		komplex_equal	(komplex a, komplex b);
komplex	komplex_mul		(komplex a, komplex b);
komplex	komplex_div		(komplex a, komplex b);
komplex	komplex_conju	(komplex z);
komplex komplex_abs		(komplex z);
komplex komplex_exp		(komplex z);
komplex komplex_sin		(komplex z);
komplex komplex_cos		(komplex z);
komplex	komplex_sqrt	(komplex z);

#define HAVE_KOMPLEX_H
#endif
