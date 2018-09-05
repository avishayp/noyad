import Vue from 'vue'
import VueQrcodeReader from 'vue-qrcode-reader'
import App from './App.vue'
import router from './routes'
import store from './store'

// === style
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue);
Vue.use(VueQrcodeReader);

let app;

store.commit('waitUser', function() {
  if (!app) {
    console.log('creating vue app instance')
    app = new Vue({
      el: '#app',
      router,
      store,
      render: h => h(App)
    })
  }
})