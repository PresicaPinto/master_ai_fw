<template>
  <div class="home-view">
    <ChatWindow />
  </div>
</template>

<script>
// Import the ChatWindow component
import ChatWindow from '@/components/ChatWindow.vue';

export default {
  name: 'HomeView',
  components: {
    ChatWindow, // Register the component
  },
};
</script>

<style scoped>
.home-view {
  height: calc(100vh - 50px); /* Example: full viewport height minus a navbar */
  padding: 20px;
}
</style>
