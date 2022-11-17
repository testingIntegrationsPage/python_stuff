AWS_SECRET_KEY = 'ASD!Q@_asdaF2rAScazasAW2r12%R'

p = subprocess.Popen(cmd,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE,
                     shell=True)
output, error = p.communicate()
