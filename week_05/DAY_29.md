Here’s the Day 29 revision README — kept simple, focused on what you need to remember later rather than full theory.

# Day 29 — Semantic Similarity + Cosine Similarity

## What I Learned

Semantic similarity means measuring how similar two texts are in meaning, even when they use different words.

Example:
"How do I containerize an application?"
"How can I package my app using Docker?"
These have similar meaning, so they have high semantic similarity.

## Why Keyword Matching Is Not Enough

Keyword matching mainly looks for the same words.

Semantic similarity looks for similar meaning.

Example:
"containerize an application" and "package an app using Docker" may not share the exact keywords, but their meanings are related.

## Vector Similarity

Vector similarity measures how similar two vectors are.

In AI, text is converted into embeddings, and those embeddings become vectors.

Similar meaning → similar vector representation → higher similarity.

## Query Embedding

A query embedding is the vector representation of the user's question.

Example:

User question → Embedding model → Query vector

The query vector can then be compared with stored document vectors.

## Cosine Similarity

Cosine similarity is a method used to compare two vectors by looking at the direction they point.

Similar direction → High cosine similarity

Different direction → Low cosine similarity

I do not need to memorize the mathematical formula yet.

## Why Cosine Similarity Is Useful

A RAG system may have hundreds or thousands of document vectors.

Cosine similarity helps compare the user's query vector with those stored vectors and calculate similarity scores.

Example:

Docker document → 0.92
Containers guide → 0.89
Python document → 0.31
SQL document → 0.18

The system can use these scores to rank and retrieve the most relevant chunks.

## Where It Is Used in RAG

User question → Create query embedding → Query vector → Similarity search → Retrieve relevant chunks → Send chunks as context to LLM → Generate answer

## Important Distinction

Embedding → Converts text into a vector.

Query embedding → Converts the user's question into a vector.

Vector similarity → Measures similarity between vectors.

Cosine similarity → One method for measuring vector similarity.

Retrieval → Selects relevant document chunks based on similarity.

LLM → Uses the retrieved chunks as context to generate the answer.

## Core Idea

Similar meaning → Similar vector direction → Higher cosine similarity → More likely to be relevant → Retrieve as context → Send to LLM

## One-Line Revision

Cosine similarity helps a RAG system find which stored document vectors are most similar to the user's query vector, so relevant context can be retrieved for the LLM.

## Day 29 Complete

Semantic similarity → Vector similarity → Query embeddings → Cosine similarity → Similarity search → Relevant context → LLM
