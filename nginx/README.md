### Build

```
scripts/build image=nginx
```

### Start Nginx OSv

```
scripts/run.py
```

This currently fails due to failure to lookup symbol ``sigsuspend``:

```
root@ubuntu:~/osv# scripts/run.py -d
OSv v0.24-101-gc0d25a9
eth0: 192.168.122.15
/tools/nginx.so: failed looking up symbol sigsuspend

[backtrace]
0x000000000022d44f <abort(char const*, ...)+270>
0x0000000000401a46 <elf::object::symbol(unsigned int)+396>
0x000000000040215a <elf::object::resolve_pltgot(unsigned int)+236>
0x000000000040636f <elf_resolve_pltgot+130>
0x000000000048ab15 <???+4762389>
0x0000000000000000 <???+0>
```

Troubleshooting:
```
root@ubuntu:~/osv# scripts/check-libcfunc-avail.sh debug /root/osv/apps/nginx/out/nginx.so 
sigsuspend not found
openat64 not found
root@ubuntu:~/osv# 
```

[Issue 747](https://github.com/cloudius-systems/osv/issues/747) blocks progress.
