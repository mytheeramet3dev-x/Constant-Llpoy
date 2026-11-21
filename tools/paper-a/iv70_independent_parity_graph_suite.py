#!/usr/bin/env python3
"""IV-70 graph suite cross-check: bitmask flip tracking vs independent vertex parity sets."""
import itertools, json
from collections import Counter

GRAPHS = {
 "single_edge": (2, [(0,1)]),
 "two_disjoint_edges": (4, [(0,1),(2,3)]),
 "path3": (3, [(0,1),(1,2)]),
 "triangle": (3, [(0,1),(1,2),(0,2)]),
 "square": (4, [(0,1),(1,2),(2,3),(0,3)]),
 "star3": (4, [(0,1),(0,2),(0,3)]),
 "path4": (4, [(0,1),(1,2),(2,3)]),
}

def bitmask_counts(n, edges):
    masks=[(1<<a)|(1<<b) for a,b in edges]
    total=vac=red=irr=0
    hist=Counter()
    for seq in itertools.product(range(len(edges)), repeat=4):
        total+=1; state=0; states=[]
        for idx in seq:
            state ^= masks[idx]; states.append(state)
        end=states[-1]; hist[end.bit_count()]+=1
        if end==0:
            vac+=1
            if states[1]==0 or states[2]==0: red+=1
            else: irr+=1
    return {"total":total,"vacuum":vac,"reducible_vacuum":red,"irreducible_vacuum":irr,"endpoint_hist":dict(sorted(hist.items()))}

def parity_counts(n, edges):
    total=vac=red=irr=0
    hist=Counter()
    for seq in itertools.product(range(len(edges)), repeat=4):
        total+=1; parity=set(); states=[]
        for idx in seq:
            a,b=edges[idx]
            for v in (a,b):
                if v in parity: parity.remove(v)
                else: parity.add(v)
            states.append(frozenset(parity))
        end=states[-1]; hist[len(end)]+=1
        if not end:
            vac+=1
            if not states[1] or not states[2]: red+=1
            else: irr+=1
    return {"total":total,"vacuum":vac,"reducible_vacuum":red,"irreducible_vacuum":irr,"endpoint_hist":dict(sorted(hist.items()))}

def run_suite():
    results={}
    for name,(n,edges) in GRAPHS.items():
        a=bitmask_counts(n,edges); b=parity_counts(n,edges)
        results[name]={"vertices":n,"edges":edges,"bitmask":a,"incidence_parity":b,"match":a==b}
    return {"suite":results,"all_match":all(x["match"] for x in results.values())}
if __name__=="__main__":
    print(json.dumps(run_suite(),indent=2))
