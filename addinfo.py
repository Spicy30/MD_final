import sys
import os
import csv
from pyproj import *


A = 0.00001549
B = 0.000006521
p = Proj(r"+proj=tmerc +ellps=GRS80 +lon_0=121 +x_0=250000 +k=0.9999")

def TWD67ToTWD97(X67, Y67):
    X97=X67+807.8+A*X67+B*Y67
    Y97=Y67-248.6+A*Y67+B*X67
    return (X97, Y97)

def TWD97ToWGS84(X97, Y97):
    ''' 
    cmd = 'echo %.15f %.15f | proj -I +proj=tmerc +ellps=GRS80 +lon_0=121 +x_0=250000 +k=0.9999 -f "%%.15f"' %(X97, Y97)
    result = os.popen(cmd).read().strip()
    result = result.split()
    WGS84_X = float(result[0])
    WGS84_Y = float(result[1])
    '''
    (WGS84_X, WGS84_Y) = p(X97, Y97, inverse=True)
    return (WGS84_X, WGS84_Y)

if __name__ == '__main__':
    
    year = '102'
    with open( year + 'y_twd97.csv', 'r') as file, open(year,'w') as out:
        next(file)
        count = 0
        intersections = []
        infos = []
        infos.append(['CASE_NO','IEOK_01,ACCD_TP','Year,x_coord','y_coord',
                     'Rd_id','Latitude','Longitude','Rd1_sp','Rd2_sp',
                     'Rd1_1_lane','Rd1_2_lane','Rd2_1_lane','Rd2_2_lane','lane_id','year',
                     'Big1_1_AM','Small1_1_AM','Scooter1_1_AM','PCU1_1_AM','Trun1_1_AM',
                     'Big1_2_AM','Small1_2_AM','Scooter1_2_AM','PCU1_2_AM','Trun1_2_AM',
                     'Big2_1_AM','Small2_1_AM','Scooter2_1_AM','PCU2_1_AM','Trun2_1_AM',
                     'Big2_2_AM','Small2_2_AM','Scooter2_2_AM','PCU2_2_AM','Trun2_2_AM'])
        
        
        '''
        with open('position.txt','r') as posfile:
            next(posfile)
            for pos in csv.reader(posfile,delimiter='\t'):
                y = float(pos[0])
                x = float(pos[1])
                intersections.append([x,y])
        '''
        
        with open('intersection_no_ch.txt','r') as posfile:
            next(posfile)
            for intersection in csv.reader(posfile,delimiter=','):
                intersections.append(intersection)
        #print(intersections)
        
        
        
        for accident in csv.reader(file):
            x67 = float(accident[4])
            y67 = float(accident[5])
            time = int(accident[1])%1000
            (x97, y97) = TWD67ToTWD97(x67,y67)
            (x,y) = TWD97ToWGS84(x67, y67)
            for intersection in intersections:
                x1 = 1000*x
                y1 = 1000*y
                x2 = float(intersection[2])*1000
                y2 = float(intersection[1])*1000
                #print x1,y1,x2,y2
                if (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) < 9:
                    count += 1
                    if time > 1200:
                        info = accident + intersection[0:10] + intersection[11:30]
                    else:
                        info = accident + intersection[0:10] + intersection[31:50]
                    infos.append(info)
                    break
        print(count)
        #print(infos)
        
        
        csv.writer(out).writerows(infos)
        
        
        