#test file to just try some algos and stuff without dealing with the rest of the project files

test = "123456789"

for i in range(len(test)):
    t = test[i:] + test[:i]
    print(t)