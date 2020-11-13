#pragma once

#include <vector>

#ifdef _WIN32
#if defined(_MSC_VER) && !defined(mainLib_STATIC)
#ifdef mainLib_EXPORTS
#define MAIN_API __declspec(dllexport)
#else
#define MAIN_API __declspec(dllimport)
#endif
#else
#define MAIN_API
#endif
#endif

namespace example
{
#ifdef _WIN32
	MAIN_API long _stdcall test();
#elif linux
	long test();
#endif
}