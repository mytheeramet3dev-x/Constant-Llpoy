#!/usr/bin/env python3
"""IV-69 exhaustive four-edge sequence engine (finite graph audit).

Enumerates ordered edge tuples; tracks flip sets as bitmasks; computes vacuum-return,
intermediate gaps, and reduced-resolvent denominator/sign data only when all intermediate
flip sets are nonempty. This is combinatorial bookkeeping, not an energy-coefficient
proof.
"""
from __future__ import annotations
import itertools, json, argparse
from collections import Counter
from pathlib import Path

def run(n_vertices: int, edges: list[tuple[int,int]]):
    normalized=[]
    for a,b in edges:
        if a==b: raise ValueError("self-loops not supported")
        if not (0 <= a < n_vertices and 0 <= b < n_vertices): raise ValueError("vertex out of range")
        normalized.append(tuple(sorted((a,b)))))
    if len(set(normalized)) != len(normalized): raise ValueError("duplicate edge definitions")
    masks=[(1<<a)|(1<<b) for a,b in normalized]
    total=len(edges)**4
    vacuum_count=0
    reducible_count=0
    irreducible_vacuum_count=0
    endpoint_hist=Counter()
    gap_hist=[Counter(),Counter(),Counter()]
    ledger=[]
    for idxs in itertools.product(range(len(edges)), repeat=4):
        flips=[]
        state=0
        for idx in idxs:
            state ^= masks[idx]
            flips.append(state)
        s1,s2,s3,s4=flips
        vac=(s4==0)
        reducible=(s2==0 or s3==0)
        irreducible=(s1!=0 and s2!=0 and s3!=0)
        if vac: vacuum_count+=1
        if vac and reducible: reducible_count+=1
        if vac and irreducible: irreducible_vacuum_count+=1
        endpoint_hist[s4.bit_count()]+=1
        gaps=[]
        for k,s in enumerate((s1,s2,s3)):
            if s==0:
                gaps.append(None)
            else:
                gap=2*s.bit_count() # in units of h
                gaps.append(gap)
                gap_hist[k][gap]+=1
        denom_product=None
        resolvent_sign=None
        if irreducible:
            denom_product=1
            resolvent_sign=-1 # three R0 factors
            for s in (s1,s2,s3):
                denom_product*=2*s.bit_count()
        ledger.append({"edge_indices":idxs,"flip_masks":flips,"flip_sizes":[s.bit_count() for s in flips],"gaps_over_h":gaps,"vacuum_return":vac,"reducible":reducible,"irreducible_chain":irreducible,"resolvent_denominator_product_over_h3":denom_product,"resolvent_sign_for_three_factors":resolvent_sign})
    return {"vertices":n_vertices,"edges":[list(e) for e in normalized],"edge_count":len(edges),"ordered_tuple_count":total,"vacuum_return_count":vacuum_count,"vacuum_return_reducible_count":reducible_count,"vacuum_return_irreducible_count":irreducible_vacuum_count,"endpoint_flip_size_histogram":dict(sorted(endpoint_hist.items())),"intermediate_gap_over_h_histograms":[dict(sorted(c.items())) for c in gap_hist],"ledger":ledger}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--vertices",type=int,default=4)
    p.add_argument("--edges",default="0-1,1-2,2-3,3-0")
    p.add_argument("--out",default="IV69_ENGINE_OUTPUT.json")
    a=p.parse_args()
    edges=[tuple(map(int,x.split("-"))) for x in a.edges.split(",") if x.strip()]
    result=run(a.vertices,edges)
    Path(a.out).write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:result[k] for k in ("vertices","edge_count","ordered_tuple_count","vacuum_return_count","vacuum_return_reducible_count","vacuum_return_irreducible_count")},indent=2))
if __name__=="__main__":
    main()
