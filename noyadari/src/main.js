import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Routes from './routes'
import VueResource from 'vue-resource'
import Buefy from 'buefy'
import 'buefy/lib/buefy.css'
import VueFire from 'vuefire'
import VueQrcodeReader from 'vue-qrcode-reader'

Vue.use(VueQrcodeReader);
Vue.use(VueFire);
Vue.use(Buefy,{defaultIconPack: 'fa'});

Vue.use(VueRouter);
Vue.use(VueResource);




const router = new VueRouter({
  mode: 'history',
  routes: Routes
});

Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
  router: router
}).$mount('#app')
