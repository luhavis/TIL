# TroubleShooting
max virtual memory areas vm.max_map_count [65530] is too low, increase to at least [262144]

```bash
sudo vi /etc/sysctl.conf
```

```bash
vm.max_map_count=262144
```

```bash
sudo sysctl -p
```




