//
// Shave and a Haircut
// Copyright Joe Alter, Inc., 2003, all rights reserved.
// US Patent #6,720,962
//
#include <maya/MFnPlugin.h>
#include <maya/MFStream.h>
#include <maya/MGlobal.h>
#include <maya/MIOStream.h>
#include <maya/MPxCommand.h>
#include <maya/MString.h>
#include <maya/MSyntax.h>
#include <maya/MTypes.h>

#include <maya/shaveAPI.h>
#include <maya/shaveItHair.h>


class shaveAPITestCmd : public MPxCommand
{
public:
    static MSyntax createSyntax();

                 shaveAPITestCmd();
    virtual      ~shaveAPITestCmd();

    void         displayGeomInfo(MString name, shaveAPI::SceneGeom& geom) const;

    void         displayHairInfo(
                     shaveAPI::HairInfo* hairInfo, bool instances
                 ) const;

    MStatus      doIt(const MArgList&);
    bool         isUndoable() const;

    static void* creator();

private:
};


void* shaveAPITestCmd::creator()
{
    return new shaveAPITestCmd();
}


shaveAPITestCmd::shaveAPITestCmd()
{
}


shaveAPITestCmd::~shaveAPITestCmd()
{
}


bool shaveAPITestCmd::isUndoable() const
{
    return false;
}


MStatus shaveAPITestCmd::doIt(const MArgList& argList)
{
    MStatus  status;
    char     msg[200];

    MGlobal::displayInfo("Test 1: export all shaveHairShapes...");

    shaveAPI::HairInfo hairInfo;

    status = shaveAPI::exportAllHair(&hairInfo);

    if (status == MS::kNotFound)
    {
        MGlobal::displayInfo(
            "  exportAllHair says there are no shaveHairShapes in the scene."
        );
    }
    else if (!status)
    {
        MGlobal::displayError(
            MString("  we got back the following unexpected error: ")
            + status.errorString()
        );
    }
    else
    {
        MGlobal::displayInfo("  Scene contains...");
        displayHairInfo(&hairInfo, false);
    }


    MGlobal::displayInfo("Test 2: export renderable shaveHairShapes...");

    status = shaveAPI::exportAllHair(&hairInfo, true);

    if (status == MS::kNotFound)
    {
        MGlobal::displayInfo(
            "  exportAllHair says there are no renderable shaveHairShapes"
			" in the scene."
        );

        status = MS::kSuccess;
    }
    else
    {
        MGlobal::displayInfo("  Renderable shaveHairShapes contain...");
        displayHairInfo(&hairInfo, false);
    }


    MGlobal::displayInfo("Test 3: iterate through non-instanced hairs...");

    status = shaveItHair::init(false, true);

    if (status == MS::kNotFound)
    {
        MGlobal::displayInfo(
            "  shaveItHair::init says there are no renderable, non-instanced"
            " shaveHairShapes in the scene."
        );
    }
    else
    {
        int  hairNum = 0;

        while (shaveItHair::nextHair(&hairInfo))
        {
	    sprintf(msg, "  Hair %d contains...", hairNum);
            MGlobal::displayInfo(msg);
            displayHairInfo(&hairInfo, false);

            if (++hairNum >= 3) break;
        }
    }


    MGlobal::displayInfo("Test 4: iterate through instanced hairs...");

    status = shaveItHair::init(true, true);

    if (status == MS::kNotFound)
    {
        MGlobal::displayInfo(
            "  shaveItHair::init says there are no renderable, instanced"
            " shaveHairShapes in the scene."
        );
    }
    else
    {
        int  hairNum = 0;

        while (shaveItHair::nextHair(&hairInfo))
        {
	    sprintf(msg, "  Hair %d contains...", hairNum);
            MGlobal::displayInfo(msg);
            displayHairInfo(&hairInfo, true);

            if (++hairNum >= 3) break;
        }
    }


    MGlobal::displayInfo("Test 5: get occlusion geometry...");

    shaveAPI::SceneGeom   hairOcclusions;
    shaveAPI::SceneGeom   shadowOcclusions;

    status = shaveAPI::exportOcclusions(&hairOcclusions, &shadowOcclusions);

    if ((status != MS::kSuccess) && (status != MS::kUnknownParameter))
    {
        MGlobal::displayError(
            MString("  we got back the following unexpected error: ")
            + status.errorString()
        );
    }
    else
    {
        if (status == MS::kUnknownParameter)
        {
            MGlobal::displayWarning(
                "  motion blur is on but no renderable camera could be found,"
                " so geometry velocities will all be zero."
            );
        }

        displayGeomInfo("Hair occlusions", hairOcclusions);
        displayGeomInfo("Shadow occlusions", shadowOcclusions);
    }

    //
    // Free up all the memory allocated to 'hairInfo'.
    //
    // This call is provided just as an example.  In this particular case
    // it is unnecessary because 'hairInfo' will go out of scope at the end
    // of the function and be destroyed, along with all of its storage.
    //
    // However, if you were planning on doing some other processing in this
    // function, then it might make sense to clear 'hairInfo's storage
    // first so that that memory was available for other uses.
    //
    hairInfo.clear();

    return MS::kSuccess;
}


MSyntax shaveAPITestCmd::createSyntax()
{
    MSyntax   syntax;

    syntax.enableQuery(false);
    syntax.enableEdit(false);

    return syntax;
}


void shaveAPITestCmd::displayGeomInfo(
        MString name, shaveAPI::SceneGeom& geom
) const
{
    MGlobal::displayInfo(MString("  ") + name + " consists of...");

    char msg[200];

    sprintf(
	msg,
	"  %d faces\n  %d vertices\n  %d face vertices",
    	geom.numFaces,
    	geom.numVertices,
    	geom.numFaceVertices
    );

    MGlobal::displayInfo(msg);

    //
    // Dump out some details for the first three faces, if there are that
    // many.
    //
    int face;
    int i;

    for (face = 0; (face < 3) && (face < geom.numFaces); face++)
    {
	sprintf(msg, "  face %d", face);
        MGlobal::displayInfo(msg);

        for (i = geom.faceStartIndices[face];
             i < geom.faceEndIndices[face];
             i++)
        {
            int vert = geom.faceVertices[i];

	    sprintf(
		buff,
		"    vertex %d: position (%f, %f, %f)  velocity (%f, %f, %f)",
	    	i-geom.faceStartIndices[face],
            	geom.vertices[vert].x,
            	geom.vertices[vert].y,
            	geom.vertices[vert].z,
            	geom.velocities[vert].x,
            	geom.velocities[vert].y,
            	geom.velocities[vert].z
	    );

            MGlobal::displayInfo(buff);
        }
    }
}


void shaveAPITestCmd::displayHairInfo(
        shaveAPI::HairInfo* hairInfo, bool instances
) const
{
    MString  strandName = (instances ? "face" : "strand");
    char     buff[200];

    sprintf(buff, "  %d %ss", hairInfo->numHairs, strandName);
    MGlobal::displayInfo(buff);

    sprintf(buff, "  %d vertices", hairInfo->numVertices);
    MGlobal::displayInfo(buff);

    sprintf(buff, "  %d %s vertices", hairInfo->numHairVertices, strandName);
    MGlobal::displayInfo(buff);

    //
    // Dump out some details for the first three strands, if there are that
    // many.
    //
    int strand;
    int i;

    for (strand = 0; (strand < 3) && (strand < hairInfo->numHairs); strand++)
    {
	sprintf(
	    buff,
	    "  %s %d: root colour (%f, %f, %f)  tip colour (%f, %f, %f)"
		"  surface normal (%f, %f, %f)",
            strandName,
	    strand,
            hairInfo->rootColors[strand].r,
            hairInfo->rootColors[strand].g,
            hairInfo->rootColors[strand].b,
            hairInfo->tipColors[strand].r,
            hairInfo->tipColors[strand].g,
            hairInfo->tipColors[strand].b,
            hairInfo->surfaceNormals[strand].x,
            hairInfo->surfaceNormals[strand].y,
            hairInfo->surfaceNormals[strand].z
        );
	MGlobal::displayInfo(buff);

        for (i = hairInfo->hairStartIndices[strand];
             i < hairInfo->hairEndIndices[strand];
             i++)
        {
            int vert = hairInfo->hairVertices[i];

	    sprintf(
		buff,
		"    vertex %d: position (%f, %f, %f)  velocity (%f, %f, %f)"
		    "  texture coords (%f, %f, %f)",
                (i-hairInfo->hairStartIndices[strand]),
                hairInfo->vertices[vert].x,
                hairInfo->vertices[vert].y,
                hairInfo->vertices[vert].z,
                hairInfo->velocities[vert].x,
                hairInfo->velocities[vert].y,
                hairInfo->velocities[vert].z,
                hairInfo->uvws[vert].x,
                hairInfo->uvws[vert].y,
                hairInfo->uvws[vert].z
            );
        }
    }
}


MStatus initializePlugin(MObject obj)
{ 
    MStatus   status;
    MFnPlugin plugin(obj, "Joe Alter, Inc.", "1.0", "Any");

    status = plugin.registerCommand(
                "shaveAPITest",
                shaveAPITestCmd::creator,
                shaveAPITestCmd::createSyntax
            );

    if (!status) 
    {
        status.perror("registering shaveAPITest command");
        return status;
    }

    return status;
}


MStatus uninitializePlugin(MObject obj)
{
    MStatus   status;
    MFnPlugin plugin(obj);

    status = plugin.deregisterCommand("shaveAPITest");

    if (!status)
    {
        status.perror("deregistering shaveAPITest command");
        return status;
    }

    return status;
}
