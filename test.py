# Copas dari stackoverflow.com
def make_readable(seconds):
    numdays = int((seconds % 31536000) / 86400); 
    numhours = int(((seconds % 31536000) % 86400) / 3600);
    numminutes = int((((seconds % 31536000) % 86400) % 3600) / 60);
    numseconds = (((seconds % 31536000) % 86400) % 3600) % 60;
    return "{}:{}:{}".format(numhours + (numdays * 24),numminutes,numseconds);

print(make_readable(0), "00:00:00")
print(make_readable(5), "00:00:05")
print(make_readable(60), "00:01:00")
print(make_readable(86399), "23:59:59")
print(make_readable(359999), "99:59:59")