import pathlib, os
 
includes = ['*.msg']
excludes = ['PENDING']

# Get the list of all files and directories
path = "O:/FINANCE/SS-CA/Contracting/PaymentRequests"

these = os.walk(path)

for x in these:
    print(x)
 


