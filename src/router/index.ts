import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home'

Vue.use(VueRouter)

let router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', name: 'Home', component: Home },
    { path: '/contact', name: 'Contact', component: () => import('../views/Contact') }
  ],
})

export default router