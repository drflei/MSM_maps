def plotmapfile(file,save=True):
    
    from scipy.interpolate import griddata
    import matplotlib.pyplot as plt
    import numpy as np
    
    x,y,z = np.loadtxt(file,skiprows=0,usecols = (1,0,5),unpack=True)
    
    # define grid.
#    xi = np.linspace(-0.1,360.1,360)
#    yi = np.linspace(-90.1,90.1,180)
    xg, yg = np.mgrid[0:360:360j, -90:90:180j]
    # grid the data.
    zg = griddata((x,y),z,(xg,yg),method='cubic')
    
    # contour the gridded data, plotting dots at the nonuniform data points.
    plt.figure(figsize=(11,7))
    plt.subplots_adjust(right=1.0)
    CS = plt.contour(xg,yg,zg,30,linewidths=0.5,colors='k')
    plt.clabel(CS, inline=1, fontsize=10)
    CS = plt.contourf(xg,yg,zg,30,cmap=plt.cm.rainbow,
                      vmax=abs(zg).max(), vmin=-abs(zg).max())
    plt.colorbar() # draw colorbar
    
    plt.xlabel("Longitude [Deg]")
    plt.ylabel("Latitude [Deg]")
    plt.title(' File: ' + file)
    if save:
      file = file.replace('/','_').replace('..','')[:-3]+'png'
      plt.savefig(file)
    else:  
      plt.show()
    plt.close()  
      
import os
plotmapfile('2030/AVKP7T12.AVG',save=True)
# dirs = ('2000','2030')

# for dir in dirs:
#     for directory, dirnames, fileList in os.walk(dir):
#         for f in fileList: 
#             if not f.endswith('.AVG'):
#                 continue  
#             file = directory+'/'+f
#             print (file)
#             plotmapfile(file)
