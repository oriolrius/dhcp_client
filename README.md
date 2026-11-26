<div align="center">

# 📡 dhcp_client

**Shout into the LAN, see who answers.**

A tiny [scapy](https://scapy.net/) DHCP probe: it broadcasts a `DHCPDISCOVER`
and dumps every `DHCPOFFER` it hears — lease, router, DNS, every option, byte by byte.

![Python](https://img.shields.io/badge/python-3.13+-3776AB?logo=python&logoColor=white)
![scapy](https://img.shields.io/badge/scapy-2.6+-2E7D32)
![uv](https://img.shields.io/badge/managed%20with-uv-DE5FE9)

</div>

---

## Why

- 🕵️ **Find rogue DHCP servers** — more than one offer means more than one server.
- 🔍 **See the real options** a server hands out, without touching your network config.
- 🧪 **Debug DHCP** on a lab network, a VLAN or a fresh router.

It never takes a lease: it only asks and listens.

## Quick start

```bash
git clone https://github.com/oriolrius/dhcp_client.git
cd dhcp_client
uv sync
sudo env "PATH=$PATH" uv run dhcp_client_v2.py
```

> [!NOTE]
> Raw sockets need root, hence `sudo`. The interface is `eth0` — edit
> `interface = "eth0"` in the script to use another one.

## The two scripts

| Script | How it works |
|---|---|
| `dhcp_client_v2.py` | ✅ Recommended. Starts the sniffer in a thread **first**, then sends the Discover, so fast servers are not missed. |
| `dhcp_client_dry.py` | The original: sends the Discover, then sniffs. Simple, but can miss a quick reply. |

Both listen for 30 seconds and print each Offer with scapy's `packet.show()`.

## What you get

```text
Sent DHCP Discover packet
Received DHCP Offer:
###[ Ethernet ]###
  ...
###[ BOOTP ]###
     op        = BOOTREPLY
     yiaddr    = 192.168.1.57
     siaddr    = 192.168.1.1
###[ DHCP options ]###
     options   = [message-type=offer server_id=192.168.1.1 lease_time=86400
                  subnet_mask=255.255.255.0 router=192.168.1.1
                  name_server=192.168.1.1 end]
```

## ⚠️ Heads-up

This sends **real broadcast packets** on your network. Use it on networks you own
or are allowed to test.

## Author

Made by [Oriol Rius](https://oriolrius.cat) — notes and write-ups at
[oriolrius.blog](https://oriolrius.blog).
