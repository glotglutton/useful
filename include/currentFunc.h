/*
 * Macros to return the name of the current function being executed.
 */

#include <iostream>

#if __STDC_VERSION__ < 199901L
#if __GNUC__ >= 2
#define __func__ __FUNCTION__
#else
#define __func__ "<unknown>"
#endif
#endif

#define __currentfunc__ __func__
#define FUNC_PREFIX __func__
