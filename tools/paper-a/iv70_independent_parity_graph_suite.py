#!/usr/bin/env python3
import itertools,json
from collections import Counter
GRAPHS={"single_edge":(2,[(0,1)]),"two_disjoint_edges":(4,[(0,1),(2,3)]),"path3":(3,[(0,1),(1,2)]),"triangle":(3,[(0,1),(1,2),(0,2)]),"square":(4,[(0,1),(1,2),(2,3),(0,3)]),"star3":(4,[(0,1),(0,2),(0,3)]),"path4":(4,[(0,1),(1,2),(2,3)])}
def bitmask(edges):
 masks=[(1<<a)|(1<<b) for a,b in edges]; t=v=r=i=0; hist=Counter()
 for seq in itertools.product(range(len(edges)),repeat=4):
  t+=1; states=[]; s=0
  for x in seq:
   s^=masks[x]; states.append(s)
  hist[states[-1].bit_count()]+=1
  if states[-1]==0:
   v+=1
   if states[1]==0 or states[2]==0:r+=1
   else:i+=1
 return {"total":t,"vacuum":v,"reducible":r,"irreducible":i,"hist":dict(sorted(hist.items()))}
def parity(edges):
 t=v=r=i=0; hist=Counter()
 for seq in itertools.product(range(len(edges)),repeat=4):
  t+=1; state=set(); states=[]
  for idx in seq:
   a,b=edges[idx]
   for vertex in (a,b):
    if vertex in state: state.remove(vertex)
    else: state.add(vertex)
   states.append(frozenset(state))
  hist[len(states[-1])]+=1
  if not states[-1]:
   v+=1
   if not states[1] or not states[2]:r+=1
   else:i+=1
 return {"total":t,"vacuum":v,"reducible":r,"irreducible":i,"hist":dict(sorted(hist.items()))}
def run_suite():
 output={}
 for name,(vertices,edges) in GRAPHS.items():
  left,right=bitmask(edges),parity(edges)
  output[name]={"vertices":vertices,"edges":edges,"bitmask":left,"incidence_parity":right,"match":left==right}
 return {"graphs":output,"all_match":all(v["match"] for v in output.values())}
if __name__=="__main__":print(json.dumps(run_suite(),indent=2))
