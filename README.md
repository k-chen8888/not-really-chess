[TABLE OF CONTENTS]
1.0.0 - Introduction 
2.0.0 - 
3.0.0 - Gameplay
	3.1.0 - Turns
		3.1.1 - State-based Player Actions
		3.1.2 - Movement
		3.1.3 - Precombat Actions
		3.1.4 - Combat
		3.1.5 - State-based Cleanup
	3.2.0 - Keywords
		3.2.1 - 
		3.2.2 - 
		3.2.3 - 
		3.2.4 - 
		3.2.5 - 
		3.2.6 - 
		3.2.7 - 


[3.0.0 Gameplay]

Turns: Each turn takes place in 4 phases
1. State-based player actions
2. Movement
3. Precombat actions
4. Combat, damage
5. State-based cleanup

Keywords:
	Rush: Can do a 50% damage basic attack after movement
	Splash: Can do 25% attack damage to adjacent tiles
	Bounce: Can knock back by one tile
		If knocked back into something, deals fixed 10 damage to each 
	Critical: Small chance of doing 25% extra damage
	Random: Strikes a random tile within a range
	Deny: Forces all attacks during the turn to misfire, preventing damage to target and reflecting 50% damage
		Denying a deny does 50% strong attack damage to both pieces
	Counter: Take only 50% physical damage and reflect back the other 50%
		Countering a magic-based attack causes 25% additional damage
	Level: Reduce elevation of tile by 1
