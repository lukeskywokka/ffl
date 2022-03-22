# Intro
When the 2021 fantasy football season ended I wasn't ready to say goodbye.  I decided to do a few different things:
- Standard Deviation of WRs and TEs
- Points Per Touch
- Draft Kings best NFC/AFC championship lineup given current Playoff PPG
- Best Auction Draft combos
- Best Snake Draft given 2021 players ranked by PPG


# Git protocol
- git add -A
- git commit -m "minor touchup"
- git push -u origin main


# 2020 auction draft revelations
- 3 WR 47 and I get tyreek, stefon, will fuller at 59 ppg avg rank = 24.6
- 3 RBs spending 75 -> 150 ppg goes from 57 -> 67: 1 baller: Kamara, Montgomery, Gibson (rook)
- 4 WRs spending 50 -> 150 goes from 76-86 ppg: baller, journeyman/newcomer (fuller), newcomer (diggs), rook
- 2 QBs: newcomer, vet for $20.  48 ppg at $20 vs 52ppg at $99
- 1 TE: newcomer/unknown Darren Waller (17ppg) for $11 vs Travis Kelce (20.8ppg) for $45
- 3 qbs: rook, journeyman, avg vet: $3 for 63ppg.  $99 for 76 ppg.  $19 for 71ppg: newcomer, rook, vet
- 4rbs: $25: 60ppg, rook, rook, 2nd year, vet....$50: 64 ppg, kinda baller, 2nd year, vet, rook
- 4 wrs: spending $20 gets you 3 relative unknowns and a vet at 72ppg
- 6 wrs: spending $60 gets stud, newcomer, newcomer, rook, rook, rook OR stud, studly vet, newcomer, newcomer, rook, rook at 109ppg
- 6 rbs: spending $95 gets, stud, rook, 2nd year, vet, rook, rook OR instead of rooks, backups at 96ppg
- 6rbs: at $105 gets 101 ppg
- 6wrs: at $80 gets 114ppg


## 2021: 
### WR: 6 for 60
- baller: deebo, tyreek, kupp, davante, JJ, Diggs, DK, Godwin, Ridley
- in between: diontae Johnson
- newcomer: Renfrow, Waddle, Devonta? Rondale or Elijah Moore? Toney
- rook: metchie?

### RBS 6 for $95
- baller: can we get cmac for cheap? Ekeler, Najee
- vet: chubb, conner, Lenny, Jacobs, Singletary, Swift, Akers, Pollard, Montgomery??, Saquon??
- newcomer: javonte, michael carter jr, Elijah Mitchell, Rhamondre, Penny, Harris, helaire
- rook: watch draft

### Qbs: 20 for 2 or 3
- baller: Mahomes, Allen, Jackson, Murray, burrow, Stafford
- vet: Rodgers, Russ, Carr
- avg vet: Cousins, Jimmy G, Matt Ryan, Tua
- newcomer: Zach Wilson, Trevor Lawrence
- rook: trey, Malik
- bleh: Daniel Jones (brian daboll), goff


### TE:15
- baller: waller, kelce, kittle, Andrews
- avg: Hockenson, Fant, Henry, Gesicki
- newcomer: PITTS
- Pat Freiermuth

## Things I've Learned:
- Trying to generate combos in the order of trillions is basically impossible. What this means is that we need to split the data into chunks to process ie WRS, RBS, TEs, QBs.
- Don't overwork your PC.  I was trying to run combos of 180 choose 7 and my PC got too hot and had to shut down.
- Use JIT with pypy for faster python execution: https://doc.pypy.org/en/latest/install.html


## Future Ideas
- Make player cards and graphics out of the data
- Standard Deviation for QBs and RBs
- Convert to simple web app to tinker with adjustable values
- Multiprocessing using lists