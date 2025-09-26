import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView,
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/LoginView.vue'),
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: () => import('../views/DashboardView.vue'),
  },
  // Add ChatWindow to a route
  {
    path: '/chat',
    name: 'Chat',
    component: () => import('../components/ChatWindow.vue'),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
