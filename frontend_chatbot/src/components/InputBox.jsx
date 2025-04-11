import React, { useState } from 'react';
 
function InputBox({ onSend }) {
  const [message, setMessage] = useState('');
 
  const handleSend = () => {
    if (message.trim()) {
      onSend(message);
      setMessage('');
    }
  };
 
  return (
<div className="input-area">
<input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type your message..."
        onKeyPress={(e) => e.key === 'Enter' && handleSend()}
      />
      <button onClick={handleSend} className="send-btn">
        ➤
      </button>
</div>
  );
}
 
export default InputBox;