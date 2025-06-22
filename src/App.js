import React from 'react';
import { motion } from 'framer-motion';
import { Mail } from 'lucide-react';

function SideNav() {
  return (
    <nav className="sidenav">
      <ul>
        <li>Inbox</li>
        <li>Sent</li>
        <li>Archive</li>
      </ul>
    </nav>
  );
}

function MessageItem({ message }) {
  return (
    <motion.div whileHover={{ scale: 1.02 }} className="message-item">
      <Mail size={16} /> {message}
    </motion.div>
  );
}

function MessagesPage() {
  const messages = ['Welcome to the portal!', 'Your rent is due'];
  return (
    <div className="messages-page">
      {messages.map((m, i) => (
        <MessageItem key={i} message={m} />
      ))}
    </div>
  );
}

export default function App() {
  return (
    <div className="app">
      <SideNav />
      <main>
        <h1>Housing Portal</h1>
        <MessagesPage />
      </main>
    </div>
  );
}
