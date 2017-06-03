#ifndef shaveEngine_h
#define shaveEngine_h
//
// Shave and a Haircut
// Copyright Joe Alter, Inc., 2000-2005, all rights reserved.
// US Patent #6,720,962
//
#ifdef __cplusplus
extern          "C"
{
#endif

#include "shaveSDKTYPES.h"

//
// Do the Windows DLL dance...
//
#if defined(WIN32) && !defined(STANDALONESDK_STATIC)
#  ifdef STANDALONESDK_EXPORTS
#    define STANDALONESDK_API __declspec(dllexport)
#  else
#    define STANDALONESDK_API __declspec(dllimport)
#  endif
#else
#  define STANDALONESDK_API
#endif


// Get a Shave render license and initialize the PRIM library.
// You must call this function before making any other PRIM calls.
	STANDALONESDK_API int PRIMlogin( void );


// Release the Shave render license and any other resources held by the
// PRIM library.
	STANDALONESDK_API int PRIMlogout( void );


// Enables dumping of diagnostic information to the specified file.
	STANDALONESDK_API void PRIMDiagnosticON( char *filename );


// Load a Shave archive file into the PRIM library.  If there is already
// an archive file loaded it will be unloaded first.
// Returns the number of voxels in the file.
	STANDALONESDK_API int PRIMinit_hairstack( char *fname );


// Get the lower and upper limits of the specified voxel's bounding box.
// Returns -1 on failure (e.g. if the voxel does not exist).
	STANDALONESDK_API int PRIMfetch_bbox( int index, VERT * obound1, VERT * obound2 );


// Get all of the hairs in the specified voxel.
	STANDALONESDK_API void PRIMfetch_voxel( int index, HAIRTYPE * outhair, int isShadow );


// Retrieve all of the hairs and UV information from shaveNode 'nodename'
// which are rooted in in the voxel specified by 'index'.
//
// 'nodename' is implementation-dependent.  For archive files generated
// from Maya, 'nodename' is the name of the corresponding shaveNode in the
// scene.
//
// 'uvs' may be NULL if you don't care about UV information, but you must
// supply a valid pointer for 'outhair'.
	STANDALONESDK_API void PRIMfetch_voxel_by_name2( int index, char *nodename, HAIRTYPE * outhair, UVSETS * uvs, int isShadow );


// This function is deprecated.  Use PRIMfetch_voxel_by_name2 instead.
	STANDALONESDK_API void PRIMfetch_voxel_by_name( int index, char *nodename, HAIRTYPE * outhair, int isShadow );


// Free up the memory held by a HAIRTYPE which has been returned by any of
// the PRIMfetch_voxel* functions.  Note that this does not free the
// HAIRTYPE itself, just the memory allocated to its member variables.
	STANDALONESDK_API void PRIMfree_hairtype( HAIRTYPE * geom );


// Free up the memory held by a UVSETS which has been returned by any of
// the PRIMfetch_voxel* functions.  Note that this does not free the
// UVSETS itself, just the memory allocated to its member variables.
	STANDALONESDK_API void PRIMfree_uvset( UVSETS * uv );


// Unload the current archive file and free up any associated resources.
	STANDALONESDK_API void PRIMclear_hairstack( void );

#ifdef __cplusplus
}
#endif
#endif
