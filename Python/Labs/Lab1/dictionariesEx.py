d1 = {'simple_key':'hello'}
d2 = {'k1':{'k2':'hello'}}
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]} 
#Not given by teachers: Info from net
dict4 = {'k1':[1,2,{'k2':['k3',{'k4':[1,2,['hello']]}]}]}
#this dict4 alone from net
print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])
print(dict4['k1'][2]['k2'][1]['k4'][2][0])