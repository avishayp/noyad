// components
import Home from './components/Home.vue'
import Login from './components/Login.vue'
import AddItem from './components/AddItem.vue'
import EditItem from './components/EditItem.vue'

// state
import store from './store'

// routes
import Vue from 'vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter);

const routes = [
    {
        name: 'login',
        path: '/login',
        component: Login,
        meta: {
            allowNonauthenticated: true
        }
    },
    {
        path: '/home',
        component: Home
    },
    {
        path: '/add',
        component: AddItem
    },
    {
        path: '/edit',
        component: EditItem
    },
    {
        path: '*',
        redirect: '/home'
    }
]

const router = new VueRouter({
    mode: 'history',
    routes: routes
})

// redirect to the sign-in page if no user authenticated
router.beforeEach( (to, from, next)  => {
    console.log('nav guard', from.path, to.path, 'user:', store.getters.userName)
    if (to.name == 'login' && store.getters.userName) {
        console.log('already logged in', store.getters.userName)
        next('/home')
    }

    else if (!to.meta.allowNonauthenticated && !store.getters.userName) {
        console.log('route', to.path, 'requires authentication')
        next('/login')
    }

    else {
        next()
    }
});

export default router