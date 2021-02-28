import { createRouter, createWebHistory } from "vue-router";
// import Home from '../views/Home/Home.vue'
import ComingSoon from "@/views/ComingSoon/ComingSoon.vue";

const routes = [
  {
    path: '/',
    name: 'ComingSoon',
    component: ComingSoon
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
