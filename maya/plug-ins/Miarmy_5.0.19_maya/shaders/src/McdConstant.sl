/******************************************************************************/
/*                                                                            */
/*    Copyright (c)The Basefount Team.                                         */
/*    All Rights Reserved.                                                    */
/*                                                                            */
/******************************************************************************/

surface McdConstant(
	color		diffusecolor = 1;
	string	mapname = "")
{
	Oi = Os;
	if( mapname == "" )
		Ci = Cs;
	else
		Ci = color texture( mapname );

	Ci *= Oi * diffusecolor;
}
