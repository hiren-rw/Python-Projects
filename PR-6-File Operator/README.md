<div align="center"> 

  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:FF6A00,100:EE0979&height=300&section=header&text=File%20Operator&fontSize=58&fontColor=ffffff&animation=fadeIn&desc=📓%20Personal%20Journal%20Manager&descAlignY=65&descSize=18" width="100%" height="100%"/> 
</div>

<br>

[![Typing SVG](https://readme-typing-svg.demolab.com/?font=Fira+Code&size=18&pause=1000&color=FF6A00&center=true&vCenter=true&width=700&lines=Read+%7C+Append+%7C+Search+%7C+Delete;try-except+%7C+FileNotFoundError+%7C+with+open;JournalManager+%7C+match-case+%7C+datetime+%F0%9F%93%93)](https://git.io/typing-svg)

<br>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Level](https://img.shields.io/badge/Level-Beginner-00C896?style=for-the-badge)
![Focus](https://img.shields.io/badge/Focus-File%20Handling%20%26%20OOP-FF6A00?style=for-the-badge)
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

> **Build a menu-driven journal app that stores your entries in a text file.**

This project — titled **"File Operator"** — uses a `JournalManager` class to add, view, search and delete journal entries saved in `journal.txt`, with errors handled so the program never crashes. 📓

<br>

<a id="features"></a>

## ✨ WHAT'S INSIDE?

<div align="center">

| 🧩 Concept | 📌 How It's Used |
|:---:|:---|
| 🏛️ **Classes & Objects** | `JournalManager` holds every operation as an instance method; one `journal` object runs the program |
| 📂 **File Handling** | `open()` in `"r"` mode reads entries, `"a"` mode appends them (and creates `journal.txt` if missing) |
| 🗑️ **Delete File** | `os.remove()` clears all entries at once, after a `y/n` confirmation |
| 🕒 **Timestamp** | `datetime.now().strftime()` stamps every entry with the date and time |
| 🔎 **Search** | Finds entries by keyword or date, ignoring upper/lower case |
| 🛡️ **Error Handling** | `try-except` catches `FileNotFoundError` and other errors with clear messages |
| ✅ **Input Checks** | Empty entries, empty searches and invalid menu options are rejected politely |
| 🔀 **`match-case`** | Clean 5-option menu routing |

</div>

---

<a id="how-it-works"></a>

## 🖥️ HOW IT WORKS

```mermaid
graph TD
    M[🔁 Menu Loop] --> A[➕ add_entry<br/>mode a]
    M --> V[📖 view_entries<br/>mode r]
    M --> S[🔎 search_entries<br/>mode r]
    M --> D[🗑️ delete_entries<br/>os.remove]
    A --> F[(📄 journal.txt)]
    V --> F
    S --> F
    D --> F
```

```text
👋 Welcome Message
   │
   ▼
📜 Show Menu (1-5)
   │
   ├── 1️⃣ Add a New Entry      → type text, saved with a timestamp
   ├── 2️⃣ View All Entries     → show everything in journal.txt
   ├── 3️⃣ Search for an Entry  → keyword or date, show matches
   ├── 4️⃣ Delete All Entries   → confirm (y/n), then delete the file
   └── 5️⃣ Exit                 → goodbye message
   │
   ▼
🔁 Repeats until Exit
```

> 📝 **Key design choice:** each entry is saved as a `Timestamp : [date time]` line followed by your text, with a blank line between entries. Deleting the file removes all entries at once.

<details>
<summary>🧾 <b>Click to see a sample run</b></summary>

<br>

```text
Enter your choice : 1

Enter your journal entry (press Enter to finish) :
Hello there! This is my first entry in my journal.  Bye..

Entry added successfully!

Enter your choice : 3

Enter a keyword or date to search : my

Matching Entries :
---------------------------------
Timestamp : [2026-09-30 15:36:55]
Hello there! This is my first entry in my journal.  Bye..

Enter your choice : 4

Are you sure you want to delete all entries? (y/n) : y

All journal entries have been deleted.

Enter your choice : 5

Thank you for using Personal Journal Manager. Goodbye!
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
<img src="6_code_ss.png" alt="File Operator Code Screenshot" width="100%">
</td>
<td align="center" width="50%">
<b>🖨️ Output</b><br><br>
<img src="6_output_ss.png" alt="File Operator Output Screenshot" width="100%">
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
cd Python-Projects/"PR-6-File Operator"

# 2️⃣ Run the program
python "Project-6.py"
```

Follow the on-screen menu to add, view, search and delete your journal entries. `journal.txt` is created automatically when you add your first entry. 🎉

---

<a id="structure"></a>

## 📁 PROJECT STRUCTURE

```text
PR-6-File Operator/
│
├── 🐍 Project-6.py
├── 🖼️ 6_code_ss.png
├── 🖼️ 6_output_ss.png
└── 📘 README.md
```

> 🎬 The demo video (`PR-6-File Operator.mp4`) is available in the repository's [Releases](https://github.com/hiren-rw/Python-Projects/releases).

---

## 🎓 LEARNING OUTCOMES

<div align="center">

`File Handling` • `Read & Append Modes` • `os.remove()` • `Exception Handling` • `Classes & Objects`
`datetime` • `match-case`

</div>

---

<a id="author"></a>

## 👨‍💻 AUTHOR

<div align="center">

**Hiren RW**

[![GitHub](https://img.shields.io/badge/GitHub-hiren--rw-181717?style=for-the-badge&logo=github)](https://github.com/hiren-rw)
[![Portfolio](https://img.shields.io/badge/Repo-Python--Projects-EE0979?style=for-the-badge&logo=bookstack&logoColor=white)](https://github.com/hiren-rw/Python-Projects)

### 🚀 One small project. Many file handling fundamentals.

**Built with 🐍 Python & curiosity.**

⭐ *Keep learning. Keep building.*

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:FF6A00,100:EE0979&height=100&section=footer" width="100%" height="100%"/>

</div>
