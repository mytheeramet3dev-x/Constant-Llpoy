#!/usr/bin/env python3
import itertools,json
from collections import Counter
GRAPHS={"single_edge":(2,[(0,1)]),"two_disjoint_edges":(4,[(0,1),(2,3)]),"path3":(3,[(0,1),(1,2)]),"triangle":(3,[(0,1),(1,2),(0,2)]),"square":(4,[(0,1),(1,2),(2,3),(0,3)]),"star3":(4,[(0,1),(0,2),(0,3)]),"path4":(4,[(0,1),(1,2),(2,3)])}
def bitmask(n,edges):
 masks=[(1<<a)|(1<<b) for a,b in edges]; t=v=r=i=0; hist=Counter()
 for seq in itertools.product(range(len(edges)),repeat=4):
  t+=1; states=[]; s=0
  for x in seq:
   s^=masks[x];states.append(s)
  hist[states[-1].bit_count()]+=1
  if states[-1]==0:
   v+=1
   if states[1]==0 or states[2]==0:r+=1
   else:i+=1
 return {"total":t,"vacuum":v,"reducible":r,"irreducible":i,"hist":dict(sorted(hist.items()))}
def parity(n,edges):
 t=v=r=i=0;hist=Counter()
 for seq in itertools.product(range(len(edges)),repeat=4):
  t+=1; s=set(); states=[]
  for x in seq:
   for z in edges[x]:
    if z in s:s.remove(z)
    else:s.add(z)
   states.append(frozenset(s))
  hist[len(states[-1])]+=1
  if not states[-1]:
   v+=1
   if not states[1] or not states[2]:r+=1
   else:i+=1
 return {"total":t,"vacuum":v,"reducible":r,"irreducible":i,"hist":dict(sorted(hist.items()))}
def run():
 out={}
 for name,(n,e) in GRAPHS.items():
  a,b=bitmask(n,e),parity(n,e);out[name]={"vertices":n,"edges":e,"bitmask":a,"parity":b,"match":a==b}
 return {"results":out,"all_match":all(x["match"] for x in out.values())}
print(json.dumps(run(),indent=2))
