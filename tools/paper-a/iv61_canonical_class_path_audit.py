#!/usr/bin/env python3
"""IV-61: exhaustive four-edge multiset canonical class/path audit (8 vertices)."""
from itertools import combinations, combinations_with_replacement, permutations
from collections import Counter

def canonical(weighted):
    adj={}
    for (u,v),m in weighted.items():
        adj.setdefault(u,set()).add(v); adj.setdefault(v,set()).add(u)
    unseen=set(adj); components=[]
    while unseen:
        root=min(unseen); stack=[root]; comp=set()
        while stack:
            x=stack.pop()
            if x in comp: continue
            comp.add(x); unseen.discard(x); stack.extend(adj[x]-comp)
        verts=sorted(comp); best=None
        for p in permutations(range(len(verts))):
            mp=dict(zip(verts,p))
            enc=tuple(sorted((min(mp[u],mp[v]),max(mp[u],mp[v]),m)
                for (u,v),m in weighted.items() if u in comp and v in comp))
            if best is None or enc<best: best=enc
        components.append((len(verts),best))
    return tuple(sorted(components,key=repr))

def states(seq):
    s=set(); result=[]
    for e in seq:
        s.symmetric_difference_update(e); result.append(tuple(sorted(s)))
    return result

def audit(n=8,k=4):
    edges=list(combinations(range(n),2)); classes={}
    for ms in combinations_with_replacement(edges,k):
        key=canonical(Counter(ms))
        c=classes.setdefault(key,[0,0,0,ms])
        c[0]+=1
        orders=set(permutations(ms)); c[1]+=len(orders)
        for seq in orders:
            ss=states(seq)
            if not ss[1] or not ss[2]: c[2]+=1
    return classes

if ____=="__main__":
    C=audit()
    print("multisets",sum(v[0] for v in C.values()))
    print("classes",len(C))
    print("ordered sequences",sum(v[1] for v in C.values()))
    print("vacuum-return sequences (step 2 or 3)",sum(v[2] for v in C.values()))
    for i,(_,v) in enumerate(sorted(C.items(),key=lambda x:repr(x[0])),1):
        print(i, "multisets=",v[0], "orders=",v[1], "vacuum=",v[2], "sample=",v[3])
