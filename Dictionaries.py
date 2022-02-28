monthConversions = {
 "Jan": "January",        # we can also use 0,1,2,...instead of jan, feb etc
 "Feb": "February",       # and we also access these numbers(0,1,2....)
 "Mar": "March",
 "Apr": "April",
 "May":	"May"	,
 "Jun":	"June",
 "Jul":	"July",
 "Aug":	"August",
 "Sep":	"September",	
 "Oct":	"October",	
 "Nov":	"November",	
 "Dec":	"December",
 }

print(monthConversions["Nov"])              # To access 'Nov'

print(monthConversions.get("Dec"))          # To access 'Dec'

print(monthConversions.get("Luv"))          # To access 'another'

print(monthConversions.get("Luv", "Not a valid key"))          # To access 'another'
