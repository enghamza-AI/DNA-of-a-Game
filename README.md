# DNA-of-a-Game
We represent a game using numbers - This project shows the concept that Numbers do represent data.

# Project 2 — DNA of a Game

## Overview

This project represents a video game as a **vector of traits** and identifies its **strongest trait**.  

It is my second foundational AI systems project, where I implement everything **from scratch without any libraries**, helping me understand how AI represents and interprets structured data.

EDIT : I also made it to find the weakest trait - I used a seperate for loop to do that (:
The key insight:  

> **Vector = description, not just numbers.**

---

## Concept

A game can be described by multiple traits:

- Violence
- Story
- Exploration
- Difficulty

Each trait is represented as a number (0–1) indicating its intensity.  

Example vector:

[0.2, 0.9, 0.4, 0.6]


Here, `Story` is the strongest trait.

---

## How It Works

### Step 1 — Create Traits and Vector

- `traits` stores human-readable trait names.
- `game_vector` stores numerical values corresponding to each trait.

### Step 2 — Find Strongest Trait

- Initialize with the first trait as strongest.
- Loop through the vector.
- Update the strongest trait when a higher value is found.

This is equivalent to the **argmax operation** in AI:


Here, `Story` is the strongest trait.

---

## How It Works

### Step 1 — Create Traits and Vector

- `traits` stores human-readable trait names.
- `game_vector` stores numerical values corresponding to each trait.

### Step 2 — Find Strongest Trait

- Initialize with the first trait as strongest.
- Loop through the vector.
- Update the strongest trait when a higher value is found.

This is equivalent to the **argmax operation** in AI:

index of highest value = strongest trait


### Step 3 — Output

- Print the strongest trait and its value.

---

## Example Output

Game Vector: [0.2, 0.9, 0.4, 0.6]
Strongest trait is: Story
Value: 0.9

weakest trait is: violence
value: 0.2


---

## AI Concepts Learned

- **Vectors as representations**: Each dimension encodes a concept.
- **Index mapping**: Translating numeric positions to meaning.
- **Argmax operation**: Finding the strongest signal.
- **Feature representation**: Core of embeddings and recommendation systems.

---

## Why This Project Matters

Even simple vectors encode **identity and meaning**.  

Applications in real AI systems:

- Content recommendation (Netflix, Spotify)
- Player behavior analytics (Steam, Xbox)
- Game design profiling
- Personality and preference modeling

By practicing vector representation and analysis, you understand how AI **encodes and interprets information** before any complex model exists.

---

## Future Improvements

- Identify the **weakest trait** as well. (ALREADY DID)
- Compare two game vectors to find similarity (introduces distance metrics).
- Build a **player profile vector** for personalized recommendations.
- Visualize game vectors in a radar/spider chart for better understanding.

---

## Goal

This project is part of my journey to become an **AI Systems Engineer**, learning how to convert **real-world properties into structured vectors** and extract meaningful insights.


