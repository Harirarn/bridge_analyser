import itertools
import json
import argparse

datfile = 'results.json'
with open(datfile) as file:
    data = json.load(file)

def percent(n):
    ret = f"{100*n:5.2f}%"
    if len(ret)>6: return "100.0%"
    else: return ret

def ptwise_add(a, b):
    if type(a) == list:
        return [ptwise_add(i, j) for i, j in zip(a, b)]
    else:
        return a + b

def ptwise_sum(a):
    if len(a) == 0: return 0
    else: b = a[0]
    for c in a[1:]:
        b = ptwise_add(b, c)
    return b

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=f'Tabulates results from {datfile}')
    parser.add_argument('-c', '-commulative', action = 'store_true', help="Shows commulative probablities instead.")
    parser.add_argument('-nt', '-NT', action = 'store_true', help="Solves for No Trump contract. Omit this for trump contracts.")
    parser.add_argument('-bl', '-blocker', action = 'store', type=int, default=2, help="In NT contracts, whether all suits have blockers.\n-bl 0: missing blockers\n-bl 1:blockers present\n-bl 2:blocker status not investigated.")
    parser.add_argument('-fit', action='store', type=int, default=8, help="Specifies the fit size.")
    parser.add_argument('-subfit', action='store', help="Specifies the number of trumps in the shorter hand. Omit this to consider all fit types.")
    args = parser.parse_args()
    #args = parser.parse_args("-nt -bl 0 -fit 8 -subfit 4".split())
    commulative = args.c
    NT_data = args.nt
    fitsize = args.fit
    subfit = args.subfit
    if subfit is not None: subfit = int(subfit)
    blocker = args.bl
    NT = data['NT']
    trumps = ptwise_sum((data['C'], data['D'], data['H'], data['S']))
    if NT_data: print('NT. Blockers',['absent', 'present', 'unknown'][blocker])
    elif subfit is None: print(f'Trumps, {fitsize} fit')
    else: print(f'Trumps, {fitsize-subfit}-{subfit} fit')
    print('HCP'+''.join(f"{i:>7d}" for i in range(int(commulative),14))+' Games')
    for hcp in range(15, 36):
        print(f"{hcp:>2} ", end='')
        if NT_data:
            sc = NT[hcp]
            if blocker == 0: combined = [a for a,b in zip(*sc)]
            elif blocker == 1: combined = [b for a,b in zip(*sc)]
            else: combined = [a+b for a,b in zip(*sc)]
        else:
            sc = trumps[hcp]
            if subfit is None:
                combined = [ptwise_sum(j) for j in sc][fitsize]
            else:
                combined = sc[fitsize][subfit]
        total = sum(combined)
        commul = list(itertools.accumulate(combined))
        for tricks in range(14-int(commulative)):
            if total == 0:
                print(" ----- ", end='')
            elif commulative:
                print(f" {percent(1-commul[tricks]/total)}", end='')
            else:
                print(f" {percent(combined[tricks]/total)}", end='')

            
        print(f"{total:6d}")
    
    
