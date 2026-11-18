# Job Application Tracking Management System

A simple, menu-driven Python console application that helps job seekers store, manage and track their job applications in one place.

Built as a beginner project using Python dictionaries, loops and `match-case`.

## Features

| No. | Feature | Description |
|-----|---------|-------------|
| 1 | Add Application | Add company, role and location (status starts as `Applied`) |
| 2 | Display All Applications | View every saved application |
| 3 | Search Application | Find an application using its Application ID |
| 4 | Update Application | Change company, role and location |
| 5 | Delete Application | Remove an application |
| 6 | Track / Update Status | Applied, Shortlisted, Rejected or Selected |
| 7 | Exit | Close the program |

## Tech Stack

- **Language:** Python 3.10 or newer (`match-case` needs 3.10+)
- **Editor:** Visual Studio Code
- **Storage:** Python dictionary (nested dictionary), in memory
- **Interface:** Command line / terminal

## Concepts Used

`while` loop, `match-case`, `if / elif / else`, dictionary, nested dictionary, `for` loop, `items()`, `len()`, `del`, `input()` and `print()`.

## How to Run

1. Make sure Python 3.10 or newer is installed:

   ```bash
   python --version
   ```

2. Clone this repository:

   ```bash
   git clone https://github.com/<your-username>/job-application-tracker.git
   cd job-application-tracker
   ```

3. Run the program:

   ```bash
   python job_tracker.py
   ```

## Data Structure

Each application is stored in a dictionary. The Application ID is the key and the details are the value.

```python
applications = {
    1: {
        "appId": 1,
        "company": "TCS",
        "role": "Python Developer",
        "location": "Mumbai",
        "status": "Applied"
    }
}
```

## Sample Output

![Sample Output](output.png)

## Limitations

- Records are stored only in memory, so all data is lost when the program closes.
- Application ID cannot be changed during an update.
- The program stops if letters are typed where a number is expected.
- No database, login or graphical interface.

## Future Enhancements

- Rewrite each menu option as a function
- Add an interview date field
- Save data permanently using a file (CSV / JSON) or SQLite
- Add input validation and exception handling (`try / except`)
- Search and filter by company name or status
- Add a graphical interface

## Author

**Sunita Vaijanath Randive**
