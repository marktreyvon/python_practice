import os,time
o1 = os.popen('git add .')
print(o1.read())
inp = input()
o2 = os.popen('git commit -m ' + inp)
print(o2.read())

o3 = os.popen('git push')
time.sleep(5)
o3.write('githubMIMA666!')
print(o3.read())