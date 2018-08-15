#Fading Suns 2E dice roller

Script to roll dice for the 1st and 2nd editions of the roleplaying game.

## How to use

Make the script executable:
```shell
chmod u+x roll
```

For a d20 roll the format is: ./roll d20 difficulty
```shell
./roll d20 15
Roll type: d20 Dice number: 1 Difficulty: 15
 14  -->  +4 VP / +4 dice

./roll d20 8
Roll type: d20 / Dice number: 1 / Difficulty: 8
 12  -->  FAIL 

./roll d20 27
Roll type: d20 / Dice number: 1 / Difficulty: 27
 15  -->  +5 VP / +8 dice
```

For a d6 roll (difficulty 4 by default): ./roll d6 number_of_dice
```shell
./roll d6 7
Roll type: d6 / Dice number: 7 / Difficulty: 4
 [1, 1, 2, 3, 4]  [6, 6]  -->  5
```

Other options:
```
    -d, --difficulty, difficulty of the roll, particularly useful for d6.
                      ./roll d6 5 -d 3
```

Examples:
```shell
./roll d20 15
./roll d20 24
./roll d6 6
./roll d6 7 -d 3
```

## Container use

```shell
docker build -t fading_suns_dice .
docker run --rm -it fading_suns_dice
```

## Run the tests

```shell
python3 test_roll.py
```

Or if you install [coverage.py](https://coverage.readthedocs.io/en/latest/):
```shell
coverage run test_roll.py
coverage report -m
coverage html
open htmlcov/index.html
```
