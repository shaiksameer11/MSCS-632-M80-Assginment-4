# Employee Scheduling Application

## Project Overview

This project implements an employee scheduling system for a company that operates 7 days a week with three shifts per day (Morning, Afternoon, Evening). The application manages employee shift preferences and creates a weekly schedule while respecting various constraints.

**Author:** Harshith Kalluri  
**Course:** Secure Software Development  
**Languages Used:** Python and Java

---

## Project Requirements Met

### Core Features Implemented:

1. **Input and Storage**
   - Collects employee names and shift preferences for each day
   - Stores information in appropriate data structures (dictionaries in Python, HashMaps in Java)

2. **Scheduling Logic**
   - Ensures no employee works more than one shift per day
   - Limits each employee to a maximum of 5 days per week
   - Guarantees at least 2 employees per shift per day
   - Randomly assigns additional employees when shifts are understaffed

3. **Shift Conflicts**
   - Detects when preferred shifts are unavailable
   - Resolves conflicts by assigning employees to available shifts

4. **Output**
   - Displays final weekly schedule in a readable format
   - Shows which employees are assigned to each shift on each day
   - Provides a summary of days worked by each employee

---

## Programming Languages

### 1. Python (Version 3.8 or higher)
- **Paradigm:** Multi-paradigm (procedural, object-oriented)
- **Why chosen:** Simple syntax, excellent for rapid development, built-in data structures
- **Key features used:** Classes, dictionaries, lists, type hints

### 2. Java (Version 8 or higher)
- **Paradigm:** Object-oriented programming
- **Why chosen:** Strong typing, enterprise-level language, different syntax from Python
- **Key features used:** Classes, HashMap, ArrayList, generics

These languages provide sufficient contrast as required:
- Python uses dynamic typing; Java uses static typing
- Python is interpreted; Java is compiled
- Different syntax and programming styles
- Different approaches to memory management

---

## File Structure

```
project-directory/
│
├── employee_scheduler.py       # Python implementation
├── EmployeeScheduler.java      # Java implementation
├── README.md                   # This file (setup instructions)
└── screenshots/                # Output screenshots (if applicable)
```

---

## Setup and Installation Instructions

### Prerequisites

#### For Python:
1. **Install Python** (if not already installed)
   - Download from: https://www.python.org/downloads/
   - Verify installation:
     ```bash
     python3 --version
     ```
   - Should display Python 3.8 or higher

#### For Java:
1. **Install Java Development Kit (JDK)**
   - Download from: https://www.oracle.com/java/technologies/downloads/
   - Or install OpenJDK:
     - **Ubuntu/Debian:**
       ```bash
       sudo apt-get update
       sudo apt-get install default-jdk
       ```
     - **macOS:**
       ```bash
       brew install openjdk
       ```
     - **Windows:** Download installer from Oracle or adopt OpenJDK

2. **Verify Java installation:**
   ```bash
   java --version
   javac --version
   ```
   - Both should display version 8 or higher

---

## How to Run the Programs

### Running Python Implementation

1. **Navigate to the project directory:**
   ```bash
   cd /path/to/project-directory
   ```

2. **Run the Python program:**
   ```bash
   python3 employee_scheduler.py
   ```
   
   OR on Windows:
   ```bash
   python employee_scheduler.py
   ```

3. **Expected Output:**
   - The program will display employee preferences being added
   - Show the scheduling process
   - Display the final weekly schedule
   - Show a summary of days worked by each employee

### Running Java Implementation

1. **Navigate to the project directory:**
   ```bash
   cd /path/to/project-directory
   ```

2. **Compile the Java program:**
   ```bash
   javac EmployeeScheduler.java
   ```
   
   - This creates an `EmployeeScheduler.class` file

3. **Run the compiled program:**
   ```bash
   java EmployeeScheduler
   ```

4. **Expected Output:**
   - Similar output to Python version
   - Shows employee assignments and final schedule

---

## Understanding the Code

### Key Control Structures Used

#### Conditionals (if-else statements):
- **Purpose:** Check constraints and validate input
- **Example locations:**
  - Checking if employee has exceeded maximum days
  - Validating day and shift names
  - Detecting scheduling conflicts

#### Loops:
- **For loops:** Iterate through days, shifts, and employees
- **While loops:** Fill understaffed shifts until minimum requirement is met
- **Example locations:**
  - Processing all employee preferences
  - Checking each day and shift for staffing levels

#### Data Structures:
- **Python:** Dictionaries (dict), Lists (list)
- **Java:** HashMap, ArrayList
- **Purpose:** Store and organize employee data, preferences, and schedules

---

## Sample Data

The programs include sample data for 8 employees:
- **Alice:** Prefers morning shifts (5 days)
- **Bob:** Prefers afternoon shifts (4 days)
- **Charlie:** Prefers evening shifts (3 days)
- **Diana:** Mixed preferences (4 days)
- **Eva:** Mixed preferences (4 days)
- **Frank:** Morning shifts (3 days)
- **Grace:** Mixed preferences (4 days)
- **Henry:** Evening and afternoon shifts (3 days)

You can modify these in the `main()` method of either program.

---

## Customization Options

### To Add More Employees:

**Python:**
```python
scheduler.add_employee_preference("NewEmployee", "Monday", "Morning")
```

**Java:**
```java
scheduler.addEmployeePreference("NewEmployee", "Monday", "Morning");
```

### To Change Constants:

Both programs have constants at the top that you can modify:
- `MIN_EMPLOYEES_PER_SHIFT` - Change minimum required employees per shift
- `MAX_DAYS_PER_WEEK` - Change maximum days an employee can work

---

## Troubleshooting

### Common Issues:

1. **Python: "python3: command not found"**
   - Solution: Use `python` instead of `python3`, or install Python 3

2. **Java: "javac: command not found"**
   - Solution: Ensure JDK is installed (not just JRE)
   - Add Java to your PATH environment variable

3. **Java: "Exception in thread 'main' java.lang.ClassNotFoundException"**
   - Solution: Make sure you compiled the program first with `javac`
   - Run from the same directory where the .class file was created

4. **Warning: "Cannot fill shift on Sunday"**
   - This is expected when all employees have reached maximum days
   - The program will still run and show which shifts couldn't be filled

---

## Testing the Programs

Both implementations should produce similar (but not identical) outputs because:
- The random assignment of employees to understaffed shifts will vary
- The order of processing may differ slightly between implementations
- Both respect all the scheduling constraints

### What to Check:
1. No employee works more than 5 days
2. No employee has more than one shift on the same day
3. Most shifts have at least 2 employees (some may have fewer if impossible to fill)
4. All employee preferences are honored when possible

---

## Code Structure Comparison

### Python Approach:
- Uses a class-based approach with instance methods
- Leverages Python's built-in dictionary and list data types
- More concise syntax with dynamic typing
- Uses list comprehensions for filtering

### Java Approach:
- Fully object-oriented with strong typing
- Uses Java Collections Framework (HashMap, ArrayList)
- More verbose with explicit type declarations
- Requires compilation before execution

---

## Learning Outcomes

This project demonstrates:
1. **Conditional logic:** Validating inputs and checking constraints
2. **Loop structures:** Iterating through collections and repeating processes
3. **Data structure management:** Storing and organizing complex data
4. **Algorithm design:** Creating schedules with multiple constraints
5. **Random selection:** Assigning employees when preferences don't fill requirements
6. **Multi-language implementation:** Understanding how different languages approach the same problem

---

## References

Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design patterns: Elements of reusable object-oriented software*. Addison-Wesley.

Lutz, M. (2013). *Learning Python* (5th ed.). O'Reilly Media.

Oracle. (2023). *The Java tutorials*. Retrieved from https://docs.oracle.com/javase/tutorial/

---

## Additional Notes

- Both programs use the same logic and produce equivalent results
- The random assignment ensures different runs may produce different results
- The code includes comments explaining key sections
- Error handling is included for invalid inputs
- The schedule respects all business rules defined in the requirements

---
