
import time
import webbrowser
def fresh():	
	i=0
	utube=r"https://www.youtube.com/watch?v=J3BpOKzEdMI"

	while i<2:
		print 'time:%s' %time.ctime()
		webbrowser.open(utube)
		time.sleep(2)
		i+=1

fresh()
