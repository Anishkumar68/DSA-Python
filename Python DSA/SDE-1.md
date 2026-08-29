### Priority 1 — Python Core + OOP

**~1.5 hours**

We already started memory. Finish:

- Variables/references
- Mutable vs immutable
- Assignment/copy

- Shallow/deep copy
 
- `is` vs `==`
    
- Lists/dicts/sets/tuples
    
- Functions
    
- `*args`, `**kwargs`
    
- Default arguments
    
- Exception handling
    
- Iterators
    
- Generators
    
- Decorators
    
- Context managers
    
- OOP
    
- `classmethod` / `staticmethod`
    
- Inheritance
    
- Polymorphism
    
- MRO
    
- `super()`
    

This directly supports the JD's requirement for **excellent OOP, data structures and algorithms**.

---

### Priority 2 — API / Backend

**~1 hour**

This is probably the **most important section after Python** because the job specifically asks for Python API development and DRF/Flask/FastAPI.

We'll cover:

- REST
    
- HTTP methods
    
- Status codes
    
- GET/POST/PUT/PATCH/DELETE
    
- Request/response
    
- Headers
    
- Authentication vs authorization
    
- Middleware
    
- Validation
    
- Pagination
    
- Error handling
    
- Swagger/OpenAPI
    
- FastAPI basics
    
- API architecture
    

---

### Priority 3 — Concurrency

**~30–40 min**

Because the JD explicitly mentions multithreading, concurrent APIs and performance.

Only learn what is interview-relevant:

```text
Thread
Process
GIL
async/await
asyncio
I/O-bound
CPU-bound
threading vs multiprocessing
```

---

### Priority 4 — Database + Async Processing

**~30 min**

Know the fundamentals:

```text
SQL
JOIN
INDEX
TRANSACTION
ACID
SQL vs NoSQL
```

Then:

```text
Celery
RabbitMQ
Kafka
Background task
Worker
Message broker
```

These are explicitly listed in the JD.

---

### Priority 5 — DSA/Coding

**~30–40 min**

Don't attempt advanced LeetCode.

We will practice the patterns most likely to expose whether you can actually code:

- String manipulation
    
- List/dict problems
    
- Frequency counting
    
- Two sum
    
- Duplicate detection
    
- Anagram
    
- Stack
    
- Queue
    
- Linked list basics
    
- Sorting/searching
    
- Big-O
    

---

### Priority 6 — Your Resume/Projects

**Final 30–45 min**

This is **critical**.

The interviewer can look at your resume and ask:

> "Explain your project."

Then drill into:

- Why FastAPI?
    
- Why Redis?
    
- Why RAG?
    
- How does your API work?
    
- Database?
    
- Authentication?
    
- Error handling?
    
- Async processing?
    
- Deployment?
    
- Architecture?
    
- What did **you personally implement?**
    
- What was the hardest problem?
    
- How did you debug it?
    

We should prepare these based on your actual resume/project rather than inventing answers.

---

# How we'll work now

**Don't read everything first.**

I'll teach you in **small chunks**, exactly like we've been doing:

> **Concept → tiny example → interview answer → likely follow-up**

And occasionally I'll stop and ask:

> **"Interviewer: Explain X."**

You answer in your own words, and I'll correct you brutally where necessary.

### Our immediate sequence

**Memory → Core Python → OOP → Iterators/Generators → Decorators → API → Concurrency → DB/Celery → Coding → Resume mock interview.**

The biggest mistake now would be spending 2 hours learning obscure Python internals while not being able to confidently explain **your API/project**.

**Let's continue with `is vs ==`, mutable/immutable behavior, and Python collections first.**