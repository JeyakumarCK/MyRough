import time
import webbrowser

counter = 0 
print "Program started at " + time.ctime()
while counter < 3 :
    time.sleep(10)
    counter += 1
    print counter, 'Opening browser'
    webbrowser.open("https://www.youtube.com/watch?v=g05kMdDz2cE")
else:
    print "While loop completed." + time.ctime()

print "Program execution completed"