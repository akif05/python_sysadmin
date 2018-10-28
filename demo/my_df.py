import subprocess

threshold = 20
partition = "/"

df = subprocess.Popen(["df", "-h"], stdout=subprocess.PIPE)
for line in df.stdout:
    # Split into spac-separated fields
    splitline = line.decode().split()
    # The %full figure is in field 4,
    # the mount point is in field 5
    if splitline[8] == partition:
        # This is the partition we want to check
        # First remove last character of filed 4
        if int(splitline[4][:-1]) > threshold:
            print(line)
            print("Partition is %s" % partition)
            print("In procent is :%d%% " % threshold)
            print("WARNING")