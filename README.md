# D4C - Dirty Deeds Done Dirt Cheap 🎭  
A versatile Discord user app with various commands.

D4C is a **legal** user application that runs on your own Discord account, much like a bot—but without breaking Discord’s Terms of Service. Unlike self-bots like `discordsb`, D4C connects through **user OAuth**, similar to how bots connect to servers.

---

## ✅ Legal & TOS-Friendly

D4C does **not** use self-botting or token hijacking. It uses Discord's **official user app authorization** methods. That means:

- You log in via Discord OAuth.
- You grant access to your own account, like logging into a connected service.
- D4C acts on your behalf using allowed API endpoints.

No token pasting or sketchy logins. Just clean, user-consented interaction.

---

## ⚙️ Installation

1. Clone the repository:  
   ```
   git clone https://github.com/bedxnta/d4c.git  
   cd d4c
   ```
   
2. Install dependencies:  
   ```
   pip install discord.py requests py-cord
   ```
   
3. Set up your app credentials (OAuth client ID/secret) in the config.

4. Run the app:  
   ```
   python main.py
   ```
   
---

## 🚀 Features

- 🎮 Execute commands from your own account
- 🛠️ Extendable architecture for custom modules
- 🔒 Safe & OAuth-based login
