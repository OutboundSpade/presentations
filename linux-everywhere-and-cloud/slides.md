---
marp: true
theme: default
paginate: true
footer: "(C) 2025, Ray Steen"
author: "Ray Steen"
class: lead
---
<style>
/* keep slides content a bit higher for quick delivery */
section { justify-content: start; }
</style>

<!-- class: invert -->
# Linux & Cloud
### Why the internet runs on penguins 🐧


---
# Linux is Everywhere

- Powers most servers and cloud VMs
- Runs on everything from Raspberry Pi to supercomputers
- Built for multitasking, networking, containers, and automation

<!-- Takeaway: If it’s in the cloud, it’s probably Linux. -->

---
# Market Snapshot

- **All TOP500 supercomputers run Linux**
- **Most public cloud workloads** run on Linux (VMs and containers)
- **Android** (Linux-based) dominates mobile OS usage

*Reason to care:* skills here translate directly to cloud jobs.

---
# Why Linux dominates the cloud

- **Open & modular**: choose minimal images, swap components
- **Kernel superpowers**: cgroups, namespaces → containers
- **Automation-first**: SSH, systemd, cloud‑init, Ansible
- **Ecosystem**: Kubernetes, Docker, Terraform, eBPF, WireGuard

---
# Containers & Kubernetes

- A **container** = process + filesystem + isolation (no full VM)
- **Kubernetes** schedules containers on Linux nodes
- Images are **tiny** (e.g., Alpine, distroless) → fast, cheap

> Linux features (cgroups, namespaces, overlayfs) make this possible.

---
# Common cloud distros

- **Ubuntu Server** (sane defaults, huge ecosystem)
- **Debian** (stable, minimal)
- **Amazon Linux** (AWS-tuned)
- **Fedora CoreOS** (immutable, great for clusters)

*Pick minimal where you can; add only what you need.*

---
<!-- class: invert -->
# DEMO TIME
Because demos *always* work
<!-- # LIVE DEMO — DigitalOcean

**Goal:** Prove how fast Linux gets from zero → serving traffic.

1. Create a droplet, install nginx, serve a page
2. Hit it from your laptop
3. Destroy it (leave no bill 🫡)


*If Wi‑Fi is flaky: show a screenshot or run a pre-recorded curl.* -->

---
# Useful one‑liners

```bash
# Quick system facts
uname -a && lsb_release -a || cat /etc/os-release

# Who/where/what
whoami && hostname -I && df -h && free -m

# Firewall open 80 (Ubuntu with ufw)
sudo ufw allow 80/tcp && sudo ufw enable
```

<!-- ---
# Security & Ops in 15s

- **SSH keys** > passwords; rotate & restrict
- **Least privilege** (sudoers, service users)
- **Patching** (unattended-upgrades)
- **Observability**: journald, systemd units, `top`, `htop`, `journalctl -u <svc>` -->

---
# Key takeaways

- Linux is the **language of the cloud**
- Learn the **basics + containers** → unlock Kubernetes
- Practice with **cheap VMs** & tear them down after

<!-- > Next step: turn this demo into a script you can reuse in interviews. -->

---
<!-- class: invert -->
# Q&A

*Ask me about containers, kubernetes, or other cloud things*

