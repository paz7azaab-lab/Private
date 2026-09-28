def detect_anomaly(values, z_threshold=3.0):
    if len(values)<2:
        return False
    mean=sum(values)/len(values)
    var=sum((x-mean)**2 for x in values)/len(values)
    sd=var**0.5
    if sd==0:
        return False
    return abs(values[-1]-mean)/sd >= z_threshold
