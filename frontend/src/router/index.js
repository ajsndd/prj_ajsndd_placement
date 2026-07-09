// /prj/frontend/src/router/index.js

import { createRouter, createWebHistory } from 'vue-router'
import login from '../components/login.vue'
import register from '../components/register.vue'
import jwtDecode from 'jwt-decode'

// Define routes with meta roles
const routes = [
  { path: '/login', name: 'login', component: login },
  { path: '/register', name: 'register', component: register },
  { path: '/', redirect: '/login' },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// Global navigation guard
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')

  if (to.meta.role) {
    if (!token) return next('/login')

    try {
      const user = jwtDecode(token)

      if (user.role !== to.meta.role) {
        return next('/login')
      }
    } catch {
      localStorage.removeItem('token')
      return next('/login')
    }
  }

  next()
})

export default router
