
# Task 07: OpenAI Agents SDK

# Exploring the OpenAI Agents SDK

### What is an OpenAI Agent?

An OpenAI Agent is a smart AI helper.  
It can talk, think, use tools, and do tasks for us.

### What is the OpenAI Agents SDK?

The SDK is a set of tools that helps you build your own AI agent.  
It makes it easy to create agents that can understand, think, and act. All with simple code.

---

#  Core Concepts:
Agents SDK is built on four simple but powerful ideas:

-  **Agents** are like humans who follow instructions and use tools to solve tasks.

-  **Handoffs** are like teamwork — one agent can ask another for help.

-  **Guardrails** are like safety rules to keep agents in control.

-  **Tracing & Observability** is like watching and understanding what the agents are doing.


##  Questions to Help You Understand

Explore these questions and answers to understand OpenAI Agents SDK easily.


## 1. The Agent class has been defined as a dataclass why?

### What is an Agent?

An Agent is a smart helper that can think, talk, and use tools to finish tasks — like a real assistant.  

In the OpenAI SDK, the Agent class stores everything the agent needs — like its name, tools, goals, and memory.

### What is a dataclass?

A `dataclass` is a simple way to create classes that mostly hold data.  
It saves you from writing extra code by creating common functions automatically.
The Agent class is made a dataclass to make the code shorter and easier to understand. When we use dataclass, 
Python automatically creates things like the __init__ method, so we don't have to write it ourselves. 
Using `dataclass` makes it quick to write and easy to read.  
That’s why the Agent class is made with `dataclass`.

## 2a. The system prompt is contained in the Agent class as instructions? Why you can also set it as callable?

The system prompt is in the Agent class to guide how the agent should reply. Making it callable means you can use it like a function to send a message and get a reply easily.

## 2b. But the user prompt is passed as parameter in the run method of Runner and the method is a classmethod

The run method in the Runner class is a classmethod, so you can call it using the class name like Runner.run(prompt) without making an object. You pass the user’s message as a parameter, and it runs the agent to get a response.

## 3. What is the purpose of the Runner class?

The Runner class is used to run the agent. It takes the user's message, sends it to the agent, and gives the agent's reply. It helps the user talk to the agent easily.

## 4. What are generics in Python? Why we use it for TContext?

Generics in Python let you write code that can work with many different types, not just one specific type. This helps make your code more flexible and reusable.

We use  TContext so the agent can handle different kinds of context data without changing the code. It allows the agent to work with any type of context, making it more flexible.

## Summary
The OpenAI Agents SDK is easy and powerful. It helps you build smart and safe AI agents that work well and are easy to understand.

