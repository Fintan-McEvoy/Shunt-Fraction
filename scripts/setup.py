import os
cwd = os.getcwd()
exec(open(cwd+'/scripts/import_modules.py').read())
exec(open(cwd+'/scripts/shuntFraction.py').read())
exec(open(cwd+'/scripts/plotTAC.py').read())
exec(open(cwd+'/scripts/TAC.py').read())
exec(open(cwd+'/scripts/hello.py').read())
