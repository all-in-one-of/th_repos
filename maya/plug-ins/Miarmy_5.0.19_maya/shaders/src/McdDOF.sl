/***************************************************/
/*  Miarmy                                         */
/*                                                 */
/*  Name: McdDOF                                   */
/*  Type: RM Shader                                */
/*  Summary:                                       */
/*    Easy and fast dof shader based on camera     */ 
/*  near/far clipping plane                        */
/*                                                 */
/*                           Basefount Technology  */
/*                                                 */
/***************************************************/

surface
McdDOF(float focus = 0;
       float outoffocus = 2000;)
{
  float d = 1;
  float LI = length(I);

  d = 1 - LI / (outoffocus - focus);
  
 
  Ci = d;
  Oi = 1;
}