# 🗓️ Personal Planner CLI Application

A beautiful, interactive Command-Line Interface (CLI) application built with Python to help users manage their daily tasks and schedules effortlessly. This project features color-coded console logs and automated task validation.

## ✨ Features
- ⏱️ **Real-time Input Validation**: Ensures time is entered in the correct 12-hour format (e.g., `09:30 AM`).
- 📝 **Task Management**: Add tasks, view your schedule, modify existing tasks, or mark them as completed.
- 🎨 **Visual Color Coding**: Terminal outputs are color-coded (Blue, Green, Yellow, Red, Cyan) for an intuitive user experience.

## 🖥️ Program Output & Demo
Since recruiters cannot run CLI applications directly on GitHub, here is a preview of the interactive program output:

### 1. Main Menu
```
========== 🗓️ PERSONAL PLANNER ==========
1. ➕ Add Task
2. 🗓️ View Tasks
3. ✏️ Modify Task
4. ✔️ Mark Task Done
5. ❌ Exit
=========================================
```

### 2. Adding a Task
```
➕ add new task
⏱️ Enter time(HH:MM AM/PM): 09:30 AM
📝 Enter task: Prepare for Interview
✅ Task added successfully!
```

### 3. Viewing the Schedule
```
==========🗓️ MY schedule ==========
1. ⏰ 09:30 AM - Prepare for Interview
===============================
```

## 🚀 How to Run the App

### Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/angelroysms-maker/Personal-Planner.git
   ```
2. Navigate to the folder and run the script:
   ```bash
   cd Personal-Planner
   python personal_planner.py
   ```

### In Google Colab
You can copy and run this simple command in any Colab notebook to download and test the app instantly:
```python
!curl -s https://raw.githubusercontent.com/angelroysms-maker/Personal-Planner/main/personal_planner.py -o remote_planner.py && python remote_planner.py
```
