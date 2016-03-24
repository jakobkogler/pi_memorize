# pi_memorize

[![Code Issues](https://www.quantifiedcode.com/api/v1/project/45a7b87eafdd4ea98892a24ce969746a/badge.svg)](https://www.quantifiedcode.com/app/project/45a7b87eafdd4ea98892a24ce969746a)

A command-line program for memorizing pi. `compute_pi.py` computes the digits
of pi and `convert_to_major.py` converts these digits to words using the
major system.

## Requirements ##

* Python 2.7 / 3.4

## Usage ##

```
> python compute_pi.py --precision 10
3.1415926535
> echo 141592653| python convert_to_major.py major1000.csv
Index    1, Digits 141: Torte
Index    4, Digits 592: Lappen, Lippe
Index    7, Digits 653: Schlamm
```

## Licence ##

Copyright (C) 2016 Jakob Kogler, [MIT License](https://github.com/jakobkogler/pi_memorize/blob/master/LICENSE.txt)
