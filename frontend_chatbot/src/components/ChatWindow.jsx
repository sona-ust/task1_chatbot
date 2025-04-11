import React, { useEffect, useRef } from 'react';
import MessageBubble from './MessageBubble';
 
function ChatWindow({ messages, isTyping }) {
  const bottomRef = useRef(null);
 
  // Auto-scroll to bottom when messages change
  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isTyping]);
 
  return (
    <div className="chat-window">
      {messages.map((msg, index) => (
        <MessageBubble key={index} sender={msg.sender} text={msg.text} />
      ))}
 
      {isTyping && (
        <MessageBubble sender="bot" text="Typing..." />
      )}
 
      <div ref={bottomRef} />
    </div>
  );
}
 
export default ChatWindow;