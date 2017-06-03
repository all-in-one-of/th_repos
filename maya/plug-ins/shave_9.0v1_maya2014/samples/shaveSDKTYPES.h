// Shave and a Haircut SDK (c)1999-2004 Joseph Alter, inc
//
// Shave and a Haircut SDK
// Copyright Joe Alter, Inc., 1999-2004, all rights reserved.
// US Patent #6,720,962
//
#ifndef shaveSDKTYPES_h
#define shaveSDKTYPES_h

#ifdef _WIN32
#include <windows.h>
#include <process.h>
#else
#include <pthread.h>
#endif

#ifdef __cplusplus
#ifndef USECPP
extern "C" 
{
#endif
#endif


//
// constants
//
#define	SHAVE_FAR_CLIP			1000000.0f
#define	SHAVE_NUM_PARAMS		60
#define	SHAVE_NUM_GROUPS		5
#define	SHAVE_MAX_LABEL_LEN		49
#define	SHAVE_VERTS_PER_GUIDE	15

#define MAX_XSI_SHAVEINSTANCES	4

typedef enum
{
	kBrushTranslate,
	kBrushScale,
	kBrushRotate,
	kBrushStand,
	kBrushPuff,
	kBrushClump
} BRUSH_MODE;


typedef enum
{
	kShaveHostMR = 0,
	kShaveHostPRMAN = 1,
	kShaveHostBuffer = 2
} SHAVE_RENDER_HOST;


//**********************************************************************
//
//      STANDALONE ("PRIM") API TYPES
//
// The following types are used by the standalone ("PRIM") API
// functions.
//
//**********************************************************************

// stucture for a vertex
typedef struct
{
	float           x, y, z;
} VERT;


typedef struct
{
	//
	// For normal hair, this structure contains a set of hairs.  Each hair
	// has a sequence of vertices which run up the middle of it.
	//
	// For instanced hair, this structure contains a set of faces
	// representing the instanced geometry.  Each face has three or more
	// vertices which define its perimeter.  Vertices may be shared between
	// adjoining faces.
	//

	//
	// Total number of vertices returned in the 'v' member below.  If a
	// vertex is shared between multiple faces then it only counts once in
	// this total.
	//
	int             totalverts;

	//
	// For regular hair, 'totalfaces' contains the total number of hairs.
	// Note that a separate hair is generated for each "pass", so if your
	// shaveNode has passes set to 3 and 5,000 hairs, then totalfaces may
	// be as high as 15,000.
	//
	// For instanced hair, 'totalfaces' contains the total number of
	// polygonal faces in the instanced geometry.
	//
	int             totalfaces;

	//
	// For normal hair, this is the total number of vertices in all of the
	// hairs, combined.
	//
	// For instanced hair, it is the total number of face-vertices.  If a
	// vertex is shared between faces then it counts once for each face in
	// this total.
	//
	int             totalfverts;

	//
	// Table to translate face-vertex indices into vertex indices, suitable
	// for indexing into 'v'.
	//
	int            *facelist;

	//
	// Array giving the starting position within 'facelist' for each
	// hair/face's vertices.  The array contains one element per hair/face.
	//
	int            *face_start;

	//
	// Array giving the ending position within 'facelist' for each
	// hair/face's vertices.  The array contains one element per hair/face.
	//
	// Note that the index give is one *beyond* the index of the
	// hair/face's last vertex in 'facelist'.  This means that the
	// following will give you the number of vertices in the hair/face:
	//
	//      face_end[N] - face_start[N]
	//
	int            *face_end;

	//
	// Opacity of each hair/face.
	//
	float          *opacity;

	//
	// Specularity for each hair/face.
	//
	float          *spec;

	//
	// Gloss for each hair/face.
	//
	float          *gloss;

	//
	// Gloss for each ambient/diffuse ratio for each hair/face.
	//
	float          *ambdiff;

	//
	// Root color for each hair (doesn't apply to faces).
	//
	VERT           *colorroot;

	//
	// Tip color for each hair (doesn't apply to faces).
	//
	VERT           *colortip;

	//
	// Radius of each hair at its root (doesn't apply to faces).
	//
	float          *radiusroot;

	//
	// Radius of each hair at its tip (doesn't apply to faces).
	//
	float          *radiustip;

	//
	// Vertices.
	//
	// This is an array containing the worldspace positions for 'totalfaces'
	// vertices.
	//
	// You access the vertices for a particular hair or face as follows:
	//
	//  int firstVert = hairType.face_start[faceOrHairNumber];
	//  int lastVert = hairType.face_end[faceOrHairNumber] - 1;
	//
	//  for (i = firstVert; i <= lastVert; i++)
	//  {
	//      int  vertIndex = hairType.facelist[i];
	//      VERT vertPosition = hairType.v[vertIndex];
	//      ...
	//  }
	//
	// Be sure to note the '- 1' at the end of the initialization of
	// 'lastVert'.  That's because the 'face_end' array actually points to
	// the first vertex *beyond* the end of the given hair/face.
	//
	VERT           *v;

	//
	// Velocity per vertex.  Accessed in the same way as 'v'.
	//
	VERT           *velocity;

	//
	// Texture parameters per vertex.  Accessed in the same way as 'v'.
	//
	// For normal hairs, u and v represent the texture parameters of the
	// point on the surface from which they are growing.  'w' is a
	// parameter which runs from 0.0 at the root to 1.0 at the tip.
	//
	// For instanced hair, u and v represent the texture coords at each
	// vertex and 'w' is unused.
	//
	VERT           *uvw;

	//
	// Not currently used.
	//
	VERT           *uvw2;

	//
	// Surface normal per-hair.  This gives the surface normal for the
	// growth surface at the point where the hair is rooted.
	//
	// Not used for instanced hair.
	//
	VERT *surfNorm; // per hair (or per hair clump) - added this on April 16, 2004
	int *index; // per strand - added this on july 3, 2009
	float *alpha; // per strand - added this on july 3, 2009
//	VERT *spec_tint; // 6.5
//	VERT *spec_tint2; // 6.5
} HAIRTYPE;


typedef struct
{
	//  Number of UV sets per hair root.
	char            totalUVSets;

	//  Number of hair roots for which UV set information is given.
	int             totalRoots;

	//  For internal use only.
	char           *channelRef;

	//  The UVZ values for the hair roots.  There will be 'totalUVSets'
	//  elements for each hair root.  So 'totalUVSets' elements for root 0,
	//  followed by 'totalUVSets' elements for root 1, etc.
	VERT           *uvRoot;
} UVSETS;


//**********************************************************************
//
//      INTERNAL STRUCTURES
//
// The remaining structures are internal to Shave and have no meaning
// within the standalone API.
//
//**********************************************************************


// simple data type for holding geometry
typedef struct
{
	int             totalverts;
	int             totalfaces;
	int             totalfverts;
	int            *facelist;	// list of face verts
	int            *face_start;	// face refferenced index into facelist
	int            *face_end;	// face refferenced index into facelist
	VERT           *color;		// vert refferenced color 
	VERT           *v;			// vert refferenced vertex position
	VERT           *velocity;	// vertex velocity
	VERT           *uv;			// vert refferenced uv info (x,y)
	VERT           *vn;			// vert normals
	float          *alpha;		// 3.9
	int				*id;		// using this to store the hair or poly ID - facewise
	float		   *r1,*r2; // face refferenced index into radius root and tip 
	int				*index; // this is the index which includes passes and clones
// coming soon for subdivs
//  int *pid; // facevert refferenced, same size as *facelist
//  VERT *bary; // facevert refferenced, same size as *facelist
// pid reffers to the original face (after triangulaiton)
// bary reffers to vert weights on that original triangle
} WFTYPE;


typedef struct
{
	WFTYPE          mesh;
	VERT           *baryweights;	// 1 per facevert
	int            *baryface;	// 1 per face
} SUBDIVTYPE;


typedef struct
{
	VERT            guide[SHAVE_VERTS_PER_GUIDE];
	VERT            velocity[SHAVE_VERTS_PER_GUIDE];
	int             select[SHAVE_VERTS_PER_GUIDE];
	int             lock[SHAVE_VERTS_PER_GUIDE];
	float           weight[SHAVE_VERTS_PER_GUIDE];	// new for 4.0
	float           cut_value;	// new for 4.0
	int             splitgroup;
	int             merge;
	int             vid;
	VERT            norm;
	int             zerosize;
	int             hidden;		// new for 4.0
} SOFTGUIDE;


// settings parameters for hair groups
// [0]=hair
// [1]=beard
// [2]=eyebrows
// [3]=eyelashes
// [4]=splines

// this type contains general shave engine info

typedef struct
{
	int             haircount[SHAVE_NUM_GROUPS+1];	// # of hairs to be generated for each group
	int             passes[SHAVE_NUM_GROUPS+1];	// number of passes to generated
	float           slider_val[SHAVE_NUM_PARAMS][SHAVE_NUM_GROUPS + 1];	// slider settings
	char            slider_lable[SHAVE_NUM_PARAMS][SHAVE_NUM_GROUPS + 1][SHAVE_MAX_LABEL_LEN + 1];	// slider labels
	int             painted[SHAVE_NUM_PARAMS][SHAVE_NUM_GROUPS + 1];	// 1=has weight painting 0= no weight painting
	int             total_guides;	// total # guide hairs
	int             instancing_status;
	int             collide[SHAVE_NUM_GROUPS + 1];	// collision on/off
	int             collision_method;	// 0 = spheres  1 = surfaces
	VERT            frizz_anim_dir[SHAVE_NUM_GROUPS + 1];	// 0 = x  1 = y  2 = z
	int             segs[SHAVE_NUM_GROUPS + 1];
	int             dontinterpolate;
	float           geom_shadow;
	int             shadowHaircount[5];	// 2.7v51
	int             uv_link[60];	// 2.7v53
	char            name[64];
	int             tipfade;
	float           multrot;	// 4.0 - this is for twist on mult hairs
	VERT            spec_tint;	// 4.0 - this is for rendering
	float           springyness;	// 4.0 - this is for dyn
	float           multrot_phase;	// 4.0
	float           multrot_offset;	// 4.0
	int             squirrel; // 5.5
	float			flyaway_percent; // 6.0
//	int				use_old_splayscale;
	int clumps;
	int rand_seed_offset;
	VERT            spec_tint2;	// 6.0.39 - this is for rendering
} SHAVEPARMS;


// opaque multi-use data type
typedef struct
{
	long            size;
	long            pos;
	char           *data;
	int            ID;
	int             time;
} MEMFILE;

typedef struct
{
	MEMFILE         restMEM;
	MEMFILE         statMEM;
	SHAVEPARMS      shavep;
} SHAVENODE;


typedef float   Matrix[4][4];

typedef struct
{
	int             Tpid;		// face ID (after triangulation)
	int             UTpid;		// faceID (with no triangulation)
	int             pntid[3];	// point IDs
	float           wgt[3];		// point weights
	float           baserad;	// the base radius
	float           tiprad;		// the tip radius
	Matrix          rest2zero[SHAVE_VERTS_PER_GUIDE];	// matricies for points on the guides
	Matrix          zero2world[SHAVE_VERTS_PER_GUIDE];
	float           u, v;		// interpolated uv coords
	VERT            norm;		// interpolated surface normal
	float           diff, spec, kspec, shad;	// some render params
	int             killme;		// some times empty hairs will get returned (for point count consistancy)
	// because they've been 'killed' by densemaps, cutmaps, etc - this will let
	// you know: killme=1 
	float           ambient;
	int             mtl;
	float           restlength;
	float           cutlength;
	int             hairID;
	int             groupID;
	unsigned long   nodeID;
	int             depthpass;
	float           u2, v2;		// 2.6v22
	int             shadowHair;	// 2.7v51
	VERT            UV[60];		// 2.7v53
	unsigned long	shaveID; // 6.0
	VERT spec_tint;
	VERT spec_tint2;
} CURVEINFO;

// this stucture gets returned from make_a_curve, and make_a_curveROOT and contains
// all kinds of non vertex info.


//
// Return codes for abcAWLOGIN.
//
#define	NOKEY			0
#define	OLDKEY_SUCCESS	1
#define	NEWKEY_SUCCESS	2
#define	HASPKEY_SUCCESS	3


typedef struct
{
	VERT            color;
	VERT            velocity;
	float           distance;
	float           opacity;
} VOXSAMP;



//
// Type for functions passed to SHAVEstart_thread().
//
// Note that 'threadID' is a Shave-specific ID ranging from 0 to one less
// than the number of threads in the thread group.  It bears no
// relationship to any operating system thread ID.
//
typedef void    ( *ThreadFunc ) ( unsigned threadID, void *data );

//
// Type for mutexes (mutual exclusions), used for locking.
//
#ifdef _WIN32
typedef HANDLE  ShaveMutex;
#else
typedef pthread_mutex_t ShaveMutex;
#endif

//
// Type for conditions, used with mutexes for locking.
//
#ifdef _WIN32
typedef HANDLE  ShaveCond;
#else
typedef pthread_cond_t ShaveCond;
#endif

#ifdef __cplusplus
#ifndef USECPP
}
#endif
#endif


#endif
