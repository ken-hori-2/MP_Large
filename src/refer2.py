
from lib2to3.pytree import Node
from sre_parse import State
import numpy as np
from itertools import count
# import pprint




class Property():
    def __init__(self, *arg):

        
        self.pre = np.array([
                            [7, "g"],
                            [7, "K"],
                            [7, "J"],
                            [7, "I"],
                            [7, "H"],
                            [7, "O"],
                            [7, "F"],
                            [7, "E"],
                            [7, "D"],
                            [7, "C"],
                            [7, "B"],
                            [7, "A"],
                            [0, "s"]
                            
                            ])

    
    def reference(self):
        
        
        Node = self.pre[:, 1]
        Arc = self.pre[:, 0]
        # print(Node)
        # print(Arc)
        Node = Node.tolist()
        Arc = Arc.tolist()
        num = [float(i) for i in Arc]
        # print(type(num))
        Arc_sum = sum(num)
        # print(Arc_sum)

        PERMISSION = [
                
                
                # [Arc_sum-float(Arc[5])-float(Arc[4])-float(Arc[3])-float(Arc[2])-float(Arc[1])-float(Arc[0])],
                # [Arc_sum-float(Arc[5])-float(Arc[4])-float(Arc[3])-float(Arc[2])-float(Arc[1])],
                # [Arc_sum-float(Arc[5])-float(Arc[4])-float(Arc[3])-float(Arc[2])],
                # [Arc_sum-float(Arc[5])-float(Arc[4])-float(Arc[3])],
                # [Arc_sum-float(Arc[5])-float(Arc[4])],
                # [Arc_sum-float(Arc[5])],
                # [Arc_sum]

                
                [0],
                [3],
                [6],
                [9],
                [12],
                [15],
                [18],
                [21],
                [24]
        ]

        return self.pre, Node, Arc, Arc_sum, PERMISSION

if __name__ == "__main__":
   test = Property()
   test.reference