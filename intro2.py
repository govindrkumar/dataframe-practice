import numpy as np
import pandas as pd

dict1 = {
    'empname': ['Govind', 'Sanjeev', 'Roshni', 'Anita'],
    'sex': ['M', 'M', 'F', 'F'],
    'department': ['Sales', 'IT', 'HR', 'Marketing']
}

dict2 = {
    'empname': ['Rahul', 'Simran', 'Amit', 'Neha'],
    'sex': ['M', 'F', 'M', 'F'],
    'department': ['Finance', 'IT', 'Sales', 'HR']
}

dict3 = {
    'empname': ['Karan', 'Pooja', 'Manish', 'Sonal'],
    'sex': ['M', 'F', 'M', 'F'],
    'department': ['Marketing', 'Finance', 'IT', 'Sales']
}

dict4 = {
    'empname': ['Vikram', 'Neeta', 'Ravi', 'Tanya'],
    'sex': ['M', 'F', 'M', 'F'],
    'department': ['HR', 'Marketing', 'Finance', 'IT']
}
mergedict = {
    'empname' : dict1['empname']+dict2['empname']+dict3['empname']+dict4['empname'],
    'sex' : dict1['sex']+dict2['sex']+dict3['sex']+dict4['sex'],
    'department' : dict1['department']+dict2['department']+dict3['department']+dict4['department']

}

df = pd.DataFrame(mergedict)
print(df)

list2 = [
    [2,3,4],
    [3,2,1],
    [4,6,2]
]
print(pd.DataFrame(list2))