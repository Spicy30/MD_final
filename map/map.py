# python 2
# get position of all crossroad


pos = ['Latitude', 'Longitude']
data = [('Intersection_id', 'Longitude', 'Latitude', 'counts')]

with open('../new/info.txt') as f, open('../new/102_count.txt') as f2:
    name = f.readline().split(',')
    name2 = f2.readline().split(',')
    for line in f:
        line = line.split(',')
        line2 = f2.readline().split(',')
        rid = int(line[0])
        lat = float(line[name.index(pos[0])])
        lon = float(line[name.index(pos[1])])
        count = int(line2[2][:-1])
        data.append( (rid, lon, lat, count) )

print data

with open('map_102_PM.xls', 'w') as f:
    f.write(('%s\t%s\t%s\t%s\n')%(data[0][0], data[0][1], data[0][2], data[0][3]))
    for cross in data[1:]:
        f.write(('%d\t%f\t%f\t%d\n')%(cross[0], cross[1], cross[2], cross[3]))
    
