#!/usr/bin/env python3
"""IV-60 pure-Python enumerator for four pair-edge weighted multigraphs."""
from itertools import combinations, combinations_with_replacement, permutations
from collections import Counter
import json, argparse

def canonical_component(vertices, weighted_edges):
    vertices=tuple(sorted(vertices)); best=None
    for perm in permutations(range(len(vertices))):
        mapping=dict(zip(vertices,perm))
        enc=tuple(sorted((min(mapping[u],mapping[v]),max(mapping[u],mapping[v]),w)
                         for (u,v),w in weighted_edges.items()))
        if best is None or enc<best: best=enc
    return (len(vertices),best)

def canonical_graph(weighted):
    adj={}
    for (u,v),w in weighted.items():
        adj.setdefault(u,set()).add(v); adj.setdefault(v,set()).add(u)
    unseen=set(adj); comps=[]
    while unseen:
        root=min(unseen); stack=[root]; c=set()
        while stack:
            x=stack.pop()
            if x in c: continue
            c.add(x); unseen.discard(x); stack.extend(adj[x]-c)
        ce={e:w for e,w in weighted.items() if e[0] in c and e[1] in c}
        comps.append(canonical_component(c,ce))
    return tuple(sorted(comps))

def endpoint_flips(weighted):
    deg=Counter()
    for (u,v),m in weighted.items(): deg[u]+=m; deg[v]+=m
    return tuple(sorted(v for v,d in deg.items() if d%2))

def vacuum_intermediate(seq):
    s=set()
    for k,e in enumerate(seq,1):
        s.symmetric_difference_update(e)
        if k in (2,3) and not s: return True
    return False

def enumerate_all(n_vertices=8,n_operations=4):
    edges=list(combinations(range(n_vertices),2)); classes=Counter(); examples={}
    endpoint_hist=Counter(); multisets=0; ordered=0; vacuum=0
    for ms in combinations_with_replacement(edges,n_operations):
        multisets+=1; w=Counter(ms); sig=canonical_graph(w)
        classes[sig]+=1; examples.setdefault(sig,ms)
        endpoint_hist[len(endpoint_flips(w))]+=1
        orders=set(permutations(ms)); ordered+=len(orders)
        vacuum+=sum(vacuum_intermediate(seq) for seq in orders)
    return {'vertex_pool_size':n_vertices,'edge_pool_size':len(edges),
      'edge_operations':n_operations,'labeled_edge_multisets':multisets,
      'unlabeled_weighted_support_classes':len(classes),
      'unique_ordered_sequences':ordered,'ordered_sequences_with_vacuum_intermediate':vacuum,
      'endpoint_flip_count_distribution_over_multisets':dict(sorted(endpoint_hist.items())),
      'classes':[{'canonical_signature':repr(sig),'represented_multisets':classes[sig],
        'sample_multiset':[list(e) for e in examples[sig]]}
        for sig in sorted(classes,key=repr)]}

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--vertices',type=int,default=8)
    p.add_argument('--operations',type=int,default=4); p.add_argument('--output',default='iv60_summary.json')
    a=p.parse_args(); result=enumerate_all(a.vertices,a.operations)
    with open(a.output,'w',encoding='utf-8') as f: json.dump(result,f,ensure_ascii=False,indent=2)
    print(json.dumps({k:v for k,v in result.items() if k!='classes'},indent=2))
