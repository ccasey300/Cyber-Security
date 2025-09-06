# program using key value pairs... dictionary
# 24/01/23
monthConversions = {
    0: "January",
    1: "February",
    2: "March",
    3: "April",
    4: "May",
    5: "June",
    6: "July",
    7: "August",
    8: "September",
    9: "October",
    10: "November",
    11: "December"
}
print(monthConversions[0])
print(monthConversions.get("XXX", "Not a valid key."))
