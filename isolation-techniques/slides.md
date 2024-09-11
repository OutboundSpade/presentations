---
marp: true
theme: default
paginate: true
footer: "(C) 2023, Ray Steen"
author: "Ray Steen"
---
<style>section  { justify-content: start; }</style>
<style scoped>section  { justify-content: center; }</style>

<!-- class: invert -->
<style scoped>section  { justify-content: center; }</style>

# <!-- min-width -->  Software Isolation Techniques for Limiting Attack Surfaces
![bg width:500px right](assets/isolation.png)

## Ray Steen

---
<style scoped>section  { justify-content: center;align-items:center; }</style>

# Problem

---
<style scoped>section  { justify-content: center; align-items:center;} h1 {text-align: center;}</style>

# You all write shitty code
## *- Professor Bernstein*

![bg width:500px right](assets/bernstdh.png)

---

![bg](assets/log4j2.png)

---
<style scoped>section  { justify-content: center;align-items:center; }</style>

# How can we mitigate this?

---

![bg fit](assets/isolation.png)

---
<style scoped>section  { justify-content: center;align-items:center; }</style>

# Technique 1
## Virtual Machines

---

![bg fit](assets/vm.png)

---

# Virtual Machines - Advantages

- ### Works out of the box
- ### Any OS
- ### Strong isolation

---

# Virtual Machines - Disadvantages

- ### Large resource usage
- ### Performance overhead
- ### OS maintenance

---

<style scoped>section  { justify-content: center;align-items:center; }</style>

# Technique 2
## Containers

---

![bg fit](assets/docker-arch.png)

---

# Containers - Advantages

- ### Resource efficient
- ### Very portable
- ### Fast startup times
- ### No performance overhead

---

# Containers - Disadvantages

- ### Primarily linux only
- ### Not optimal from some applications
- ### Moderate isolation

---


<style scoped>section  { justify-content: center;align-items:center; }</style>

# Technique 3
## WASM

---

![bg fit](assets/wasm.jpg)

---

# WASM - Advantages

- ### Very portable
- ### Fast startup times
- ### Runs in the browser
- ### Strong isolation

---

# WASM - Disadvantages

- ### Pre-built or source code required
- ### No official standard interface
- ### Performance overhead

---

![bg fit](assets/happy_bern.jpg)

---