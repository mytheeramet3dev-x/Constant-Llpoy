#!/usr/bin/env python3
"""IV-62 exhaustive denominator ledger for four pair-edge operations on 8 vertices."""
from itertools import combinations, combinations_with_replacement, permutations
from collections import Counter
import json, argparse

def compute(n=8, k=4):
    edges=list(combinations(range(n),2))
    step_hist=[Counter() for _ in range(k-1)]
    zero_step=[0]*(k-1)
    total=0; nonzero_all=0; zero_any=0; gap_triples=Counter()
    for multiset in combinations_with_replacement(edges,k):
        for seq in set(permutations(multiset)):
            total+=1; flips=set(); gaps=[]
            for i,e in enumerate(seq[:k-1]):
                flips.symmetric_difference_update(e)
                gap=2*len(flips) # Delta E / h
                gaps.append(gap)
                step_hist[i][gap]+=1
                if gap==0: zero_step[i]+=1
            if any(g==0 for g in gaps): zero_any+=1
            else:
                nonzero_all+=1
                gap_triples[tuple(gaps)]+=1
    return {
      "vertex_pool_size":n,"edge_pool_size":len(edges),"edge_operations":k,
      "ordered_sequences":total,"all_intermediate_denominators_nonzero":nonzero_all,
      "at_least_one_vacuum_intermediate":zero_any,
      "gap_histograms_by_intermediate_step_deltaE_over_h":[dict(sorted(c.items())) for c in step_hist],
      "zero_gap_counts_by_step":zero_step,
      "nonzero_gap_tuple_histogram_deltaE_over_h":{str(list(t)):v for t,v in sorted(gap_triples.items())},
      "note":"Gap DeltaE=2h|S|; values in histograms are DeltaE/h. Zero-gap paths flagged only, not corrected/subtracted."
    }
if __name__=="__main__":
    p=argparse.ArgumentParser(); p.add_argument('--vertices',type=int,default=8); p.add_argument('--operations',type=int,default=4); p.add_argument('--output',default='iv62_denominator_ledger.json'); a=p.parse_args()
    result=compute(a.vertices,a.operations)
    with open(a.output,'w',encoding='utf-8') as f: json.dump(result,f,indent=2,ensure_ascii=False)
    print(json.dumps(result,indent=2,ensure_ascii=False))
