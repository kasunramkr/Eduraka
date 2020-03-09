import pandas, numpy

# Series
ar = numpy.array((2, 5, 6, 7))
print(pandas.Series(ar))

dic = {1: "abc", 2: "lmn", 3: "aer"}
print(pandas.Series(dic))

# DataFrame
dic = [{"c1": 3, "c2": 4}, {"c1": 6, "c2": 78}, {"c1": 0, "c2": 33, "c3": 2}]

df = pandas.DataFrame(dic, index=["r1", "r2", "r3"])
print(df)
print(df.loc["r2"])

df.to_csv("new.csv")
print(pandas.read_csv("new.csv"))
