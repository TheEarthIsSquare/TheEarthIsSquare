import Vue from 'vue'
import Vuex from 'vuex'
import App from './App.vue'
import router from './router'
import { library } from '@fortawesome/fontawesome-svg-core'
import {faBars, faTimes} from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'


library.add(faBars, faTimes)

Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.use(Vuex)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')