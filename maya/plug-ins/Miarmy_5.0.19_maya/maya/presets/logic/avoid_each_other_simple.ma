//Maya ASCII 2014 scene
//Name: avoid_each_other_simple.ma
//Last modified: Sun, Jun 26, 2016 05:25:27 PM
//Codeset: 936
requires maya "2014";
requires -nodeType "mentalrayFramebuffer" -nodeType "mentalrayOutputPass" -nodeType "mentalrayRenderPass"
		 -nodeType "mentalrayUserBuffer" -nodeType "mentalraySubdivApprox" -nodeType "mentalrayCurveApprox"
		 -nodeType "mentalraySurfaceApprox" -nodeType "mentalrayDisplaceApprox" -nodeType "mentalrayOptions"
		 -nodeType "mentalrayGlobals" -nodeType "mentalrayItemsList" -nodeType "mentalrayShader"
		 -nodeType "mentalrayUserData" -nodeType "mentalrayText" -nodeType "mentalrayTessellation"
		 -nodeType "mentalrayPhenomenon" -nodeType "mentalrayLightProfile" -nodeType "mentalrayVertexColors"
		 -nodeType "mentalrayIblShape" -nodeType "mapVizShape" -nodeType "mentalrayCCMeshProxy"
		 -nodeType "cylindricalLightLocator" -nodeType "discLightLocator" -nodeType "rectangularLightLocator"
		 -nodeType "sphericalLightLocator" -nodeType "abcimport" -nodeType "mia_physicalsun"
		 -nodeType "mia_physicalsky" -nodeType "mia_material" -nodeType "mia_material_x" -nodeType "mia_roundcorners"
		 -nodeType "mia_exposure_simple" -nodeType "mia_portal_light" -nodeType "mia_light_surface"
		 -nodeType "mia_exposure_photographic" -nodeType "mia_exposure_photographic_rev" -nodeType "mia_lens_bokeh"
		 -nodeType "mia_envblur" -nodeType "mia_ciesky" -nodeType "mia_photometric_light"
		 -nodeType "mib_texture_vector" -nodeType "mib_texture_remap" -nodeType "mib_texture_rotate"
		 -nodeType "mib_bump_basis" -nodeType "mib_bump_map" -nodeType "mib_passthrough_bump_map"
		 -nodeType "mib_bump_map2" -nodeType "mib_lookup_spherical" -nodeType "mib_lookup_cube1"
		 -nodeType "mib_lookup_cube6" -nodeType "mib_lookup_background" -nodeType "mib_lookup_cylindrical"
		 -nodeType "mib_texture_lookup" -nodeType "mib_texture_lookup2" -nodeType "mib_texture_filter_lookup"
		 -nodeType "mib_texture_checkerboard" -nodeType "mib_texture_polkadot" -nodeType "mib_texture_polkasphere"
		 -nodeType "mib_texture_turbulence" -nodeType "mib_texture_wave" -nodeType "mib_reflect"
		 -nodeType "mib_refract" -nodeType "mib_transparency" -nodeType "mib_continue" -nodeType "mib_opacity"
		 -nodeType "mib_twosided" -nodeType "mib_refraction_index" -nodeType "mib_dielectric"
		 -nodeType "mib_ray_marcher" -nodeType "mib_illum_lambert" -nodeType "mib_illum_phong"
		 -nodeType "mib_illum_ward" -nodeType "mib_illum_ward_deriv" -nodeType "mib_illum_blinn"
		 -nodeType "mib_illum_cooktorr" -nodeType "mib_illum_hair" -nodeType "mib_volume"
		 -nodeType "mib_color_alpha" -nodeType "mib_color_average" -nodeType "mib_color_intensity"
		 -nodeType "mib_color_interpolate" -nodeType "mib_color_mix" -nodeType "mib_color_spread"
		 -nodeType "mib_geo_cube" -nodeType "mib_geo_torus" -nodeType "mib_geo_sphere" -nodeType "mib_geo_cone"
		 -nodeType "mib_geo_cylinder" -nodeType "mib_geo_square" -nodeType "mib_geo_instance"
		 -nodeType "mib_geo_instance_mlist" -nodeType "mib_geo_add_uv_texsurf" -nodeType "mib_photon_basic"
		 -nodeType "mib_light_infinite" -nodeType "mib_light_point" -nodeType "mib_light_spot"
		 -nodeType "mib_light_photometric" -nodeType "mib_cie_d" -nodeType "mib_blackbody"
		 -nodeType "mib_shadow_transparency" -nodeType "mib_lens_stencil" -nodeType "mib_lens_clamp"
		 -nodeType "mib_lightmap_write" -nodeType "mib_lightmap_sample" -nodeType "mib_amb_occlusion"
		 -nodeType "mib_fast_occlusion" -nodeType "mib_map_get_scalar" -nodeType "mib_map_get_integer"
		 -nodeType "mib_map_get_vector" -nodeType "mib_map_get_color" -nodeType "mib_map_get_transform"
		 -nodeType "mib_map_get_scalar_array" -nodeType "mib_map_get_integer_array" -nodeType "mib_fg_occlusion"
		 -nodeType "mib_bent_normal_env" -nodeType "mib_glossy_reflection" -nodeType "mib_glossy_refraction"
		 -nodeType "mib_illum_hair_x" -nodeType "builtin_bsdf_architectural" -nodeType "builtin_bsdf_architectural_comp"
		 -nodeType "builtin_bsdf_carpaint" -nodeType "builtin_bsdf_ashikhmin" -nodeType "builtin_bsdf_lambert"
		 -nodeType "builtin_bsdf_mirror" -nodeType "builtin_bsdf_phong" -nodeType "contour_store_function"
		 -nodeType "contour_store_function_simple" -nodeType "contour_contrast_function_levels"
		 -nodeType "contour_contrast_function_simple" -nodeType "contour_shader_simple" -nodeType "contour_shader_silhouette"
		 -nodeType "contour_shader_maxcolor" -nodeType "contour_shader_curvature" -nodeType "contour_shader_factorcolor"
		 -nodeType "contour_shader_depthfade" -nodeType "contour_shader_framefade" -nodeType "contour_shader_layerthinner"
		 -nodeType "contour_shader_widthfromcolor" -nodeType "contour_shader_widthfromlightdir"
		 -nodeType "contour_shader_widthfromlight" -nodeType "contour_shader_combi" -nodeType "contour_only"
		 -nodeType "contour_composite" -nodeType "contour_ps" -nodeType "mi_metallic_paint"
		 -nodeType "mi_metallic_paint_x" -nodeType "mi_bump_flakes" -nodeType "mi_car_paint_phen"
		 -nodeType "mi_metallic_paint_output_mixer" -nodeType "mi_car_paint_phen_x" -nodeType "physical_lens_dof"
		 -nodeType "physical_light" -nodeType "dgs_material" -nodeType "dgs_material_photon"
		 -nodeType "dielectric_material" -nodeType "dielectric_material_photon" -nodeType "oversampling_lens"
		 -nodeType "path_material" -nodeType "parti_volume" -nodeType "parti_volume_photon"
		 -nodeType "transmat" -nodeType "transmat_photon" -nodeType "mip_rayswitch" -nodeType "mip_rayswitch_advanced"
		 -nodeType "mip_rayswitch_environment" -nodeType "mip_card_opacity" -nodeType "mip_motionblur"
		 -nodeType "mip_motion_vector" -nodeType "mip_matteshadow" -nodeType "mip_cameramap"
		 -nodeType "mip_mirrorball" -nodeType "mip_grayball" -nodeType "mip_gamma_gain" -nodeType "mip_render_subset"
		 -nodeType "mip_matteshadow_mtl" -nodeType "mip_binaryproxy" -nodeType "mip_rayswitch_stage"
		 -nodeType "mip_fgshooter" -nodeType "mib_ptex_lookup" -nodeType "misss_physical"
		 -nodeType "misss_physical_phen" -nodeType "misss_fast_shader" -nodeType "misss_fast_shader_x"
		 -nodeType "misss_fast_shader2" -nodeType "misss_fast_shader2_x" -nodeType "misss_skin_specular"
		 -nodeType "misss_lightmap_write" -nodeType "misss_lambert_gamma" -nodeType "misss_call_shader"
		 -nodeType "misss_set_normal" -nodeType "misss_fast_lmap_maya" -nodeType "misss_fast_simple_maya"
		 -nodeType "misss_fast_skin_maya" -nodeType "misss_fast_skin_phen" -nodeType "misss_fast_skin_phen_d"
		 -nodeType "misss_mia_skin2_phen" -nodeType "misss_mia_skin2_phen_d" -nodeType "misss_lightmap_phen"
		 -nodeType "misss_mia_skin2_surface_phen" -nodeType "surfaceSampler" -nodeType "mib_data_bool"
		 -nodeType "mib_data_int" -nodeType "mib_data_scalar" -nodeType "mib_data_vector"
		 -nodeType "mib_data_color" -nodeType "mib_data_string" -nodeType "mib_data_texture"
		 -nodeType "mib_data_shader" -nodeType "mib_data_bool_array" -nodeType "mib_data_int_array"
		 -nodeType "mib_data_scalar_array" -nodeType "mib_data_vector_array" -nodeType "mib_data_color_array"
		 -nodeType "mib_data_string_array" -nodeType "mib_data_texture_array" -nodeType "mib_data_shader_array"
		 -nodeType "mib_data_get_bool" -nodeType "mib_data_get_int" -nodeType "mib_data_get_scalar"
		 -nodeType "mib_data_get_vector" -nodeType "mib_data_get_color" -nodeType "mib_data_get_string"
		 -nodeType "mib_data_get_texture" -nodeType "mib_data_get_shader" -nodeType "mib_data_get_shader_bool"
		 -nodeType "mib_data_get_shader_int" -nodeType "mib_data_get_shader_scalar" -nodeType "mib_data_get_shader_vector"
		 -nodeType "mib_data_get_shader_color" -nodeType "user_ibl_env" -nodeType "user_ibl_rect"
		 -nodeType "xgen_geo" -nodeType "xgen_seexpr" -nodeType "xgen_scalar_to_integer" -nodeType "xgen_integer_to_vector"
		 -nodeType "xgen_scalar_to_vector" -nodeType "xgen_boolean_to_vector" -nodeType "xgen_boolean_switch"
		 -nodeType "xgen_tube_normals" -nodeType "xgen_hair_phen" -nodeType "mia_material_x_passes"
		 -nodeType "mi_metallic_paint_x_passes" -nodeType "mi_car_paint_phen_x_passes" -nodeType "misss_fast_shader_x_passes"
		 -dataType "byteArray" "Mayatomr" "2014.0 - 3.11.1.12 ";
requires -nodeType "McdGlobal" -nodeType "McdAgent" -nodeType "McdAgentInfo" -nodeType "McdBakeGeo"
		 -nodeType "McdBoundBox" -nodeType "McdBound" -nodeType "McdCrossroad" -nodeType "McdRBDEmitter"
		 -nodeType "McdKinePrim" -nodeType "McdPhyDebug" -nodeType "McdPhyJoint" -nodeType "McdPlace"
		 -nodeType "McdAction" -nodeType "McdActionProxy" -nodeType "McdStoryList" -nodeType "McdAgentDummy"
		 -nodeType "McdState" -nodeType "McdAgentGroup" -nodeType "McdVarGroup" -nodeType "McdVarHost"
		 -nodeType "McdSpace" -nodeType "McdCloth" -nodeType "McdActionShell" -nodeType "McdSkin"
		 -nodeType "McdAgentParticleEmitter" -nodeType "McdTerrain" -nodeType "McdMeshDrive"
		 -nodeType "McdMeshDriveIM" -nodeType "McdRoad" -nodeType "McdPath" -nodeType "McdSpot"
		 -nodeType "McdWind" -nodeType "McdZone" -nodeType "McdFormation" -nodeType "McdRMShader"
		 -nodeType "McdRMDispMat" -nodeType "McdTexInfo" -nodeType "McdGeoVisInfo" -nodeType "McdDecision"
		 -nodeType "McdBrain" -nodeType "McdBrainPost" "MiarmyExpressForMaya2014" "4.7.12";
requires "MiarmyProForMaya2013" "4.0";
requires "MiarmyProForMaya2012" "3.6";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2014";
fileInfo "version" "2014";
fileInfo "cutIdentifier" "201309050112-886424";
fileInfo "osv" "Microsoft Windows 8 Business Edition, 64-bit  (Build 9200)\n";
createNode McdDecision -n "avoidSphereLfTurnRt";
	setAttr -s 20 ".atv[0:19]" yes yes no no no no no no no no no no no 
		no no no no no no no;
	setAttr -s 2 ".atv";
	setAttr -s 20 ".in";
	setAttr ".in[0]" -type "string" "sound.x";
	setAttr ".in[1]" -type "string" "sound.d";
	setAttr -s 20 ".inLgg";
	setAttr ".inLgg[0]" -type "string" "someone in my sphere with angle from 0 to 90";
	setAttr ".inLgg[1]" -type "string" "someone in my sphere with distance < 30";
	setAttr -s 20 ".inInfMin[1:19]" yes no no no no no no no no no no no 
		no no no no no no no;
	setAttr -s 20 ".invMax[0:19]"  90 30 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0;
	setAttr -s 20 ".fin[0:19]"  20 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 20 ".fout[0:19]"  20 20 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0;
	setAttr -s 21 ".outAtv[0:20]" yes yes no no no no no no no no no no 
		no no no no no no no no no;
	setAttr -s 2 ".out";
	setAttr ".out[0]" -type "string" "ry";
	setAttr ".out[1]" -type "string" "*:rate";
	setAttr -s 20 ".outLgg";
	setAttr ".outLgg[0]" -type "string" "rotate to RIGHT as speed 120";
	setAttr ".outLgg[1]" -type "string" "change all actions playback speed 0.5";
	setAttr -s 2 ".outv[0:1]"  -120 0.5;
createNode McdDecision -n "avoidSphereRtTurnLf";
	setAttr -s 20 ".atv[0:19]" yes yes no no no no no no no no no no no 
		no no no no no no no;
	setAttr -s 20 ".in";
	setAttr ".in[0]" -type "string" "sound.x";
	setAttr ".in[1]" -type "string" "sound.d";
	setAttr -s 20 ".inLgg";
	setAttr ".inLgg[0]" -type "string" "someone in my sphere with angle from -90 to 0";
	setAttr ".inLgg[1]" -type "string" "someone in my sphere with distance < 30";
	setAttr -s 20 ".invMin[0:19]"  -90 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0;
	setAttr -s 20 ".inInfMin[1:19]" yes no no no no no no no no no no no 
		no no no no no no no;
	setAttr -s 20 ".invMax[1:19]"  30 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0;
	setAttr -s 20 ".fin[0:19]"  20 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 20 ".fout[0:19]"  20 20 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0;
	setAttr -s 21 ".outAtv[0:20]" yes yes no no no no no no no no no no 
		no no no no no no no no no;
	setAttr -s 2 ".out";
	setAttr ".out[0]" -type "string" "ry";
	setAttr ".out[1]" -type "string" "*:rate";
	setAttr -s 20 ".outLgg";
	setAttr ".outLgg[0]" -type "string" "rotate to LEFT as speed 120";
	setAttr ".outLgg[1]" -type "string" "change all actions playback speed 0.5";
	setAttr -s 2 ".outv[0:1]"  120 0.5;
createNode McdDecision -n "avoidSphereFrtSlowDn";
	setAttr -s 20 ".atv[0:19]" yes yes no no no no no no no no no no no 
		no no no no no no no;
	setAttr -s 20 ".in";
	setAttr ".in[0]" -type "string" "sound.x";
	setAttr ".in[1]" -type "string" "sound.d";
	setAttr -s 20 ".inLgg";
	setAttr ".inLgg[0]" -type "string" "someone in my sphere with angle from -10 to 10";
	setAttr ".inLgg[1]" -type "string" "someone in my sphere with distance < 30";
	setAttr -s 20 ".invMin[0:19]"  -10 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0;
	setAttr -s 20 ".inInfMin[1:19]" yes no no no no no no no no no no no 
		no no no no no no no;
	setAttr -s 20 ".invMax[0:19]"  10 30 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0;
	setAttr -s 20 ".fin[0:19]"  10 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 20 ".fout[0:19]"  10 20 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0;
	setAttr -s 21 ".outAtv[0:20]" yes no no no no no no no no no no no 
		no no no no no no no no no;
	setAttr ".out[0]" -type "string" "*:rate";
	setAttr -s 20 ".outLgg";
	setAttr ".outLgg[0]" -type "string" "change all actions playback speed 0.1";
	setAttr ".outv[0]"  0.1;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -av -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 1;
	setAttr -av ".unw" 1;
	setAttr -k on ".etw";
	setAttr -k on ".tps";
	setAttr -k on ".tms";
lockNode -l 1 ;
select -ne :renderPartition;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 6 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
lockNode -l 1 ;
select -ne :initialShadingGroup;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 40 ".dsm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
	setAttr -cb on ".mimt";
	setAttr -cb on ".miop";
	setAttr -k on ".mico";
	setAttr -cb on ".mise";
	setAttr -cb on ".mism";
	setAttr -cb on ".mice";
	setAttr -av -cb on ".micc";
	setAttr -k on ".micr";
	setAttr -k on ".micg";
	setAttr -k on ".micb";
	setAttr -cb on ".mica";
	setAttr -av -cb on ".micw";
	setAttr -cb on ".mirw";
lockNode -l 1 ;
select -ne :initialParticleSE;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
	setAttr -cb on ".mimt";
	setAttr -cb on ".miop";
	setAttr -k on ".mico";
	setAttr -cb on ".mise";
	setAttr -cb on ".mism";
	setAttr -cb on ".mice";
	setAttr -av -cb on ".micc";
	setAttr -k on ".micr";
	setAttr -k on ".micg";
	setAttr -k on ".micb";
	setAttr -cb on ".mica";
	setAttr -av -cb on ".micw";
	setAttr -cb on ".mirw";
lockNode -l 1 ;
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 6 ".s";
lockNode -l 1 ;
select -ne :defaultTextureList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 4 ".tx";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
lockNode -l 1 ;
select -ne :defaultRenderUtilityList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".u";
select -ne :defaultRenderingList1;
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
lockNode -l 1 ;
select -ne :defaultResolution;
	setAttr -av -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av ".w";
	setAttr -av ".h";
	setAttr -av ".pa" 1;
	setAttr -av -k on ".al";
	setAttr -av ".dar";
	setAttr -av -k on ".ldar";
	setAttr -k on ".dpi";
	setAttr -av -k on ".off";
	setAttr -av -k on ".fld";
	setAttr -av -k on ".zsl";
	setAttr -k on ".isu";
	setAttr -k on ".pdu";
select -ne :defaultLightSet;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -k on ".mwc";
	setAttr -k on ".an";
	setAttr -k on ".il";
	setAttr -k on ".vo";
	setAttr -k on ".eo";
	setAttr -k on ".fo";
	setAttr -k on ".epo";
	setAttr -k on ".ro" yes;
lockNode -l 1 ;
select -ne :defaultObjectSet;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -k on ".mwc";
	setAttr -k on ".an";
	setAttr -k on ".il";
	setAttr -k on ".vo";
	setAttr -k on ".eo";
	setAttr -k on ".fo";
	setAttr -k on ".epo";
	setAttr ".ro" yes;
lockNode -l 1 ;
select -ne :hardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k off ".ctrs" 256;
	setAttr -av -k off ".btrs" 512;
	setAttr -k off ".fbfm";
	setAttr -k off -cb on ".ehql";
	setAttr -k off -cb on ".eams";
	setAttr -k off -cb on ".eeaa";
	setAttr -k off -cb on ".engm";
	setAttr -k off -cb on ".mes";
	setAttr -k off -cb on ".emb";
	setAttr -av -k off -cb on ".mbbf";
	setAttr -k off -cb on ".mbs";
	setAttr -k off -cb on ".trm";
	setAttr -k off -cb on ".tshc";
	setAttr -k off ".enpt";
	setAttr -k off -cb on ".clmt";
	setAttr -k off -cb on ".tcov";
	setAttr -k off -cb on ".lith";
	setAttr -k off -cb on ".sobc";
	setAttr -k off -cb on ".cuth";
	setAttr -k off -cb on ".hgcd";
	setAttr -k off -cb on ".hgci";
	setAttr -k off -cb on ".mgcs";
	setAttr -k off -cb on ".twa";
	setAttr -k off -cb on ".twz";
	setAttr -cb on ".hwcc";
	setAttr -cb on ".hwdp";
	setAttr -cb on ".hwql";
	setAttr -k on ".hwfr";
	setAttr -k on ".soll";
	setAttr -k on ".sosl";
	setAttr -k on ".bswa";
	setAttr -k on ".shml";
	setAttr -k on ".hwel";
lockNode -l 1 ;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
select -ne :defaultHardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -av -k on ".rp";
	setAttr -k on ".cai";
	setAttr -k on ".coi";
	setAttr -cb on ".bc";
	setAttr -av -k on ".bcb";
	setAttr -av -k on ".bcg";
	setAttr -av -k on ".bcr";
	setAttr -k on ".ei";
	setAttr -av -k on ".ex";
	setAttr -av -k on ".es";
	setAttr -av -k on ".ef";
	setAttr -av -cb on ".bf";
	setAttr -k on ".fii";
	setAttr -av -cb on ".sf";
	setAttr -k on ".gr";
	setAttr -k on ".li";
	setAttr -k on ".ls";
	setAttr -av -k on ".mb";
	setAttr -k on ".ti";
	setAttr -k on ".txt";
	setAttr -k on ".mpr";
	setAttr -k on ".wzd";
	setAttr -k on ".fn" -type "string" "im";
	setAttr -k on ".if";
	setAttr -k on ".res" -type "string" "ntsc_4d 646 485 1.333";
	setAttr -k on ".as";
	setAttr -k on ".ds";
	setAttr -k on ".lm";
	setAttr -av -k on ".fir";
	setAttr -k on ".aap";
	setAttr -av -k on ".gh";
	setAttr -cb on ".sd";
lockNode -l 1 ;
select -ne :ikSystem;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av ".gsn";
	setAttr -k on ".gsv";
	setAttr -s 3 ".sol";
dataStructure -fmt "raw" -as "name=externalContentTable:string=node:string=key:string=upath:uint32=upathcrc:string=rpath:string=roles";
applyMetadata -fmt "raw" -v "channel\nname externalContentTable\nstream\nname v1.0\nindexType numeric\nstructure externalContentTable\n0\n\"MRigOK_OriginalAgent_stadiumMan_Body_color_file20\" \"fileTextureName\" \"Z:/animcarft/MRig/cloth_color.jpg\" 1617874645 \"Z:/animcarft/MRig/cloth_color.jpg\" \"sourceImages\"\n1\n\"MRigOK_OriginalAgent_stadiumMan_file2\" \"fileTextureName\" \"Z:/animcarft/MRig/shoe_color.jpg\" 3882243069 \"Z:/animcarft/MRig/shoe_color.jpg\" \"sourceImages\"\n2\n\"OriginalAgent_stadiumMan_Body_color_file2\" \"fileTextureName\" \"Z:/miarmy/example/walker/file/Walker_Project/sourceimages/casual/face color.jpg\" 1605933646 \"Z:/miarmy/example/walker/file/Walker_Project/sourceimages/casual/face color.jpg\" \"sourceImages\"\n3\n\"file3\" \"fileTextureName\" \"Z:/animcarft/MRig/leg_color.jpg\" 1825504361 \"Z:/animcarft/MRig/leg_color.jpg\" \"sourceImages\"\nendStream\nendChannel\nendAssociations\n" 
		-scn;
// End of avoid_each_other_simple.ma
