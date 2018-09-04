import Home from './components/Home.vue'
import Login from './components/Login.vue'
import AddItem from './components/AddItem.vue'
export default [
    {
        path: '/',
        name: 'login',
        component: Login
    },
    {
        path: '/home',
        name: 'home',
        component: Home
    },
    {
        path: '/additems',
        name: 'additem',
        component: AddItem
    }
]