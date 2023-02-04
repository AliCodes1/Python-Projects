import re
str_pattern=r"\w{1-15}@\w{1-8}[.](c,o,m|c,a)$"
email_1=False
while email_1==False:
    ent_email=input('{:<30s}'.format('Enter an e-mail address:'))
    if re.match(str_pattern,ent_email)!=None:
        print("Your e-mail address,",ent_email+",","has been successfully created!")
        email_1=True
    else:
        print("Invalid e-mail address! Please try again...\n")