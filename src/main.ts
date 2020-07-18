import Vue from 'vue'
import Vuex from 'vuex'
import App from './App.vue'
import router from './router'
import VueAxios from './plugins/axios'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faInstagram } from '@fortawesome/free-brands-svg-icons'
import { faBars, faTimes, faArrowRight, faCheckCircle } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
// @ts-ignore
import { SquareSpinner } from 'vue-spinners'

library.add(faBars, faTimes, faArrowRight, faInstagram, faCheckCircle)

Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.component('square', SquareSpinner)

Vue.use(Vuex)
Vue.use(VueAxios)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')