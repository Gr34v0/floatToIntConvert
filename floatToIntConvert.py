#import math

def convert(rh, mx, mn):
	
	result = 0
	convertVar = 65536/(mx - mn)
	
	result = round((rh - mn) * convertVar)
	
	print(result)
	
	return result

def unconvert(rh, mx, mn):
	
	result = 0
	
	convertVar = 65536/(mx - mn)
	
	result = round(rh + mn/(65536/(mx-mn)))
	
	print(result)
	
def main():
	
	mx = 110.4
	mn = 20.1
	rh = 20.2
	
	unconvert(convert(rh, mx, mn), mx, mn)
	
	
main()