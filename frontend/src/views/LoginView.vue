<template>
  <div class="login-view">
    <h2>Login</h2>
    <form @submit.prevent="login">
      <input type="email" placeholder="Email" v-model="email" />
      <input type="password" placeholder="Password" v-model="password" />
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    login() {
      console.log('Logging in with:', this.email, this.password);
      // Implement actual login logic here
    },
  },
};
</script>

<style scoped>
.login-view {
  padding: 20px;
}
</style>
