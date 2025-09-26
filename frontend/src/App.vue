<template>
  <div id="app">
    <TheHeader />
    <router-view />
    <TheFooter />
  </div>
</template>

<script>
import TheHeader from './components/layout/TheHeader.vue';
import TheFooter from './components/layout/TheFooter.vue';

export default {
  name: 'App',
  components: {
    TheHeader,
    TheFooter,
  },
};
</script>

<style>
/* Global styles */
body {
  margin: 0;
  overflow: hidden;
  transition: background-color 0.3s;
}

/* Add a global dark mode class for the body */
body.dark-mode-global {
  background-color: #1a2339; /* Darkish blue */
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
