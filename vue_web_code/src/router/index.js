import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/components/Home'
import Login from '@/components/Login'
import Cipher from '@/components/Cipher'

Vue.use(VueRouter)

const routes = [
  { path: '/login', component: Login, name: 'login' },
  { path: '/', component: Home },
  { path: '/Cipher', component: Cipher }
]

const router = new VueRouter({
  routes
})

export default router
