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
- goods.txt
- bads.txt

## tips:
- auto-increment resolve delay
- catch KeyboardInterrupt and save all results
