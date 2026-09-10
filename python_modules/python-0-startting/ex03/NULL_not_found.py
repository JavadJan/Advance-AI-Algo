#import math
#def NULL_not_found(object: any) ->int:
#	name = type(object).__name__
#	notation = type(object)
#	if(object == "" and name == 'str'):
#		print(f"Empty : {notation}")
#	elif(name == 'bool'):
#		print(f"Fake : {object} {notation}")
#	elif(object == 0):
#		print(f"Zero : {object} {notation}")
#	elif(name == 'str'):
#		print("Type not Found")
#	elif math.isnan(object) if isinstance(object, float) else False:
#		print(f"Cheese: {object} {notation}")
#	elif (object is None):
#		print(f"Nothing: {object} {notation}")
	
#	return 1
import math

def NULL_not_found(obj: any) -> int:

    if obj is None:
        print(f"Nothing: {obj} {type(obj)}")

    elif isinstance(obj, bool):
        print(f"Fake : {obj} {type(obj)}")

    elif isinstance(obj, str) and obj == "":
        print(f"Empty : {type(obj)}")

    elif isinstance(obj, int) and obj == 0:
        print(f"Zero : {obj} {type(obj)}")

    elif isinstance(obj, float) and math.isnan(obj):
        print(f"NaN : {obj} {type(obj)}")

    elif isinstance(obj, str):
        print("Type not Found")

    else:
        print(f"{type(obj).__name__}: {type(obj)}")

    return 1
