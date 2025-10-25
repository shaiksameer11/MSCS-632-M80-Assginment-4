"""
Employee Scheduling Application - Python Implementation
This program manages employee schedules for a company operating 7 days a week.
Author: Harshith Kalluri
"""

import random
from typing import Dict, List, Set

# Days of the week
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Shift types
SHIFTS = ["Morning", "Afternoon", "Evening"]

# Minimum employees required per shift
MIN_EMPLOYEES_PER_SHIFT = 2

# Maximum days an employee can work per week
MAX_DAYS_PER_WEEK = 5


class EmployeeScheduler:
    """Class to manage employee scheduling"""
    
    def __init__(self):
        """Initialize the scheduler with empty data structures"""
        # Store employee preferences: {employee_name: {day: shift}}
        self.preferences = {}
        
        # Store final schedule: {day: {shift: [employees]}}
        self.schedule = {}
        
        # Track days worked by each employee: {employee_name: number_of_days}
        self.days_worked = {}
        
        # Initialize schedule structure
        for day in DAYS:
            self.schedule[day] = {
                "Morning": [],
                "Afternoon": [],
                "Evening": []
            }
    
    def add_employee_preference(self, name: str, day: str, shift: str):
        """Add an employee's shift preference for a specific day"""
        
        # Input validation
        if day not in DAYS:
            print(f"Error: {day} is not a valid day")
            return False
        
        if shift not in SHIFTS:
            print(f"Error: {shift} is not a valid shift")
            return False
        
        # Initialize employee if not exists
        if name not in self.preferences:
            self.preferences[name] = {}
            self.days_worked[name] = 0
        
        # Check if employee already has preference for this day
        if day in self.preferences[name]:
            print(f"Warning: {name} already has a preference for {day}")
            return False
        
        # Add preference
        self.preferences[name] = self.preferences.get(name, {})
        self.preferences[name][day] = shift
        
        return True
    
    def create_schedule(self):
        """Create the weekly schedule based on preferences and constraints"""
        
        print("\n=== Starting Schedule Creation ===\n")
        
        # First pass: Assign employees to their preferred shifts
        for employee, prefs in self.preferences.items():
            for day, preferred_shift in prefs.items():
                
                # Check if employee hasn't exceeded maximum days
                if self.days_worked[employee] >= MAX_DAYS_PER_WEEK:
                    print(f"{employee} has already worked {MAX_DAYS_PER_WEEK} days")
                    continue
                
                # Check if employee is not already scheduled for this day
                already_scheduled = False
                for shift in SHIFTS:
                    if employee in self.schedule[day][shift]:
                        already_scheduled = True
                        break
                
                if already_scheduled:
                    print(f"{employee} is already scheduled on {day}")
                    continue
                
                # Assign to preferred shift
                self.schedule[day][preferred_shift].append(employee)
                self.days_worked[employee] += 1
                print(f"Assigned {employee} to {preferred_shift} shift on {day}")
        
        # Second pass: Fill shifts that have fewer than minimum employees
        print("\n=== Filling Understaffed Shifts ===\n")
        
        for day in DAYS:
            for shift in SHIFTS:
                current_count = len(self.schedule[day][shift])
                
                # If shift needs more employees
                while current_count < MIN_EMPLOYEES_PER_SHIFT:
                    # Find available employees
                    available = self._find_available_employees(day)
                    
                    if not available:
                        print(f"Warning: Cannot fill {shift} shift on {day}")
                        break
                    
                    # Randomly select an available employee
                    selected = random.choice(available)
                    self.schedule[day][shift].append(selected)
                    self.days_worked[selected] += 1
                    current_count += 1
                    
                    print(f"Randomly assigned {selected} to {shift} shift on {day}")
        
        print("\n=== Schedule Creation Complete ===\n")
    
    def _find_available_employees(self, day: str) -> List[str]:
        """Find employees who are available to work on a specific day"""
        available = []
        
        for employee in self.preferences.keys():
            # Check if employee hasn't exceeded maximum days
            if self.days_worked[employee] >= MAX_DAYS_PER_WEEK:
                continue
            
            # Check if employee is not already scheduled for this day
            already_scheduled = False
            for shift in SHIFTS:
                if employee in self.schedule[day][shift]:
                    already_scheduled = True
                    break
            
            if not already_scheduled:
                available.append(employee)
        
        return available
    
    def print_schedule(self):
        """Print the final schedule in a readable format"""
        
        print("\n" + "="*70)
        print("FINAL EMPLOYEE SCHEDULE FOR THE WEEK")
        print("="*70 + "\n")
        
        for day in DAYS:
            print(f"\n{day.upper()}")
            print("-" * 50)
            
            for shift in SHIFTS:
                employees = self.schedule[day][shift]
                employee_list = ", ".join(employees) if employees else "No employees assigned"
                print(f"  {shift:15} : {employee_list}")
        
        print("\n" + "="*70)
        print("EMPLOYEE WORK SUMMARY")
        print("="*70 + "\n")
        
        # Sort employees by name
        sorted_employees = sorted(self.days_worked.items())
        
        for employee, days in sorted_employees:
            print(f"  {employee:20} : {days} days")
        
        print("\n" + "="*70 + "\n")


def main():
    """Main function to run the employee scheduling application"""
    
    print("="*70)
    print("EMPLOYEE SCHEDULING APPLICATION")
    print("="*70)
    
    # Create scheduler instance
    scheduler = EmployeeScheduler()
    
    # Sample data: Add employee preferences
    print("\n=== Adding Employee Preferences ===\n")
    
    # Employee 1: Alice
    scheduler.add_employee_preference("Alice", "Monday", "Morning")
    scheduler.add_employee_preference("Alice", "Tuesday", "Morning")
    scheduler.add_employee_preference("Alice", "Wednesday", "Morning")
    scheduler.add_employee_preference("Alice", "Thursday", "Morning")
    scheduler.add_employee_preference("Alice", "Friday", "Morning")
    
    # Employee 2: Bob
    scheduler.add_employee_preference("Bob", "Monday", "Afternoon")
    scheduler.add_employee_preference("Bob", "Wednesday", "Afternoon")
    scheduler.add_employee_preference("Bob", "Friday", "Afternoon")
    scheduler.add_employee_preference("Bob", "Saturday", "Afternoon")
    
    # Employee 3: Charlie
    scheduler.add_employee_preference("Charlie", "Tuesday", "Evening")
    scheduler.add_employee_preference("Charlie", "Thursday", "Evening")
    scheduler.add_employee_preference("Charlie", "Saturday", "Evening")
    
    # Employee 4: Diana
    scheduler.add_employee_preference("Diana", "Monday", "Morning")
    scheduler.add_employee_preference("Diana", "Tuesday", "Afternoon")
    scheduler.add_employee_preference("Diana", "Wednesday", "Evening")
    scheduler.add_employee_preference("Diana", "Friday", "Morning")
    
    # Employee 5: Eva
    scheduler.add_employee_preference("Eva", "Monday", "Evening")
    scheduler.add_employee_preference("Eva", "Wednesday", "Morning")
    scheduler.add_employee_preference("Eva", "Thursday", "Afternoon")
    scheduler.add_employee_preference("Eva", "Sunday", "Evening")
    
    # Employee 6: Frank
    scheduler.add_employee_preference("Frank", "Tuesday", "Morning")
    scheduler.add_employee_preference("Frank", "Thursday", "Morning")
    scheduler.add_employee_preference("Frank", "Saturday", "Morning")
    
    # Employee 7: Grace
    scheduler.add_employee_preference("Grace", "Monday", "Afternoon")
    scheduler.add_employee_preference("Grace", "Wednesday", "Afternoon")
    scheduler.add_employee_preference("Grace", "Friday", "Evening")
    scheduler.add_employee_preference("Grace", "Sunday", "Morning")
    
    # Employee 8: Henry
    scheduler.add_employee_preference("Henry", "Tuesday", "Evening")
    scheduler.add_employee_preference("Henry", "Thursday", "Evening")
    scheduler.add_employee_preference("Henry", "Saturday", "Afternoon")
    
    print("\nEmployee preferences added successfully!\n")
    
    # Create the schedule
    scheduler.create_schedule()
    
    # Print the final schedule
    scheduler.print_schedule()


# Run the application
if __name__ == "__main__":
    main()
