# Employee Hierarchy

A simple Python application demonstrating Object-Oriented Programming (OOP) principles
---

## 📌 Project Overview

This project builds a simple employee hierarchy:
- **`Employee`** (Base Class): Represents standard employees with a base salary.
- **`Manager`** (Subclass): Inherits from `Employee` and includes an added performance bonus.
- **`Developer`** (Subclass): Inherits from `Employee` and includes an added project allowance.

All classes share a common interface method, `calculate_salary()`, allowing the system to process payroll dynamically across a list of mixed employee roles.

## 🛠️ Features

- **Object-Oriented Design:** Clear separation of base and derived classes.
- **Polymorphism:** Iterate through a list of different employee types and invoke their specialized `calculate_salary()` methods seamlessly.
- **Flexible Extensions:** Easy to add new employee types (e.g., `Intern`, `SalesExecutive`) without modifying existing payroll logic.

## 🚀 Getting Started

### Prerequisites
- [Python 3.x](https://www.python.org/downloads/) installed on your machine.

### Installation
1. Clone this repository:
   ```bash
   git clone [https://github.com/your-username/employee-hierarchy.txt](https://github.com/your-username/employee-hierarchy.txt)
