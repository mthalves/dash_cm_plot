colors = {
	'titlebg': '#CECECE',
    'background': '#FFFFFF',
    'text': '#000000'
}

def fopen(filename,mode):
		# 1. Open the file
		file = open(filename,'r')

		# 2. Seeking to the start
		file.seek(0,0)

		# 3. Return to the function's call
		return file

def multFunc(*funcs):
    def multFunc(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return multFunc