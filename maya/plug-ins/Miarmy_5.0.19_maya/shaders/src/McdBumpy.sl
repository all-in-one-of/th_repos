/***************************************************/
/*  Miarmy                                         */
/*                                                 */
/*  Name: McdBumpy                                 */
/*  Type: RM Shader                                */
/*  Summary:                                       */
/*    Displacement shader can be assign to polygon */
/*  mesh. (not just subd)                          */
/*                                                 */
/*                           Basefount Technology  */
/*                                                 */
/***************************************************/


displacement
McdBumpy(
	float Km = 1, amplitude = 1;
	string texturename = ""; )
{
	normal Ndiff;
	if( texturename != "" )
	{
		float amp = Km * amplitude * float texture( texturename, s, t );
		
		Ndiff = normalize(N) - normalize(Ng);
		P += amp * normalize( N );
		N = normalize(calculatenormal( P )) + Ndiff;
	}
}
