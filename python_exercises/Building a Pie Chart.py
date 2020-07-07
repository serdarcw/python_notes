https://edabit.com/challenge/GwCAximybWF6ANdLY

Building a Pie Chart

data={"a": 30, "b": 15, "c": 55}

k=360/sum(data.values())
for key, value in data.items():
    data[key]=int(value*k,1)
print(data)


def pie_chart(data):
	total = sum(v for k,v in data.items())
	for key in data:
		data[key] *= 360/total
		data[key] = round(data[key],1)
	return data



    def pie_chart(data):
	total = sum(data.values())
	return {i:round(data[i]/total * 360, 1) for i in data}




    def pie_chart(data):
	freq_total = 0
	for category in data:
		freq_total += data[category]
	for category in data:
		data[category] /= freq_total
		data[category] = round(data[category] * 360, 1)
	return data




def pie_chart(data):
	tot = sum(data.values())
	for i in data:
		data[i] = round(data[i]*360/tot,1)
	return data

