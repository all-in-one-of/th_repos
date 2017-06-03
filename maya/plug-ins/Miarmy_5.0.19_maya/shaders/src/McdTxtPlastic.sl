surface McdTxtPlastic( 
	float	Ks		=  1, 
		Kd		=  1, 
		Ka		=  1,
		opacity 		=  1,
		roughness	= .1;
	color	diffusecolor 	= 1,
		specularcolor 	= 1;
	string	mapname 	= "",
		traname 		= "")
{
	normal	Nf = faceforward(normalize(N), I );

	if( mapname != "" )
		Ci = color texture( mapname );
	else
		Ci = Cs;

	if( traname != "" )
		Oi = float texture( traname );
	else
		Oi = Os * opacity;

	Ci = Oi * ( Ci * 
		(Ka * ambient() + Kd * diffusecolor * diffuse(Nf)) 
		+ specularcolor * Ks * specular(Nf, normalize( -I ), roughness) );
}
