#def all_thing_is_obj(object: any) ->int:
#	name = type(object).__name__
#	notation = type(object)
#	if (name == 'str'):
#		print(f"{object} is in the kitchen")
#	elif (name == 'int'):
#		print("Type not found")
#	else:
#		print(f"{name}: {notation}")
#	return 42

def all_thing_is_obj(obj)->int:
    if isinstance(obj, str):
        print(f"{obj} is in the kitchen")
    elif isinstance(obj, int):
        print("Type not found")
    else:
        print(f"{type(obj).__name__}: {type(obj)}")
    return 42