<template>
  <div class="chat-window" :class="{ 'dark-mode': isDarkMode }">
    <div class="header">
      <h3>AI Chatbot</h3>
      <button @click="toggleDarkMode" class="dark-mode-toggle">
        {{ isDarkMode ? 'Light Mode' : 'Dark Mode' }}
      </button>
    </div>

    <div class="messages-display" ref="messagesDisplay">
      <div v-if="isLoading" class="message-item-wrapper chatbot">
        <div class="message-item chatbot">
            <div class="typing-indicator">
              <span></span><span></span><span></span>
            </div>
        </div>
      </div>
      <div v-for="(message, index) in messages" :key="index" :class="['message-item-wrapper', message.type]">
        <div :class="['message-item', message.type]">
          <!-- Use v-html to render markdown content -->
          <div class="content" v-html="renderMarkdown(message.text)"></div>
          <div class="timestamp">{{ formatTimestamp(message.timestamp) }}</div>
        </div>
      </div>
    </div>

    <div class="message-input-area">
      <input
        v-model="newMessage"
        @keyup.enter="sendMessage"
        placeholder="Type your message..."
        :disabled="isLoading"
      />
      <button @click="sendMessage" :disabled="isLoading">Send</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { nextTick } from 'vue';
import { marked } from 'marked'; // Import marked

export default {
  name: 'ChatWindow',
  data() {
    return {
      messages: [],
      newMessage: '',
      isLoading: false,
      isDarkMode: false,
      apiBaseUrl: 'http://localhost:5000/api/chat'
    };
  },
  methods: {
    renderMarkdown(text) {
      if (!text) return '';
      return marked(text);
    },
    formatTimestamp(date) {
      if (!date) return '';
      const d = new Date(date);
      if (isNaN(d.getTime())) return '';
      return d.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    },
    async scrollToBottom() {
      await nextTick();
      const container = this.$refs.messagesDisplay;
      if (container) {
        container.scrollTop = container.scrollHeight;
      }
    },
    async sendMessage() {
      if (this.newMessage.trim() === '' || this.isLoading) return;
      const userMessage = { type: 'user', text: this.newMessage, timestamp: new Date() };
      this.messages.push(userMessage);
      this.scrollToBottom();
      this.newMessage = '';
      this.isLoading = true;
      try {
        const response = await axios.post(this.apiBaseUrl, { message: userMessage.text });
        this.messages.push({ type: 'chatbot', text: response.data.response, timestamp: new Date() });
      } catch (error) {
        console.error('Error sending message:', error);
        this.messages.push({ type: 'chatbot', text: 'Error: Could not get a response.', timestamp: new Date() });
      } finally {
        this.isLoading = false;
        this.scrollToBottom();
      }
    },
    async fetchChatHistory() {
      this.isLoading = true;
      try {
        const response = await axios.get(this.apiBaseUrl);
        this.messages = response.data.history.map(item => ([
          { type: 'user', text: item.user_message, timestamp: new Date(item.timestamp) },
          { type: 'chatbot', text: item.chatbot_response, timestamp: new Date(item.timestamp) }
        ])).flat();
      } catch (error) {
        console.error('Error fetching chat history:', error);
      } finally {
        this.isLoading = false;
        this.scrollToBottom();
      }
    },
    toggleDarkMode() {
      this.isDarkMode = !this.isDarkMode;
      if (this.isDarkMode) {
        document.body.classList.add('dark-mode-global');
      } else {
        document.body.classList.remove('dark-mode-global');
      }
    }
  },
  mounted() {
    this.fetchChatHistory();
  }
};
</script>

<style scoped>
/* ... (previous styles are mostly the same) ... */
.content :deep(p) {
    margin: 0 0 0.5em 0;
}
.content :deep(p:last-child) {
    margin-bottom: 0;
}
.content :deep(ul), .content :deep(ol) {
    padding-left: 20px;
}
.chat-window {
  width: 90vw;
  height: 95vh;
  margin: 2.5vh auto;
  display: flex;
  flex-direction: column;
  border: 1px solid #ccc;
  border-radius: 8px;
  overflow: hidden;
  background-color: #fff;
  transition: background-color 0.3s, color 0.3s;
}
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  border-bottom: 1px solid #eee;
  background-color: #f7f7f7;
}
.dark-mode-toggle {
  padding: 5px 10px;
  border-radius: 20px;
  border: 1px solid #ccc;
  cursor: pointer;
  background-color: #fff;
}
.messages-display {
  display: flex;
  flex-direction: column; /* Reverted to column */
  flex-grow: 1;
  padding: 10px;
  overflow-y: auto;
  background-color: #f9f9f9;
  -ms-overflow-style: none;
  scrollbar-width: none;
}
.messages-display::-webkit-scrollbar {
  display: none;
}
.message-item-wrapper {
  display: flex;
  margin-bottom: 4px;
}
.message-item-wrapper.user {
  justify-content: flex-end;
}
.message-item-wrapper.chatbot {
  justify-content: flex-start;
}
.message-item {
  padding: 8px 12px;
  border-radius: 18px;
  max-width: 80%;
  word-wrap: break-word;
  text-align: left; /* Align text to the left within bubbles */
}
.message-item.user {
  background-color: #dcf8c6;
}
.message-item.chatbot {
  background-color: #f1f0f0;
}
.timestamp {
  font-size: 0.75em;
  color: #888;
  margin-top: 4px;
  text-align: right;
}
.typing-indicator {
  display: flex;
  padding: 8px 12px;
}
.typing-indicator span {
  height: 8px;
  width: 8px;
  margin: 0 2px;
  background-color: #9E9E9E;
  border-radius: 50%;
  display: inline-block;
  animation: bounce 1.4s infinite ease-in-out both;
}
.typing-indicator span:nth-child(1) { animation-delay: -0.32s; }
.typing-indicator span:nth-child(2) { animation-delay: -0.16s; }
@keyframes bounce {
  0%, 80%, 100% { transform: scale(0); }
  40% { transform: scale(1.0); }
}
.message-input-area {
  display: flex;
  padding: 10px;
  border-top: 1px solid #eee;
  background-color: #fff;
}
.message-input-area input {
  flex-grow: 1;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 20px;
  margin-right: 10px;
  outline: none;
}
.message-input-area button {
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 20px;
  cursor: pointer;
}
.message-input-area button:disabled {
  background-color: #a5d6a7;
  cursor: not-allowed;
}
.chat-window.dark-mode {
  background-color: #1a2339;
  color: #f0f0f0;
  border-color: #4a5568;
}
.chat-window.dark-mode .header {
  background-color: #2d3748;
  border-bottom-color: #4a5568;
}
.chat-window.dark-mode .dark-mode-toggle {
  background-color: #4a5568;
  color: #f0f0f0;
  border-color: #718096;
}
.chat-window.dark-mode .messages-display {
  background-color: #252d41;
}
.chat-window.dark-mode .message-item.user {
  background-color: #056162;
}
.chat-window.dark-mode .message-item.chatbot {
  background-color: #384259;
}
.chat-window.dark-mode .timestamp {
  color: #a0aec0;
}
.chat-window.dark-mode .message-input-area {
  background-color: #2d3748;
  border-top-color: #4a5568;
}
.chat-window.dark-mode .message-input-area input {
  background-color: #4a5568;
  border-color: #718096;
  color: #f0f0f0;
}
.chat-window.dark-mode .message-input-area button {
  background-color: #319795;
}
</style>
