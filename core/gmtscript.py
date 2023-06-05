from core.get_img_gmt import *



def gmthelp(urlarr, exarr, path, filedir):
	if int(exarr) in range(1, 87):
		get_images_gmt(urlarr[0] + exarr +'/', path, filedir)
		os.chdir(filedir)
	elif int(exarr) in range(87, 186):
		get_images_gmt(urlarr[1] + exarr +'/', path, filedir)
		os.chdir(filedir)
	elif int(exarr) in range(186, 222):                                                                                                                                          
		get_images_gmt(urlarr[2] + exarr +'/', path, filedir)
		os.chdir(filedir)                                                                                                                      
	elif int(exarr) in range(223, 362):                                                                                                                                          
		get_images_gmt(urlarr[3] + exarr +'/', path, filedir)
		os.chdir(filedir)                                                                                                                      
	elif int(exarr) in range(363, 444):                                                                                                                                          
		get_images_gmt(urlarr[4] + exarr +'/', path, filedir)
		os.chdir(filedir)                                                                                                                      
	elif int(exarr) in range(445, 532):                                                                                                                                          
		get_images_gmt(urlarr[5] + exarr +'/', path, filedir)
		os.chdir(filedir)                                                                                                                      
	elif int(exarr) in range(533, 630):                                                                                                                                          
		get_images_gmt(urlarr[6] + exarr +'/', path, filedir)
		os.chdir(filedir)                                                                                                                      
	elif int(exarr) in range(631, 737):                                                                                                                                     
		get_images_gmt(urlarr[7] + exarr +'/', path, filedir)
		os.chdir(filedir)                                                                                                                      
	elif int(exarr) in range(738, 910):                                                                                                                                          
		get_images_gmt(urlarr[8] + exarr +'/', path, filedir)
		os.chdir(filedir)                                                                                                                      
	elif int(exarr) in range(911, 1010):                                                                                                                                         
		get_images_gmt(urlarr[9] + exarr +'/', path, filedir)
		os.chdir(filedir)                                                                                                                      
	elif int(exarr) in range(1011, 1077):                                                                                                                                        
		get_images_gmt(urlarr[10] + exarr +'/', path, filedir)
		os.chdir(filedir)                                                                                                                      
	elif int(exarr) in range(1078, 1147):                                                                                                                                        
		get_images_gmt(urlarr[11] + exarr +'/', path, filedir)
		os.chdir(filedir)                                                                                                                      
	elif int(exarr) in range(1148, 1183):                                                                                                                                        
		get_images_gmt(urlarr[12] + exarr +'/', path, filedir)
		os.chdir(filedir)                                                                                                                     
	elif int(exarr) in range(1184, 1310):                                                                                                                                        
		get_images_gmt(urlarr[13] + exarr +'/', path, filedir)
		os.chdir(filedir)