import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import VueClipboard from 'vue-clipboard2'
import VueTippy from 'vue-tippy'

Vue.use(VueTippy);
Vue.use(VueClipboard);

Vue.config.productionTip = false;

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app');
