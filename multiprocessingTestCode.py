from multiprocessing import Pool
import time

globalFound25=False
def f(x):
	return 2
	global globalFound25
	if(globalFound25):
		return 0
	else:
		result=x*x
		if result ==25:
			#time.sleep(2)
			globalFound25=True
	return x*x

if __name__=='__main__':
	p = Pool(5)
	#found25=False
	print(p.map(f, [1,5,2,3,4]))
	print(globalFound25)
	#for i in [1,2,3,5,4]:
	#	print(f(i))