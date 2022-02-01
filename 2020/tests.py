import multiprocessing


ahash = {}

def func(mapp):
    mapp["a"] -= 1

mapp = {}
mapp["a"] = 5
func(mapp)
print(mapp)


def funk():
    print("func")
    global ahash
    hashy = {}
    hashy["a"] = "funk"
    ahash["b"] = "33"
    return hashy

ahash = {}
ahash["a"] = 22
p1 = multiprocessing.Process(target=funk, args=())
p1.start()
p1.join()
print(ahash)


a = [1]
b = a
a[0] = 2
b[0]
print(b)

# merge dicts
a = {}
b = {}
c = {}
a[1] = 1
b[2] = 2
c[3] = 3

d = {**a, **b, **c}
print(d)