import Vue from 'vue'
import VueFire from 'vuefire';
import VueQrcodeReader from 'vue-qrcode-reader'
import App from './App.vue'
import router from './routes'
import store from './store'

import VueChartkick from 'vue-chartkick'
import Highcharts from 'highcharts'

// map display
import VueMapbox from 'vue-mapbox'
import Mapbox from 'mapbox-gl'

// === style
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue);
Vue.use(VueFire);
Vue.use(VueQrcodeReader);
Vue.use(VueChartkick, {adapter: Highcharts})
Vue.use(VueMapbox, { mapboxgl: Mapbox })

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