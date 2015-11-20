

def find_dirs(dirstr=""):
	# Finds directories matching the input pattern
	# and returns the list
    import subprocess as sp
    cmdline = ["ls -d */ | grep "+dirstr]
    out, err = sp.Popen(cmdline, stdout=sp.PIPE, stderr = sp.PIPE, shell=True).communicate()
    return out.split()



def find_files(filestr=""):
	# Finds files (no directories)  matching the input pattern
	# and returns the list
    import subprocess as sp
    cmdline = ["ls -p | grep " + filestr + " | grep -v /"]
    out, err = sp.Popen(*cmdline, stdout=sp.PIPE, stderr = sp.PIPE, shell=True).communicate()
    return out.split()
