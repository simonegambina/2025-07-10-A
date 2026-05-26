from model.category import Category
from model.model import Model

mymdl = Model()

c = Category(7, "Road Bikes")
mymdl.buildGraph(c)
n,e = mymdl.getGraphDetails()

print(f"N nodi: {n}, N archi: {e}")