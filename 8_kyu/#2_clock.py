def past(h, m, s):
    # Convert to seconds to milidetik
    s *= 1000
    # Convert to minutes to milidetik
    m *= 60000
    # Convert to hours to milidetik
    h *= 3600000
    # Sum
    return h + m + s

# Best Solution
# def past(h, m, s):
    # return (3600*h + 60*m + s) * 1000


print(past(0,1,1),61000)
print(past(1,1,1),3661000)
print(past(0,0,0),0)
print(past(1,0,1),3601000)
print(past(1,0,0),3600000)