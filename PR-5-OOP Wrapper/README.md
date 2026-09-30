<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0072FF,100:00C9A7&height=200&section=header&text=OOP%20Wrapper&fontSize=52&fontColor=ffffff&animation=fadeIn&desc=🏢%20Employee%20Management%20System&descAlignY=62&descSize=18" width="100%" height="200"/>

<br>

[![Typing SVG](https://readme-typing-svg.demolab.com/?font=Fira+Code&size=18&pause=1000&color=00C9A7&center=true&vCenter=true&width=700&lines=Classes+%7C+Objects+%7C+Inheritance+%7C+Encapsulation;Method+Overriding+%7C+super+%7C+issubclass+%7C+__del__;Person+%E2%86%92+Employee+%E2%86%92+Manager+%26+Developer+%F0%9F%90%8D)](https://git.io/typing-svg)

<br>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Level](https://img.shields.io/badge/Level-Intermediate-00C896?style=for-the-badge)
![Focus](https://img.shields.io/badge/Focus-Object%20Oriented%20Programming-0072FF?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)

</div>

<br>

## 📑 Table of Contents

<div align="center">

[🎯 Objective](#objective) • [✨ Features](#features) • [🖥️ Flow](#how-it-works) • [📸 Preview](#preview) • [🎬 Demo](#demo) • [▶️ Run It](#run) • [📁 Structure](#structure) • [👨‍💻 Author](#author)

</div>

---

<a id="objective"></a>

## 🎯 OBJECTIVE

> **Build a menu-driven Employee Management System that puts Python's OOP concepts to work.**

This project — titled **"OOP Wrapper"** — uses a class hierarchy of `Person`, `Employee`, `Manager` and `Developer` to create, store and display employee records from a simple console menu. 🧑‍💼

<br>

<a id="features"></a>

## ✨ WHAT'S INSIDE?

<div align="center">

| 🧩 Concept | 📌 How It's Used |
|:---:|:---|
| 🏛️ **Classes & Objects** | `Person`, `Employee`, `Manager`, `Developer` — objects stored in a `database` dictionary |
| 🧬 **Inheritance** | Multilevel: `Person → Employee → Manager / Developer`, with `Manager` and `Developer` both extending `Employee` |
| 🔒 **Encapsulation** | Private `__emp_id` and `__salary`, accessed through getters & setters |
| 🔄 **Method Overriding** | Each subclass extends `display()` to show its own extra details |
| ⬆️ **`super()`** | Calls the parent's constructor and `display()` |
| 🎛️ **Default Arguments** | `emp_id=None, salary=0.0` simulate method overloading |
| 🧹 **Destructor `__del__`** | Defined in `Person` and `Employee`; `database.clear()` on exit releases the objects |
| 🔎 **`issubclass()`** | Verifies a class is a subclass of `Employee` before showing its records |
| 🔀 **`match-case`** | Clean 6-option menu routing |
| 🛡️ **Error Handling** | `try-except` catches invalid menu input |

</div>

---

<a id="how-it-works"></a>

## 🖥️ HOW IT WORKS

```mermaid
graph TD
    P[👤 Person<br/>name, age] --> E[💼 Employee<br/>+ emp_id, salary]
    E --> M[🧑‍💼 Manager<br/>+ department]
    E --> D[👨‍💻 Developer<br/>+ programming_language]
```

```text
👋 Welcome Message
   │
   ▼
📜 Show Menu (1-6)
   │
   ├── 1️⃣ Create a Person     → name, age
   ├── 2️⃣ Create an Employee  → + employee ID, salary
   ├── 3️⃣ Create a Manager    → + department
   ├── 4️⃣ Create a Developer  → + programming language
   ├── 5️⃣ Show Details        → pick a class, display all its records
   └── 6️⃣ Exit                → free all objects, goodbye message
   │
   ▼
🔁 Repeats until Exit
```

> 🔐 **Key design choice:** `emp_id` and `salary` are **private** attributes, so they can only be read or changed through getters and setters.

<details>
<summary>🧾 <b>Click to see a sample run</b></summary>

<br>

```text
Enter your choice: 3

Enter Name: CCC
Enter Age: 33
Enter Employee ID: 333
Enter Salary: 3333
Enter Department: CC

Manager created with name: CCC, age: 33, ID: 333, salary: $3333.0, and department: CC.

Enter your choice: 5

Choose details to show:
1. Person
2. Employee
3. Manager
4. Developer

Enter your choice: 3

[System Info: Verified that Manager is a subclass of Employee]

Manager Details:
Name :  CCC
Age :  33
Employee ID: 333
Salary: $3333.0
Department: CC

Enter your choice: 6

Exiting the system. All resources have been freed.

Goodbye!
```

</details>

---

<a id="preview"></a>

## 📸 PREVIEW

<div align="center">

<table>
<tr>
<td align="center" width="50%">
<b>🧑‍💻 Code</b><br><br>
<img src="5_code_ss.png" alt="OOP Wrapper Code Screenshot" width="100%">
</td>
<td align="center" width="50%">
<b>🖨️ Output</b><br><br>
<img src="5_output_ss.png" alt="OOP Wrapper Output Screenshot" width="100%">
</td>
</tr>
</table>

</div>

---

<a id="demo"></a>

## 🎬 VIDEO EXPLANATION

<div align="center">

[![Watch the Demo](https://img.shields.io/badge/▶️_WATCH_DEMO-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://github.com/hiren-rw/Python-Projects/releases)

*Click the button above and open the release to watch the full walkthrough* 🎥

</div>

---

<a id="run"></a>

## ▶️ RUN THE PROJECT

Requires **Python 3.10+** (for `match-case`).

```bash
# 1️⃣ Clone the repository
git clone https://github.com/hiren-rw/Python-Projects.git
cd Python-Projects/"PR-5-OOP Wrapper"

# 2️⃣ Run the program
python "Project-5.py"
```

Follow the on-screen menu to create people, employees, managers and developers, then view their details. 🎉

---

<a id="structure"></a>

## 📁 PROJECT STRUCTURE

```text
PR-5-OOP Wrapper/
│
├── 🐍 Project-5.py
├── 🖼️ 5_code_ss.png
├── 🖼️ 5_output_ss.png
└── 📘 README.md
```

> 🎬 The demo video (`PR-5-OOP Wrapper.mp4`) is available in the repository's [Releases](https://github.com/hiren-rw/Python-Projects/releases).

---

## 🎓 LEARNING OUTCOMES

<div align="center">

`Classes & Objects` • `Inheritance` • `Encapsulation` • `Method Overriding` • `super()`
`Default Arguments` • `Destructor` • `issubclass()` • `match-case`

</div>

---

<a id="author"></a>

## 👨‍💻 AUTHOR

<div align="center">

**Hiren RW**

[![GitHub](https://img.shields.io/badge/GitHub-hiren--rw-181717?style=for-the-badge&logo=github)](https://github.com/hiren-rw)
[![Portfolio](https://img.shields.io/badge/Repo-Python--Projects-0072FF?style=for-the-badge&logo=bookstack&logoColor=white)](https://github.com/hiren-rw/Python-Projects)

### 🚀 One small project. Many OOP fundamentals.

**Built with 🐍 Python & curiosity.**

⭐ *Keep learning. Keep building.*

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0072FF,100:00C9A7&height=100&section=footer" width="100%" height="100"/>

</div>
