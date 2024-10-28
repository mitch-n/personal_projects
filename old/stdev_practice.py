from statistics import mean, stdev

data=[13,1,1,1l]

print("Mean",mean(data))
print("Stdv",stdev(data))
threshold=int(mean(data))+int(stdev(data)*2)

print("Threshold",threshold)
