#ifndef HAVE_NVECTOR_H

typedef struct {int size; double* data;} nvector;

nvector*	nvector_alloc		(int n);
void		nvector_free		(nvector* v);
void		nvector_set			(nvector* v, int i, double value);
double		nvector_get			(nvector* v, int i);
double		nvector_dot_product	(nvector* u, nvector* v);

// Optional
void	nvector_print		(char* s, nvector* v);
void	nvector_set_zero	(nvector* v);
int		nvector_equal		(nvector* a, nvector* b);
void	nvector_add			(nvector* a, nvector* b);
void	nvector_sub			(nvector* a, nvector* b);
void	nvector_scale		(nvector* a, double x);

#define HAVE_NVECTOR_H
#endif
