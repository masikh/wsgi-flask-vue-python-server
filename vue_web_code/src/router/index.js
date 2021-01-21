import Vue from 'vue'
import VueRouter from 'vue-router'
import Accounts from '@/components/Accounts'
import AccountCreate from '@/components/AccountCreate'
import Password from '@/components/Password'
import Home from '@/components/Home'
import Login from '@/components/Login'
import Cipher from '@/components/Cipher'
import CharacterWidgets from '@/components/CharacterWidgets'

Vue.use(VueRouter)

const routes = [
  { path: '/login', component: Login, name: 'login' },
  { path: '/', component: Home },
  { path: '/accounts', component: Accounts },
  { path: '/new_account', component: AccountCreate },
  { path: '/password', component: Password },
  { path: '/Cipher', component: Cipher },
  { path: '/CharacterWidgets', component: CharacterWidgets }
]

const router = new VueRouter({
  routes
})

export default router
