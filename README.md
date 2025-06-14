
# 💬 Real-Time Chat App with Django & WebSockets



A complete real-time messaging platform with public/private chats, group management, and live user status tracking.

## ✨ Key Features
- **Multi-channel Chatting**
  - 📢 Public chat room
  - 🔒 Private 1-on-1 conversations
  - 👥 Admin-managed group chats
- **Real-Time Indicators**
  - 💚 Live online/offline status
  - ⚡ Instant message delivery
- **Group Controls**
  - 🛠️ Admin: Rename groups/remove members
  - 👋 Members: Leave groups
- **Media Support**
  - 📁 File attachments
  - 🖼️ Image sharing

## 🛠 Tech Stack
| Backend          | Frontend     | Tools       |
|------------------|--------------|-------------|
| Django           | HTMX         | Pipenv      |
| Django Channels  | WebSockets   | PostgreSQL  |

## 🚀 Installation
```bash
# 1. Clone and enter project
git clone https://github.com/lamaDayoub/django-realTimeChat
cd realtime_chat

# 2. Setup environment
pipenv install && pipenv shell
echo "SECRET_KEY=your-key-here" > .env
echo "DEBUG=True" >> .env

# 3. Initialize database
python manage.py migrate

# 4. Create admin (optional)
python manage.py createsuperuser

# 5. Run development server
python manage.py runserver
```
Access at: `http://localhost:8000`

## 🌟 Usage Guide
1. **Sign up** for an account
2. **Public Chat**: Automatically join main room
3. **Private Chat**: Click any user's profile
4. **Create Group**: Via navigation menu
5. **Manage Groups**: Admin tools appear for group creators

