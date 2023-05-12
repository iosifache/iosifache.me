---
title: Fundamentals of Software Architecture
summary: Main ideas and personal notes on the book "Fundamentals of Software Architecture”
tags:
  - architecture
  - software-development
  - book-summary
date: 2022-10-15
slug: fundamentals-of-software-architecture
---

# Software Architecture

- It is the blueprint of a system, consisting on:
    - Structure: The way in which components are arranged. For example, microservices or monolith.
    - Characteristics: Operational goals supported by the architecture. For example, availability, testability, and performance.
    - Decisions: Rules based on which the system is designed. For example, what particular layers can access the data layer directly.
    - Design principles: Guideline (not hard limits, but a decision). For example, the preference of asynchronous messages between services.

# Software Architects

## Responsibilities

- Make architecture decisions.
    - Manage trade-offs.
- Continually analyze the architecture.
- Keep current with latest trends.
    - Code. This will avoid the Romanian "Fă ce zice popa, nu ce face el".
- Ensure compliance with decisions.
- Diverse exposure and experience.
- Have business domain knowledge.
- Possess interpersonal skills.
- Understand and navigate politic.

## Comparison with a Developer

- The architect operate on a greater level of abstraction (structure, characteristics, decision, design principles). A developer deals with more concrete artifacts, such as class design, user interfaces and source code.

![](/images/fundamentals-of-software-architecture/fosa_0203.png)

- The architect has a higher technical breadth than a developer. The latter has depth.
    - In the pyramid below, the depth is the measure of how well you operate the technologies/frameworks/tools you know that you know (the height of the first section). The breadth is the number of ones you know you don't know (the width of the second section).
    - The goal is to invert the shape: to increase the staff you know and decrease the ones that you don't have idea about.

![](/images/fundamentals-of-software-architecture/fosa_0206.png)

## Katas

- Architectural katas are exercises practiced by architects to build an architecture from a set of business concerns.
- They are explained by specifying:
    - A problem description
    - Users
    - Requirements
    - Additional context.

# Architecture Characteristics

- Are also known as non-functional requirements.
- These are not established by the architect himself, but deduced from domain concerns. For example, if a business expects a burst of connections when the Black Friday campaign starts, then the architecture needs to be elastic (the elasticity characteristic).
- They are applied for each architectural quantum.

## Criteria

- Specifies a non-domain design consideration.
- Influences some structural aspect of the design.
- Is critical or important to application success.

## Explicit and Implicit Characteristics

- Explicit, that appear explicitly in the problem specification
- Implicit, which are deducted by the architect. For example, if a website process card information, the security is implicit. It needs to be embedded in the architecture, despite the lack of explicit specification.

## Common Characteristics

- Operational
    - Availability
    - Continuity
    - Performance
    - Recoverability
    - Reliability
    - Robustness
    - Scalability
    - Elasticity
- Structural
    - Modularity
    - Configurability
    - Extensibility
    - Installability
    - Reuse
    - Localization
    - Maintainability
    - Portability
    - Supportability
    - Upgradability
- Cross-cutting
    - Accessibility
    - Archivability
    - Authentication
    - Authorization
    - Legal
    - Privacy
    - Security
    - Supportability
    - Usability

## Architectural Quantum

- A quantum is an independently deployable artifact with high functional cohesion and synchronous connascence.
    - "An architecture quantum includes all the necessary components to function independently of other parts of the architecture."
    - "High functional cohesion implies that an architecture quantum does something purposeful."
    - "Synchronous connascence implies synchronous calls within an application context or between distributed services that form this architecture quantum."
- A kata in the book presents an auction company. Multiple quanta were identified, each with different characteristics:
    - Bidder feedback
    - Auctioneer
    - Bidder.

## Governance via Fitness Functions

- The characteristics are imposed via fitness functions, namely any mechanism that provides an objective integrity assessment of the characteristic.
- Fitness functions are only a new way to perceive the existent tools used by developers:
    - Metrics
    - Monitors
    - Unit testing
    - Chaos engineering.
- The developers needs to understand why the fitness function is introduced.

### Cyclomatic Complexity

- An example for ensuring modularity is a metric named Cyclomatic Complexity.
- It provides an object measure for the complexity of code, at the function/method, class, or application level.
- The value of 5 is ideal, but anything under 10 is ok.

### Cohesion

- Defines to which extent the parts of a module should be contained within the same module.

#### Types

- Functional: One module contains everything it needs to function.
- Sequential: One module's output is another's input.
- Communicational: Modules exchanges information.
- Procedural: The code from two modules must execute in a particular order.
- Temporal: Modules are related based on timing dependencies.
- Logical: The code inside a module is related, but not functionally coupled. For example, a utility module.
- Coincidental: Luck made the code be in the same module. It's the worst.

#### Metrics

- Instability
    - Is defined as the ratio of efferent coupling to the sum of both efferent and afferent coupling.
    - Afferent coupling measures the number of incoming connections to a code artifact (component, class, function, and so on).
    - Efferent coupling measures the outgoing connections to other code artifacts.
- Abstractness
    - Is the ratio of abstract artifacts (abstract classes, interfaces, and so on) to concrete artifacts (implementation).
- Distance from the main sequence

![](/images/fundamentals-of-software-architecture/fosa_0303.png)

- Chidamber and Kemerer Lack of Cohesion in Methods (abbreviated LCOM)

### Connascence

- Two components are connascent if a change in one would require the other to be modified in order to maintain the overall correctness of the system.

#### Types

- Static, namely source-code coupling
    - Name: For example, name of methods.
    - Type: For example, type of variable.
    - Meaning: For example, meaning of `true` in a programming language.
    - Position: For example, order of given parameters.
    - Algorithm: For example, a hashing algorithm used by two modules.
- Dynamic, at runtime
    - Execution: When order of executing some code blocks matters.
    - Timing: For example, two threads manipulating a shared resource.
    - Values: For example, transactions in distributed instances of relational databases.
    - Identity: When two components must change together.
- Quantum
    - Synchronous
    - Asynchronous

#### Metrics

- Strength: Ease with which a developer can refactor that type of coupling.
- Degree: Size of the impact.

# Architecture

## Modules

- Modules are logical groups of related code.
- Examples
    - Classes in an object-oriented language
    - Functions in a structured or functional language

## Components

- The architecture is composed of components, which are the physical manifestation of a software module.
- There are two ways to partition components:
    - Technical, in which components are grouped depending on their technical functions
    - Domain, in which groups are formed by considering the business domains and workflows.

![](/images/fundamentals-of-software-architecture/fosa_0805.png)
## Techniques

### Entity (Trap)

- The data model dictates the overall architecture.
- Derives from Fred Brooks' Approach: "Get the data structures correct, and the code will write itself".
-  Process
    1. Identify the data structures.
    2. Map the data structures to components.
- It is ok for simplistic applications, when a simple CRUD database suffice. The pattern that could be applied is naked objects.

### Actor/Action

- Process
    1. Identify the actors.
    2. Identify the actions performed by each actor.

### Event Storming

- Came from domain-driven design and is widely used when designing microservices.
- Process
    1. Suppose messages/events are exchanged between the established (future) components.
    2. Identify all events that may occur.
    3. Group the events in components.

### Workflow

- Process
    1. Identify the key roles.
    2. Identify the workflows in which each role is involved.
    3. Group the workflows in components.

### Recommended Process

1. Identify initial components.
2. Divide the functional requirements (or user stories) and assign them to each component.
3. For each component:
    1. Establish characteristics from business concerns.
    2. Restructure the components.
4. When the restructuring is no longer required:
    1. Prioritize the most important characteristics.
    2. Measure the top characteristics by setting fitness functions.

## Architecture Styles

- Types
    - Monolithic, in which all code is encapsulated into a single deployment unit
    - Distributed, in which multiple deployment units exits

### Big Ball of Mud

- "A Big Ball of Mud is a haphazardly structured, sprawling, sloppy, duct-tape-and-baling-wire, spaghetti-code jungle [..] The overall structure of the system may never have been well-defined." - Brian Foote

### Layered

![](/images/fundamentals-of-software-architecture/fosa_1003.png)

- Monolithic structure
- One quanta
- Technical partitioning
- Composed of multiple logical layers, each with a different role or responsibility (handling the UI, executing business operations, storing data, etc.)
- A variant of this architecture is the closed-layered architecture, in which a request from the topmost layer must be handled by each layer, without the ability to skip any of it (as in the fast-lane reader pattern).
- You must avoid the architecture sinkhole anti-pattern, in which requests are only passed from layer to layer, without any processing. There are scenarios in which this must happen, but they don't need to exceed 20% from all scenarios.

### Pipeline

![](/images/fundamentals-of-software-architecture/fosa_1101.png)

- Monolithic structure
- One quanta
- Technical partitioning
- Components
    - Filters, processing (generally, in a stateless manner) the input to produce an output
    - Pipes, linking the filters
        - Producer
        - Transformer
        - Tester
        - Consumer
- Appears as an underlying principle in Unix shell languages

### Microkernel

![](/images/fundamentals-of-software-architecture/fosa_1202.png)

- Monolithic structure
- One quanta
- Domain or technical partitioning
- Also named plug-in architecture
- Components
    - Core system, with minimal functionalities to run the system
    - Multiple plug-in components, with specialized functionalities meant to enhance or extend the core system
    - Registry of available modules
    - Contracts, to standardize the communication between plug-ins and the core system

### Service-Based

![](/images/fundamentals-of-software-architecture/fosa_1304.png)

- Distributed structure
- Domain partitioning
- 1 to many quanta
- Components
    - Separately deployed user interface(s)
    - Separately deployed remote coarse-grained services (4 to 12, with 7 being the sweet spot)
    - Monolithic database or multiple domain-specific databases

### Event-Driven

![](/images/fundamentals-of-software-architecture/fosa_1401.png)

- Distributed structure
- Technical partitioned
- 1 to many quanta
- Components
    - Requests
    - Request orchestrator (optional)
    - Request processor
    - Database
- Variants
    - Mediator
        - Custom logic can be implemented in the mediator. For example, if an event is received, then a sequence of other events are generated and sent to each responsible processor.
        - The communication flow between processors represents a tree.
    - Broker, in which there is no need of central management of events
        - Technologies such as RabbitMQ and ActiveMQ are used here.
        - Distribution approaches are:
            - Fan-out: All processors receive the event.
            - Directed
            - Topic-based: Only processors which are subscribed to that topic will receive.
        - The communication flow between processors represents a graph.
- When synchronous messaging is required, then the request-reply pattern can be used.

### Space-Based

![](/images/fundamentals-of-software-architecture/fosa_1502.png)

- Distributed structure
- Domain or technical partitioned
- 1 to many quanta
- The names came from the concept of tuple space, where multiple parallel processors communicate through shared memory.
- Components
    - Processing unit
        - Code
        - In-memory data grid
        - Data replication engines
    - Virtualized middleware
        - Messaging grid, for sending requests from clients to processing units
        - Data grid, for ensuring the data replication between replicas from processing units' engines
        - Processing grid, which is like a mediator in the service-based architecture, helping to orchestrate multiple processing units to achieve a common goal
        - Deployment manager, for elasticity and startup/shutdown
    - Data pumps to send updates to database
    - Data writers to write the updates from data pumps into database
    - Data readers to read from database and send data to processing units (at startup)
- Hazelcast, Apache Ignite and Oracle Coherance are used for both in-memory data grids and data replication engines.
- A hybrid approach can be used, in which the database is on-premise and the processing units and virtualized middleware in the cloud.

### Orchestration-Driven Service-Oriented

![](/images/fundamentals-of-software-architecture/fosa_1601.png)

- Distributed structure
- Technical partitioned
- One quantum
- The architecture style is centered on reusing code from the organization's codebase.
- Components
    - Business services, which are domain-related entry points in the architecture
    - Enterprise service bus
        - Orchestration engine, defining the relationship between business and enterprise services
    - Enterprise services, which implements shared, atomic logic, that can be shared between multiple businesses
    - Application services, which are application-specific, non-shared services
    - Infrastructure services, such as logging, monitoring, authentication, and authorization

### Microservices

![](/images/fundamentals-of-software-architecture/fosa_1701.png)

- Distributed structure
- Domain partitioning
- 1 to many quanta
- Microservices means modules smaller than a service (like in the service-based architecture), not something like a serverless function (dealing only with a minimal workflow).
    - "The term microservice is a label, not a description." - Martin Fowler, the creator of the term "microservice"
- Components
    - API layer
    - Highly decoupled microservices, each modeling a domain or workflow
    - Monolithic interfaces or multiple ones
- Scenarios in which shared functionalities are required (for example, unified monitoring and logging) can be achieved with the sidecar pattern. These sidecars report to a service plane and forms a service mesh, distributed on each node of the architecture.
- When complex processes are implemented, then a mechanism from below is required:
    - Orchestration: A separate service deals with triggering other services, sequencing results and sending a result to the client.
    - Choreography: Just like in broker event-driven architecture, the services communicates with each other to achieve a common goal.

# Soft Skills

## Making Decisions

### Anti-patterns

- Covering your assets: The architect postpones or avoid making a decision because of his hear of making a wrong choice.
- Groundhog day: People don't know why a decision was made. The decision gets discussed over and over.
- Email-driven architecture: People forget about a decision that was made regarding the architecture.

### Architecture Decision Records

- An architecture decision record (ADR) is a simple record for documenting a decision regarding the architecture.
- An ADR is composed of:
    - Title
    - Status: Proposed, accepted, accepted and supersedes X, superseded by Y, request for comments until Z
    - Context: What made me do this decision?
    - Decision
    - Consequences: What's the impact of the decision?
    - Compliance: How to ensure compliance with the decisions?
    - Notes: Author, CHANGELOG, other meta-data
- These can be managed by a third party software or simply with a shared folder of Markdown files.

## Assessing Risks

- For assessing the risk of a certain component, use a 1-9 scale as follows:
![](/images/fundamentals-of-software-architecture/fosa_2001.png)
### Risk Storming

1. Gather a bunch of professionals (developers, architects, etc.) from the core team.
2. Identify the areas of risks for each pair component-characteristic.
3. Establish consensus between participants.
4. Mitigate the risks by applying enhancements to the most risky characteristics of components.  

## Diagramming

- Unified Modeling Language
- C4 model
    - Context
    - Container
    - Component
    - Class
- ArchiMate

## Leading Teams

### Architect Personalities

1. Control freak: Tries to control each aspect of the development. Imposes too tight boundaries, which cause frustration.
2. Armchair: Is not interested in the development process at all. It has loose boundaries, which can create confusion.
3. Effective: Can establish appropriate boundaries.

### Dosing the Control

For each aspect below, add or subtract 20 from a baseline 0.
- Team familiarity
- Team size
- Overall experience
- Project complexity
- Project duration.

![](/images/fundamentals-of-software-architecture/fosa_2206.png)

### Team Risks

- Process loss (or Brook's law): The more people you add to a project, the more time it will take.
- Pluralistic ignorance:  Manifests when everyone agrees to a decision, but privately rejects it.
- Diffusion of responsibility: It is based on the fact that as team size increases, it has a negative impact on communication.

### Using Checklists

Examples of checklists that can be offered to the development team are:
- Code Completion Checklist: When the developer states that the task is done.
- Unit and Functional Testing Checklist
- Software Release Checklist.

### Leadership

- Be pragmatic, yet visionary.

## Developing Thyself

- The 20-minute rule: Devote 20-minutes each day (in the morning, before opening the email inbox) to learning something new.
- Use others or develop own tech radars.
- Follow interesting persons on social media.

# Others

## Fallacies of Distributed Architectures

- The network is reliable.
- Latency is zero.
- Bandwidth is infinite.
- The network is secure.
- The topology never changes.
- The is only one administrator.
- Transport cost is zero.
- The network is homogeneous (with equipment only from one vendor).

## Replicated versus Distributed Cache

- Replicated cache uses an in-memory replica on each computing device.
- The distributed one has a central caching server and the computing devices access it via a custom protocol.

## Patterns

- Sidecar
- Service locator: Describes the process of obtaining a service with a strong abstraction layer. As in Kubernetes.
- Naked objects
- Fast-lane reader: The component bypasses unnecessary layers.

## Anti-patterns

- Anti-pattern: Something that seems like a good idea when you begin, but leads you into trouble.
- Architecture sinkhole: Passing a request from layer to layer, without any processing

## Mental Models

- Frozen caveman: A person thinks that the information he possesses is still cutting edge, despite the evolution that happened in the meantime.
- Conway's law: Organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations.

# Quotes

> "Never shoot for the _best_ architecture, but rather the _least worst_ architecture."

> "There are not right or wrong answers in architecture—only trade-offs."

> "It depends."

> "Business stakeholders will appreciate visionary solutions that fit within a set of constraints, and developers will appreciate having a practical (rather then theoretical) solution to implement."

---

# References

- [Fundamentals of Software Architecture: An Engineering Approach](https://www.goodreads.com/book/show/44144493-fundamentals-of-software-architecture)