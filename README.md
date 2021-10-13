# bridge_analyser
Analyses which point ranges score how much tricks with a double dummy solver.

Requires python package ddstable.
```
python -m pip install ddstable
```

Running the dds-analysis.py creates a results.json and games.pbn file.
The results.json file is a dict. If dumped into the variable 'data', then
```
data[trump][points][fitsize][smallersize][tricks]
```
represents number games where, the team had 'points' in HCP, 'fitsize' number of cards in 'trump',
'smallersize' number of trumps in the shorter hand, and double dummy solver reported 'tricks' number of tricks taken.
For No trumps,
```
data['NT'][points][stopper][tricks]
```
'stopper' is 0 or 1 depending on all 4 four suits are stopped or not.

The tabulate.py file tabulates the data from results.json file.

usage: tabulate.py [-h] [-c] [-nt] [-bl BL] [-fit FIT] [-subfit SUBFIT]

```
optional arguments:
  -h, --help           show this help message and exit
  -c, -commulative     Shows commulative probablities instead.
  -nt, -NT             Solves for No Trump contract. Omit this for trump
                       contracts.
  -bl BL, -blocker BL  In NT contracts, whether all suits have blockers.
                       -bl 0: missing blockers
                       -bl 1:blockers present
                       -bl 2:blocker status not investigated.
  -fit FIT             Specifies the fit size.
  -subfit SUBFIT       Specifies the number of trumps in the shorter hand.
                       Omit this to consider all fit types.
```
