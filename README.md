## Example:
```
➜  registrar-checker git:(main) ✗ python3 main.py domains-from-urlhaus_uniq-sort.txt
[Threads] press Enter(6) or type 32 :>
[Registrar] press Enter(RU-CENTER) or type REG-RU :>

[!] 771 elements loaded
[!] Wait starting threads...
[%] Scanned: 6 | Queue size: 757 | Active threads: 8
[%] Scanned: 17 | Queue size: 746 | Active threads: 8
[%] Scanned: 43 | Queue size: 720 | Active threads: 8
... [EDITED] ...
[%] Scanned: 749 | Queue size: 14 | Active threads: 8
[%] Scanned: 757 | Queue size: 6 | Active threads: 8

[+] Success domains: 7
```

## Output:
- success.txt
- errors.txt

## tips:
- auto-increment resolve delay
- catch KeyboardInterrupt and save all results

## ccTLD & TLD support list
~~~
ccTLD
- uz
- ac.uk
- ar
- at
- be
- br
- ca
- co
- co.jp
- com.au
- cl
- cn
- cz
- de
- eu
- fr
- it
- ir
- jp
- kr
- lv
- lt
- mx
- nz
- pl
- ru
- uk
- us
- mx
- br
- sh
- id
- tv
- cc
- nyc
- pw
- рф (xn--p1ai)
- in
- ua

TLD
- download
- biz
- edu
- education
- com
- download
- info
- me
- mobi
- name
- net
- ninja
- nyc
- online
- org
- io
- xyz
- tel
- online
- wiki
- press
- pharmacy
- rest
- security
- site
- space
- store
- tech
- tel
- theatre
- tickets
- video
- website
- club
- work
- bank
- ca
- mu
- rw
~~~
