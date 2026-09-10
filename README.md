# PyGit - A Simple Git Clone in Python

> **Watch the full tutorial on YouTube!**  
> https://youtu.be/g2cfjDENSyw

---

## 📖 What is PyGit?

PyGit is a **Python implementation of Git** that demonstrates the core concepts and internals of version control systems. This project is for educational purposes to understand how Git works under the hood by implementing the fundamental data structures and operations.

## Core Components

### 1. **GitObject Class**

- Base class for all Git objects (Blob, Tree, Commit)
- Handles serialization/deserialization with zlib compression
- Generates SHA-1 hashes for object identification (real Git uses SHA-256 nowadays)