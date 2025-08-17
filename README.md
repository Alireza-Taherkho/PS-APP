## 📌 Features

- **System Setup**
  - Define game systems with pricing rules (per-minute or custom intervals).
  - Add your devices and link them to the predefined system types.

- **Game Session Management**
  - Start a new game by selecting device, controllers, and notes.
  - Track **start/end times** (with timestamps in the Iranian calendar).
  - Update session details (controllers, device name, notes).
  - End a session and calculate total cost automatically.

- **Smart Calculator for Notes**
  - Notes section only accepts numbers.
  - Acts like an **auto-calculator** for additions/subtractions.
  - Useful for consumables or extra charges without manual math.

- **Alarms**
  - Set alarms for either **time duration** (e.g., 50 minutes) or **amount** (e.g., 50,000 Toman).
  - Custom sound alerts when the time/credit is finished.
  - Option to stop or change alarm sounds.

- **History & Transactions**
  - **History Tab**: View all completed sessions.
  - **Deleted Sessions**: Track sessions that were started but deleted before completion.
  - **Transactions**: Filter by date and check total earnings.

- **Flexible Pricing Adjustments**
  - Combine sessions using a simple tag:  
    Example: `#5` → Adds the price of session ID 5 to the current one.  
    - The sum is reflected in the total but not duplicated in the history.

- **Game Cleanup Options**
  - Remove individual sessions or clear them in bulk.

---

## 🛠️ Tech Stack

- **Python 3**
- **Tkinter** (GUI)
- Additional Python libraries (for calendar, sound, etc.)

---
