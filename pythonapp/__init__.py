from termcolor import cprint


def msg():
	print(''),
	cprint('===========================', 'yellow'),
	print(''),
	cprint('_My Own Python Application_', 'green', attrs=['bold', 'blink']),
	cprint('  Hosted in Linode Cloud   ', 'green', attrs=['reverse', 'concealed']),
	print(''),
	cprint('===========================', 'yellow'),
	print('')
	
    