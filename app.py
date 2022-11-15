from math import sin
from flask import Flask
app = Flask(__name__)

if __name__ == "__main__":
	#runIntegrations(lower, upper)
	print("STARTED")

Ns = [10, 100, 1000, 10000, 100000, 1000000]
lower = 0
upper = 3.14159

def numericalIntegration(parts, lowerBound, upperBound):
	
	sections = [lowerBound + x * (upperBound - lowerBound) / parts for x in range(parts + 1)]
	#print(sections)
	result = 0.0
	#print(len(sections))
	for index in range(len(sections) - 1):

		#print("===========================")
		x = sections[index]
		#print(x)
		y = sections[index + 1]
		#print(y)
		di = abs(sin(x))
		#print(di)
		result += (di * abs(x - y))
		#print(di)
	return result


@app.route('/runIntegrations/<lowerBound>/<upperBound>')
def runIntegrations(lowerBound, upperBound):
	print("I'm here!")
	reponses = ""
	for N in Ns:
		res = numericalIntegration(N, float(lowerBound), float(upperBound))
		reponses += "result: " + str(res) + " Points: " + str(N) + "\n"
		print("result: " + str(res) + " Points: " + str(N))

	return "OK \n" + reponses
