




def func(mapp):
    mapp["a"] -= 1

mapp = {}
mapp["a"] = 5
func(mapp)
print(mapp)