#!/usr/bin/env python3
"""IV-63: classify vacuum-return four-edge sequences by prefix and repetition."""
from itertools import combinations, combinations_with_replacement, permutations
from collections import Counter
import json, argparse

def classify(n=8,k=4):
    edges=list(combinations(range(n),2)); total=0
    vacuum=Counter(); by_edge_repeat=Counter(); by_state_repeat=Counter(); detailed=Counter()
    for multiset in combinations_with_replacement(edges,k):
        for seq in set(permutations(multiset)):
            total+=1; flips=set(); states=[]
            for edge in seq:
                flips.symmetric_difference_update(edge); states.append(frozenset(flips))
            v2=(len(states[1])==0); v3=(len(states[2])==0)
            if not (v2 or v3): continue
            category='step2' if v2 else 'step3'
            # In this four-edge enumeration these prefix-vacuum categories are disjoint.
            repeated_edges=k-len(set(seq))
            repeated_states=k-len(set(states))
            vacuum[category]+=1
            by_edge_repeat[category,repeated_edges]+=1
            by_state_repeat[category,repeated_states]+=1
            # prefix edge count, full-sequence repeated edge count, repeated states
            detailed[category,len(set(seq)),repeated_edges,repeated_states]+=1
    return {'vertex_pool_size':n,'edge_pool_size':len(edges),'operations':k,
      'ordered_sequences_total':total,'vacuum_prefix_counts':dict(vacuum),
      'edge_repeat_count_by_vacuum_category':{f'{cat}|{r}':v for (cat,r),v in sorted(by_edge_repeat.items())},
      'repeated_intermediate_state_count_by_category':{f'{cat}|{r}':v for (cat,r),v in sorted(by_state_repeat.items())},
      'detailed_counts':{f'{cat}|distinct_edges={d}|edge_repeats={er}|state_repeats={sr}':v
         for (cat,d,er,sr),v in sorted(detailed.items())}}

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--vertices',type=int,default=8); p.add_argument('--operations',type=int,default=4); p.add_argument('--output',default='iv63_vacuum_path_classification.json'); a=p.parse_args()
    r=classify(a.vertices,a.operations)
    with open(a.output,'w',encoding='utf-8') as f: json.dump(r,f,indent=2,ensure_ascii=False)
    print(json.dumps(r,indent=2,ensure_ascii=False))
