import matplotlib.pyplot as plt

axis = ["x", "y", 'z']

sensor = ['gyro', 'magnetic']

file_names = [i + '_' + j + '.txt' for i in sensor for j in axis]
files = [open("data/" + i) for i in file_names]

timer_file = open("data/timer.txt")
timer = list(timer_file)
timer_file.close()

timer = [float(i.rstrip('\n')) for i in timer]

data = dict.fromkeys(file_names, [])

for i in range(len(file_names)):
    data[file_names[i]] = list(files[i])
    data[file_names[i]] = [float(j.rstrip('\n')) for j in data[file_names[i]]]

[i.close() for i in files]

plt.figure(1)
plt.title("gyro")
for i in range(3):

    plt.subplot(3, 1, i+1)
    plt.plot(timer, data[file_names[i]])

plt.figure(2)
plt.title("magnetic")
for i in range(3):

    plt.subplot(3, 1, i+1)
    plt.plot(timer, data[file_names[i+3]])
plt.show()

print(data)
print(timer)






