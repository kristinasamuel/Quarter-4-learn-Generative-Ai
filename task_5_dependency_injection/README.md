## What is Dependency Injection (DI)?

Dependency Injection means:

Dependency Injection (DI) is a design pattern that allows us to pass (inject) the resources a function needs, instead of creating them inside the function itself.

### In FastAPI:
Instead of writing the same logic again and again, you write a helper function and inject it into your route.

### Why Use Dependency Injection?
- Reuse logic easily (e.g. authentication, fetching data)
- Keep code clean and organized
- Write less repeated code
- Add/remove functionality with less editing

### 💡 Real-Life Example:
Imagine logging in users:  
Instead of checking login credentials in every API route, you create a `login_check()` function once and inject it wherever you need it.

### ❌ Without Dependency Injection:  
You would write the same login check code again and again in every route.

### ✅ With Dependency Injection:  
You write one function called `login_check()` and **inject** it wherever you need. FastAPI will run it automatically before the main logic.

This saves time and keeps your code clean.