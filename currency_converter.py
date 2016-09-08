# Simple currency converter

#import libraries
import urllib
import re

# Find and read current currency exchange rates from http://www.xe.com/
html = urllib.urlopen("http://www.xe.com/").read()

# Command Line Directions
print "\nSelect the currency you would like to convert to from USD\n"
print "Ex. Type EUR for USD To EURO conversion\n"
print "List of available exchanges\n"

# Find all instances of currency rates
# --------------------------------------------
# Current Euro exchange rate
USD2EUR = "rel='EUR,USD,1,2'>(.+?.)</a>"
# Current Great B. Pound exchange rate
USD2GBP = "rel='GBP,USD,1,3'>(.+?.)</a>"
# Current Australian Dollar exchange rate
USD2AUD = "rel='AUD,USD,1,5'>(.+?.)</a>"
# Current Canadian Dollar exchange rate
USD2CAD = "rel='CAD,USD,1,6'>(.+?.)</a>"
# Current New Z. exchange rate
USD2NZD = "rel='NZD,USD,1,8'>(.+?.)</a>"
# Current Japense Yen exchange rate
USD2JPY = "rel='JPY,USD,1,9'>(.+?.)</a>"

# Find EUR rate
USD2EURPAT = re.compile(USD2EUR)
USD2EUR_RATE = re.findall(USD2EURPAT,html)

# Find GBP rate
USD2GBPPAT = re.compile(USD2GBP)
USD2GBP_RATE = re.findall(USD2GBPPAT,html)

# Find AUD rate
USD2AUDPAT = re.compile(USD2AUD)
USD2AUD_RATE = re.findall(USD2AUDPAT,html)

# Find CAD rate
USD2CADPAT = re.compile(USD2CAD)
USD2CAD_RATE = re.findall(USD2CADPAT,html)

# Find NZD rate
USD2NZDPAT = re.compile(USD2NZD)
USD2NZD_RATE = re.findall(USD2NZDPAT,html)

# Find JPY rate
USD2JPYPAT = re.compile(USD2JPY)
USD2JPY_RATE = re.findall(USD2JPYPAT,html)


# Extract Data
eur = float(''.join(USD2EUR_RATE))
gbp = float(''.join(USD2GBP_RATE))
aud = float(''.join(USD2AUD_RATE))
cad = float(''.join(USD2CAD_RATE))
nzd = float(''.join(USD2NZD_RATE))
jpy = float(''.join(USD2JPY_RATE))

# Store values in dictionary
rate_dict = {'EURO': eur, 'GBP': gbp, 'AUD': aud, 'CAD': cad, 'NZD': nzd, 'JPY': jpy}
print " COUNTRY   CURRENT RATE"
print " -------   ------------"
print " EURO     %f\n GBP      %f\n AUD      %f\n CAD      %f\n NZD      %f\n JPY      %f" %(rate_dict['EURO'],rate_dict['GBP'],rate_dict['AUD'],rate_dict['CAD'],rate_dict['NZD'],rate_dict['JPY'])

# Collect Data from user prompt
currency = float(raw_input('\nEnter $USD Amount\n'))
rate = raw_input('Enter Country\n')

# Convert USD to appropriate currency
conv_curr = currency*rate_dict[rate]

# Print current currency exchange rate
print "\n$%f USD is %f %s" %(currency,conv_curr,rate) 
