from whois import query
domain = input('domain > ')
registrar = input('registrar > ')
if registrar in query(domain).registrar:
	print(domain)