---
title: Software Development Principles
summary: Software development principles, seasoned with a bit of Python
tags:
    - development
    - principles
    - python
    - book-summary
date: 2022-09-11
slug: software-development-principles
---

# General Principles

- **Keep it short and simple** (abbreviated KISS)
- **Boy scout rule**: Leave the code cleaner than you found. This helps for incremental codebase cleanup.
- **Don't repeat yourself** (abbreviated DRY): Every piece of knowledge (information or behavior) must have a single representation in the system.
- **There's more than one way to do it** (abbreviated TMTOWTDI and pronounced "Tim Toady"): Design the system to be flexible: a user may find multiple ways to achieve his goad. Used in Perl, avoided in Python.
- **You aren't gonna need it** (abbreviated YAGNI): Implement functionality only when you need it.
- **Open-close**: An entity (function, class, module) should be open to extensions, but close for modifications.

# Contextual

## Naming

- Use intention-revealing names.
    - `elapsed_time_in_days`, not `d` (context-dependent)
    - `game_board`, not `the_list` (context-dependent)
- Avoid disinformation.
    - `accounts`, not `accounts_list` (linked to the implementation, namely an iterable of type `list`)
- Make meaningful distinction between variables with close names.
    - `money` and `money_amount` are the same when used in the same context.
    - There is no difference between `Product`, `ProductData` and `ProductInfo` due to the noise words used as suffixes.
- Use pronounceable names.
    - `generation_timestamp`, not `gen_time_ymdhms`
- Use searchable names.
    - Too generic search when using `7`. A constant named `DAYS_IN_WEEK` is better.
- Avoid encodings, mental mapping, prefixes, and type information.
    - `multiplication_factor`, not simply `f`
    - `__users`, not `__private_users`
    - `accounts`, not `accounts_dictionary`
- Avoid abstract words such as:
    - `processor`
    - `data`
    - `info`
    - `controller`
    - `manager`
- Functions should have verbs in their names.
    - `pay_employee()`, not `new_payment()`
- Don't be cute or use puns.
    - Plain `kill()`, not `whack()`
- Make the names context-specific
    - A `zipcode` in a context where `source_address` and `destination_address` can refer to any of them. Transform it into `source_zipcode` or `destination_zipcode`.

## Comments

- Use code to document the code.
    - `employee.is_eligible_for_full_benefits()`, not `if (employee.has_flag(HOURLY) && employee.age > 65) // check if the employee is eligible for full benefits`
- Use good comments:
    - Legal, for example copyrights
    - Description of a decision
    - `TODO` comments
- Avoid bad comments:
    - Dependent information, such as constants values and parameters names that could be changed in future implementations
    - Commented-out code
      - Just remove it, you have `git` to restore it if you need to.
    - Journal comments (use `git blame` instead)
    - Position markers, such as `// Public methods`
    - Obvious comments, such as `// Defaults constructor`

## Lines of Code

- Declare variables close to their first usage.
- Avoid multiple `switch` statements. The only ones should occur when creating a class in a factory. Multiples switches are a sign of bad design. Inheritance can be used.
- Keep lines short (120 characters per line recommended).
- Use implicit line joining for splitting long lines of text.

## Functions

### Functionality

- Do one thing.
    - `save_page_to_file` calls multiple functions to: download page and write the content to a file. It does not execute this whole functionality on its own.
- Only one level of abstraction per function
    - A function `get_links_from_html_page` downloads the page and calls another function to search the effective text with a RegEx (which is at another abstraction level).
- Do only what's expected.
    - A `check_password` function will not initialize a session.

### Structure

- Small functions, with 20 LoCs (recommended)
- Only one indentation level
- Use structured programming: one entry, one exit.
- Remove functions that are not called.

### Arguments

- Prefer fewer arguments. When over 3 arguments, maybe you can pass a class instead.
- Avoid output arguments.
- No flag arguments. Split the function into multiple functions, one per each flag possible value.
- Don't pass `None` to any argument.
- Annotate their type.

### Return Value

- Do not return `None`.
- Do not return error codes. Raise exception instead.
- Annotate its type.

### Documentation

- Document only the functionalities that are on the edge of the system you design. The others impose friction during implementation.

## Objects and Data Structures

### Design

- Use classes for allowing access to members only through methods. This allows further processing and verifications.
- Use data structures to group data. The processing is done through another functions.
- Avoid hybrids (half class, half data structure), namely classes with exposed members.
- **Single Responsibility Principle** (abbreviated SRP) or **High Cohesion**: A class should have one and only one reason to change.
- **Low coupling**: A class should have the least possible dependencies.
- **Dependency injection**: Delegate secondary responsibilities to another objects that are dedicated for that purpose.
    - Do not manage the profile picture in a `User` class, just create a new `ProfilePicture` one that manages itself.
- **Composition over Inheritance** (abbreviated CoI): Prefer embedding of different objects within another object (according to the dependency injection principle) instead of inheritance. The latter will expose all the public methods of the parent class and is limited by some programming languages (for example, multiple inheritance could not be achieved).
- **Interface Segregation Principle** (abbreviated ISP): A client should not have access to methods it doesn't use. If a broader interface is used, another interface (called role interface) can be created to limit the exposed methods.
- **Liskov Substitution Principle** (abbreviated LSP): If a class is substituted with any of its subclasses, the program should work well. This implies that the return types and exceptions types remains the same. In addition, no side effect is introduced.

### Structure

- Declare instance variables at the top of the class.
- After the instance variable, place each public function, eventually followed by the private methods it calls.

### Methods

- **Law of Demeter**: A method should not know about the implementation of an object it manipulates.
    - `user.profile_picture.badge`, not `user.get_profile_picture().get_badge()`.
- If a method does not use the parent object, transform it into a `@staticmethod`.

### Members

- Annotate types in class beginning.
- Initialize the members in constructor.
- Place a `_` in front of the name if the member is protected (that can be used in a subclass) and `__` if it is private (used only in the current class).

## Included Modules

- Use only absolute imports.
- Import only the functionalities that are exposed explicitly by the module (for example, the ones in `__init__.py`). Do not navigate the inwards of the module.

## Source Code Files (or Modules)

- Avoid huge files (over some hundreds LoCs).
- Place the called functions after the callee. The code can be read as a newspaper.
- Add a docstring describing the source code functionality.
- Maintain a predictable structure:
    - Imports
    - Constants
    - Type annotations aliases
    - Enumerations
    - Classes
    - Module-level functions

## Third-Party Components

- Hide third party code with wrapper classes.
- Translate learning code in unit tests. If something changes in the future versions, the tests will fail.
- Implement interfaces and dummy classes for upcoming functionalities.

## Whole System

- Separate the startup process of the application.

# Additional Aspects

## Formatting

- Establish formatting rules with your team. Implement them using linters and formatters.
- Avoid formatting your code manually.

## Error Handling

- Use exceptions, not return codes.
- Define a root exception and inherit from it for each child exception.
- Provide context to an exception with the help of docstrings and name uniqueness.
- Push error handling to the edge of each component of the system.

## Unit Testing

- Create a test for each state of a function/object.
    - Test an exception in a function separately, not in the test targeting the normal functioning
- Keep only one `assert` per test.
- **FIRST**: The tests should be:
    - Fast
    - Independent
    - Repeatable
    - Self-validating by returning a boolean indicating if it passed or not
    - Written before the code that make them pass (in a TDD fashion).
- Name each test `test_<method_or_class>_<state>`.
- Keep the production-grade standards for test code.
- The tests can be place into a different `tests` folder or in the same implementation file.
- Run all the tests.
- Use coverage to determine code that is not tested.

## Journaling

- Avoid `print`. Use logging functionalities instead.

## Configuration

- **Convention over configuration** (abbreviated CoC): Develop software by establishing "sensible defaults" wrapped into conventions. This will ease the usage compared to the more flexible approach of configuration.
- Expose the user-configurable aspects via a separate configuration class that parse a configuration file to get its members values.
- Expose the aspects configurable by programmers via constants in the current file or in a separate module, only with configuration constants.

---

# References

- [Clean Code: A Handbook of Agile Software Craftsmanship](https://www.goodreads.com/book/show/3735293-clean-code)
